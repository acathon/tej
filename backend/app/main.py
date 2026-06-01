from fastapi import FastAPI

from backend.app.api.v1.routes import router as v1_router

app = FastAPI(title="TEJ-Fisc")
app.include_router(v1_router)
