from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

try:
    from backend.app.schemas import MatriculeFiscal, RetenueSource  # noqa: E402
    PYDANTIC_AVAILABLE = True
except ModuleNotFoundError as exc:  # pragma: no cover - environment dependent
    if exc.name != "pydantic":
        raise
    PYDANTIC_AVAILABLE = False


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        ("1234567AMN000", "1234567AMN000"),
        ("1234567/A/M/N/000", "1234567AMN000"),
        ("1234567 a m n 000", "1234567AMN000"),
    ],
)
def test_matricule_normalization(input_value: str, expected: str) -> None:
    if not PYDANTIC_AVAILABLE:
        pytest.skip("pydantic not installed")
    matricule = MatriculeFiscal(raw_value=input_value)
    assert matricule.raw_value == expected


def test_retenue_source_arithmetic_passes() -> None:
    if not PYDANTIC_AVAILABLE:
        pytest.skip("pydantic not installed")
    retenue = RetenueSource(
        identifiant_beneficiaire=MatriculeFiscal(raw_value="1234567AMN000"),
        nom_beneficiaire="Test Beneficiaire",
        code_retenue="J",
        montant_brut=1000.0,
        taux_retenue=10.0,
        montant_retenue=100.0,
        montant_net=900.0,
    )
    assert retenue.montant_net == 900.0


def test_retenue_source_arithmetic_fails() -> None:
    if not PYDANTIC_AVAILABLE:
        pytest.skip("pydantic not installed")
    with pytest.raises(ValueError, match="Incohérence"):
        RetenueSource(
            identifiant_beneficiaire=MatriculeFiscal(raw_value="1234567AMN000"),
            nom_beneficiaire="Test Beneficiaire",
            code_retenue="J",
            montant_brut=1000.0,
            taux_retenue=10.0,
            montant_retenue=110.0,
            montant_net=890.0,
        )


def test_export_history_uses_non_reserved_metadata_attribute() -> None:
    model_source = (PROJECT_ROOT / "backend" / "app" / "models.py").read_text()

    model_lines = model_source.splitlines()

    assert not any(line.startswith("    metadata: Mapped") for line in model_lines)
    assert any(line.startswith("    export_metadata: Mapped") for line in model_lines)
    assert 'mapped_column(\n        "metadata", JSON, nullable=False\n    )' in model_source
