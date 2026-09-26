from fastapi import FastAPI

app = FastAPI(title="Intermatch ML Service")

@app.get("/")
def root():
    return {"status": "ok"}
