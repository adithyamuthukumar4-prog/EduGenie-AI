from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


load_dotenv()


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory="templates"
)


# --------------------------------------------------
# Request Models
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=30000
    )


# --------------------------------------------------
# Frontend
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie"
    }


# --------------------------------------------------
# Q&A
# --------------------------------------------------

@app.post("/qa")
async def qa(payload: QuestionRequest):

    result = answer_question(
        payload.question
    )

    return {
        "result": result
    }


# --------------------------------------------------
# Explanation
# --------------------------------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    result = explain_topic(
        payload.text
    )

    return {
        "result": result
    }


# --------------------------------------------------
# Quiz
# --------------------------------------------------

@app.post("/quiz")
async def quiz(payload: TextRequest):

    result = generate_quiz(
        payload.text
    )

    return {
        "result": result
    }


# --------------------------------------------------
# Summary
# --------------------------------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    result = summarize_text(
        payload.text
    )

    return {
        "result": result
    }


# --------------------------------------------------
# Learning Path
# --------------------------------------------------

@app.post("/learn/recommendations")
async def recommendations(payload: TextRequest):

    result = get_learning_recommendations(
        payload.text
    )

    return {
        "result": result
    }