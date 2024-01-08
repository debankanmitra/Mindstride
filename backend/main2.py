from sse_starlette.sse import EventSourceResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import asyncio

app = FastAPI()
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
async def generate_event():
    while True:
        # Generate an event with current timestamp
        data = {"name": "John Doe"}
        # Format the event data for SSE
        event_data = f"data: {data}\n\n"
        yield event_data
        # Wait for a second before sending the next event

@app.get("/check")
async def get_events():
    return EventSourceResponse(generate_event())

