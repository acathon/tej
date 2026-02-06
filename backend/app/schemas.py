from datetime import datetime
from typing import Any

import re

from pydantic import BaseModel, Field, field_validator, model_validator

MATRICULE_REGEX = r"^\d{7}[A-Z]{3}\d{3}$"


class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=8)


class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class EnterpriseCreate(BaseModel):
    owner_id: int
    legal_name: str = Field(..., min_length=2)
    matricule_fiscal: str
    contact_email: str | None = None


class EnterpriseRead(BaseModel):
    id: int
    owner_id: int
    legal_name: str
    matricule_fiscal: str
    contact_email: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MatriculeFiscal(BaseModel):
    raw_value: str = Field(..., description="Le matricule complet sans séparateurs")

    @field_validator("raw_value")
    @classmethod
    def validate_format(cls, value: str) -> str:
        normalized = value.upper().replace("/", "").replace(" ", "")
        if not re.match(MATRICULE_REGEX, normalized):
            raise ValueError(
                "Format de matricule fiscal invalide (Ex: 1234567AMN000)"
            )
        return normalized


class DocumentCreate(BaseModel):
    enterprise_id: int
    filename: str
    mime_type: str
    storage_path: str
    extracted_payload: dict[str, Any]


class DocumentRead(BaseModel):
    id: int
    enterprise_id: int
    filename: str
    mime_type: str
    storage_path: str
    extracted_payload: dict[str, Any]
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class WithholdingCertificateCreate(BaseModel):
    enterprise_id: int
    document_id: int | None = None
    source_filename: str
    period: str
    gross_amount: float
    withholding_rate: float
    net_payable: float
    extracted_payload: dict[str, Any]
    notes: str | None = None


class WithholdingCertificateRead(BaseModel):
    id: int
    enterprise_id: int
    document_id: int | None
    source_filename: str
    period: str
    gross_amount: float
    withholding_rate: float
    net_payable: float
    extracted_payload: dict[str, Any]
    validation_status: str
    notes: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ExportHistoryCreate(BaseModel):
    enterprise_id: int
    period: str
    export_format: str = Field(default="xml")
    metadata: dict[str, Any]


class ExportHistoryRead(BaseModel):
    id: int
    enterprise_id: int
    period: str
    export_format: str
    status: str
    metadata: dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True


class RetenueSource(BaseModel):
    identifiant_beneficiaire: MatriculeFiscal
    nom_beneficiaire: str
    code_retenue: str = Field(..., description="Ex: J pour Honoraires, R pour Loyers")
    montant_brut: float = Field(..., gt=0)
    taux_retenue: float = Field(..., ge=0, le=100)
    montant_retenue: float
    montant_net: float

    @model_validator(mode="after")
    def check_arithmetic(self) -> "RetenueSource":
        expected_retenue = round(self.montant_brut * (self.taux_retenue / 100), 3)
        if abs(self.montant_retenue - expected_retenue) > 0.005:
            raise ValueError(
                "Incohérence : Le montant de retenue "
                f"({self.montant_retenue}) ne correspond pas "
                f"au calcul ({expected_retenue})"
            )
        if abs(self.montant_net - (self.montant_brut - self.montant_retenue)) > 0.005:
            raise ValueError(
                "Le montant net est incorrect par rapport au brut et à la retenue."
            )
        return self
