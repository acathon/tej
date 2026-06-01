from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    enterprises: Mapped[list["Enterprise"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )


class Enterprise(Base):
    __tablename__ = "enterprises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    legal_name: Mapped[str] = mapped_column(String(255), nullable=False)
    matricule_fiscal: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    contact_email: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(32), default="active")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    owner: Mapped[User] = relationship(back_populates="enterprises")
    documents: Mapped[list["Document"]] = relationship(
        back_populates="enterprise", cascade="all, delete-orphan"
    )
    certificates: Mapped[list["WithholdingCertificate"]] = relationship(
        back_populates="enterprise", cascade="all, delete-orphan"
    )
    export_history: Mapped[list["ExportHistory"]] = relationship(
        back_populates="enterprise", cascade="all, delete-orphan"
    )


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    enterprise_id: Mapped[int] = mapped_column(
        ForeignKey("enterprises.id", ondelete="CASCADE"), nullable=False, index=True
    )
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(128), nullable=False)
    storage_path: Mapped[str] = mapped_column(String(512), nullable=False)
    extracted_payload: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="uploaded")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    enterprise: Mapped[Enterprise] = relationship(back_populates="documents")


class WithholdingCertificate(Base):
    __tablename__ = "withholding_certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    enterprise_id: Mapped[int] = mapped_column(
        ForeignKey("enterprises.id", ondelete="CASCADE"), nullable=False, index=True
    )
    document_id: Mapped[int | None] = mapped_column(
        ForeignKey("documents.id", ondelete="SET NULL"), index=True
    )
    source_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    period: Mapped[str] = mapped_column(String(16), nullable=False)
    gross_amount: Mapped[float] = mapped_column(Float, nullable=False)
    withholding_rate: Mapped[float] = mapped_column(Float, nullable=False)
    net_payable: Mapped[float] = mapped_column(Float, nullable=False)
    extracted_payload: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(String(32), default="pending")
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    enterprise: Mapped[Enterprise] = relationship(back_populates="certificates")
    document: Mapped[Document | None] = relationship()


class ExportHistory(Base):
    __tablename__ = "export_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    enterprise_id: Mapped[int] = mapped_column(
        ForeignKey("enterprises.id", ondelete="CASCADE"), nullable=False, index=True
    )
    period: Mapped[str] = mapped_column(String(16), nullable=False)
    export_format: Mapped[str] = mapped_column(String(16), default="xml")
    status: Mapped[str] = mapped_column(String(32), default="pending")
    export_metadata: Mapped[dict[str, Any]] = mapped_column(
        "metadata", JSON, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    enterprise: Mapped[Enterprise] = relationship(back_populates="export_history")
