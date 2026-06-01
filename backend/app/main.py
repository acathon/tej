from fastapi import FastAPI

app = FastAPI(title="TEJ-Fisc")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
