from fastapi import FastAPI
import google.generativeai as genai
import os
import urllib.parse
from fastapi.middleware.cors import CORSMiddleware

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, # Allows CORS from this origin
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World - AI chat"}


@app.get("/ai/{prompt}")
async def gen_response(prompt: str):
    # answer = model.generate_content(urllib.parse.unquote(prompt))
    answer = chat.send_message(urllib.parse.unquote(prompt), stream=False)
    print(answer.text)
    return {"answer": answer.text}