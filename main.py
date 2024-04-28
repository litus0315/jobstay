from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from domain.job import job_router
from domain.answer import answer_router
from domain.member import member_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
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


