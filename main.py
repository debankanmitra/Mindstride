from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from mangum import Mangum
from inference.Initialize import Intialize
from inference.Gemini import Query_from_gemini
from inference.Groq import Query_from_groq

# import uvicorn


# co, groq, index defined at the module level to store the initialized objects
co = None
groq = None
index = None


@asynccontextmanager
async def lifespan(app: FastAPI):

    # To modify the same global variables we are using the global keyword
    global co, groq, index

    # Modify the global variables
    co, index, groq = await Intialize()
    print("Initialized", co, index, groq)
    yield
    # Clean up
    print("Cleaned up")


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class UserQuery(BaseModel):
    user: str


@app.post("/groq_inference")
async def get_groq_inference(query: UserQuery):
    response = Query_from_groq(query.user, co, groq, index)
    return {"output": response}


@app.post("/gemini_inference")
async def get_gemini_inference(query: UserQuery):
    # sending modified co, index directly with the user query
    response = Query_from_gemini(query.user, co, index)
    return {"output": response}


# Create the Mangum handler
handler = Mangum(app)

# if __name__ == "__main__":
#     uvicorn.run(app)
