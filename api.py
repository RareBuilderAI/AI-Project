from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "RobotChat API is running"}


@app.post("/chat")
def chat(data: ChatMessage):
    reply = get_response(data.message)

    return {
        "user": data.message,
        "RobotChat": reply
    }