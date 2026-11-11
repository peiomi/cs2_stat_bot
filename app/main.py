from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CS2 bot API"}