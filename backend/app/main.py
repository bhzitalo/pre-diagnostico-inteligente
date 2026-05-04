from fastapi import FastAPI
from api.triagem import router as triagem_router

app = FastAPI()

app.include_router(triagem_router, prefix="/triagem")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)