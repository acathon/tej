import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from backend.app.engine.validators import is_valid_matricule_fiscal  # noqa: E402


def validate_matricule_fiscal(value: str) -> bool:
    """Validate Tunisian tax ID format: 1234567AMN000 or 1234567/A/M/N/000."""
    return is_valid_matricule_fiscal(value)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python validate_matricule.py <MATRICULE>")
        return 1

    matricule = sys.argv[1]
    is_valid = validate_matricule_fiscal(matricule)
    print("valid" if is_valid else "invalid")
    return 0 if is_valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
