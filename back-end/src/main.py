from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.db import Base, engine
from router.auth_router import auth_router
#from router.book_router import book_router
from router.user_router import user_router
# Create Tables if dont exists
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()
# Create App
app = FastAPI(
        title="BMS - Book Managment System",
        description="Alumno: Rafael Alesso - 2024",
        version="1.0.0"
)
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# App Routes
app.include_router(auth_router)
#app.include_router(book_router)
app.include_router(user_router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)