import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.ports.email.api.email_router import router as email_router

logging.basicConfig(level=logging.DEBUG if settings.debug_logs else logging.INFO)

app = FastAPI(
    title=settings.project_name,
    description="api documentation of the project",
    debug=settings.debug_logs,
)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(email_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
