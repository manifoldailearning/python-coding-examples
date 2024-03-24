from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
def welcome():
    return "welcome to fastapi code"

@app.get("/hello") 
def hello():
    return "hello from fastapi code"

@app.post("/response") 
def myresponse():
    return "This is the response from post method"

#uvicorn fast-api:app --reload