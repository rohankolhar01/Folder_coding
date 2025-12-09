from fastapi import FastAPI

app = FastAPI(title="Backend API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI backend!"}