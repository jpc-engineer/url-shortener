from fastapi import FastAPI, HTTPException, Request, status
from contextlib import asynccontextmanager
from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import declarative_base, sessionmaker

from models import URLRequest

DATABASE_URL = "sqlite:///./urls.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"
    short_code = Column(String, primary_key=True, index=True)
    long_url = Column(String, unique=True, nullable=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting up.. Connecting to SQLite.")

    Base.metadata.create_all(bind=engine)

    yield

    print("Server is shutting down... Disposing database engine.")
    engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.post("/shorten", status_code=status.HTTP_201_CREATED)
async def create_short_url(payload: URLRequest):
    return {"message": "URL received successfully", "target_url": payload.url}