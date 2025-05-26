from fastapi import FastAPI, Request
from pydantic import BaseModel
from tutor_agent import classify_and_delegate

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_agent(req: QueryRequest):
    response = classify_and_delegate(req.question)
    return {"response": response}
