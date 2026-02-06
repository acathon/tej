# TEJ-Fisc Project Structure

## Backend (FastAPI)
```
backend/
  app/
    api/                 # Endpoints (v1/auth, v1/extract, v1/fiscal)
    core/                # Config, sécurité (JWT), constantes fiscales
    engine/              # Cœur métier (OCR, XML, validators)
    models/              # SQLAlchemy models
    schemas/             # Pydantic schemas
    main.py              # FastAPI entrypoint
  tests/                 # Tests unitaires fiscaux
  docker-compose.yml
```

## Frontend (Angular 19)
```
frontend/
  src/
    app/
      core/              # Guards, interceptors, services globaux
      features/
        dashboard/       # Idée E (Control Tower)
        upload/          # Idée A (Smart Connector)
        audit/           # Idée C (Pre-Audit Shield)
        solo/            # Idée B (Tax Wallet)
      shared/            # UI (Bento, Glassmorphism)
    app.config.ts        # Signals & configuration
  tailwind.config.js
```
