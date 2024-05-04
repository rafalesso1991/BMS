from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import Base, engine
from router.auth_route import auth_router
from router.book_route import book_router
from router.user_route import user_router
import uvicorn

# CREATE TABLES if they dont exists
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

# APP
app = FastAPI(
        title="BMS - Book Managment System",
        description="Alumno: Rafael Alesso - 2024",
        version="1.0.0",
        debug=True
)

# ORIGINS
origins = [
    "http://localhost:3000"
]

# MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ROUTES
app.include_router(auth_router)
app.include_router(book_router)
app.include_router(user_router)

# RUN
if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)