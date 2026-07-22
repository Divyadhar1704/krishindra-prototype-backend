from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot.engine import ChatbotEngine

app = FastAPI()

# Allow Flutter Web to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # For prototype
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ChatbotEngine()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Krishindra Prototype API"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = engine.get_response(request.question)

    reply = (
        reply.replace("<br>", "\n")
             .replace("<br/>", "\n")
             .replace("<br />", "\n")
    )
    return {"response": reply}