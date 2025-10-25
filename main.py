from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from link.views import router as links_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    title="LinkTrim API",
    description="API LinkTrim",
    version="0.1.0",
)

app.include_router(links_router, tags=["links"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
