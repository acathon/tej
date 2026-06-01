import re
import sys

MAT_FISCAL_PATTERN = re.compile(r"^\d{7}[A-Z]{3}\d{3}$")


def validate_matricule_fiscal(value: str) -> bool:
    """Validate Tunisian tax ID format: 1234567AMN000 or 1234567/A/M/N/000."""
    normalized = value.upper().replace("/", "").replace(" ", "")
    return bool(MAT_FISCAL_PATTERN.match(normalized))


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
