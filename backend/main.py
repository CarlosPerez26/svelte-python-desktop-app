from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/data")
def get_data():
    # This is where your python logic will go
    return {"message": "This is a message from your Python backend!"}

