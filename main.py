from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.job import job_router
from domain.answer import answer_router
from domain.member import member_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://15.164.125.175",
    "https://jobstay.co.kr",
    "https://www.jobstay.co.kr",
    "https://jobstay.co.kr",
    "https://www.jobstay.co.kr"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job_router.router)
app.include_router(answer_router.router)
app.include_router(member_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))
app.mount("/static", StaticFiles(directory="frontend/public/static"), name="static")
@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")