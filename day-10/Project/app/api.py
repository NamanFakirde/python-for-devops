# this is the APi file which connects the endpoints 

from fastapi import FastAPI
from router import health_route, aws_route, log_route

app = FastAPI (
    title = "Internal utilities API",
    description = "This is the internal devops utilites API to help team to work effeciently such as AWS usage, log analysis and health.",
    version = "1.0.0",
    docs_url = "/doc",
    redoc_url = "/redoc",
)

app.include_router(health_route.router)
app.include_router(aws_route.router, prefix="/aws")
app.include_router(log_route.router)
