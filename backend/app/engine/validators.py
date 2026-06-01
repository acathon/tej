import re

MATRICULE_REGEX = r"^\d{7}[A-Z]{3}\d{3}$"
MATRICULE_PATTERN = re.compile(MATRICULE_REGEX)


def normalize_matricule_fiscal(value: str) -> str:
    return value.upper().replace("/", "").replace(" ", "")


def is_valid_matricule_fiscal(value: str) -> bool:
    return bool(MATRICULE_PATTERN.match(normalize_matricule_fiscal(value)))
