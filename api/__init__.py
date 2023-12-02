from contextlib import asynccontextmanager
import asyncio
from fastapi import FastAPI
from api.router import router
from prometheus_client import make_asgi_app
from api.consumer import consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    register_metrics = asyncio.create_task(consumer())

    yield

    register_metrics.cancel()


app = FastAPI(lifespan=lifespan)

app.include_router(router=router, prefix="/api/v1")

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
