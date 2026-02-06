# TEJ-Fisc Database Schema (SQLAlchemy)

## Users
Représente un compte utilisateur (auth/JWT).

- `id` (PK)
- `email`
- `hashed_password`
- `is_active`
- `created_at`
- `updated_at`

## Enterprises (Dossiers)
Représente un "Dossier Entreprise" (dossier client).

- `id` (PK)
- `owner_id` (FK -> Users)
- `legal_name`
- `matricule_fiscal`
- `contact_email`
- `status`
- `created_at`
- `updated_at`

## Documents
Documents sources (PDF/images/Excel) liés à une entreprise.

- `id` (PK)
- `enterprise_id` (FK -> Enterprises)
- `filename`
- `mime_type`
- `storage_path`
- `extracted_payload` (JSON)
- `status`
- `created_at`
- `updated_at`

## WithholdingCertificates
Représente un "Certificat de Retenue à la Source".

- `id` (PK)
- `enterprise_id` (FK -> Enterprises)
- `document_id` (FK -> Documents)
- `source_filename`
- `period`
- `gross_amount`
- `withholding_rate`
- `net_payable`
- `extracted_payload` (JSON)
- `validation_status`
- `notes`
- `created_at`
- `updated_at`

## ExportHistory
Historique des exports (XML/ZIP).

- `id` (PK)
- `enterprise_id` (FK -> Enterprises)
- `period`
- `export_format`
- `status`
- `metadata` (JSON)
- `created_at`
