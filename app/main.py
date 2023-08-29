from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import employee, client
#, contract, history

app = FastAPI()

# Middleware
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(employee.router)
app.include_router(client.router)
# app.include_router(contract.router)
# app.include_router(history.router)