from fastapi import APIRouter

from backend.app.api.v1 import auth, extract, fiscal

router = APIRouter()
router.include_router(auth.router)
router.include_router(extract.router)
router.include_router(fiscal.router)


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
