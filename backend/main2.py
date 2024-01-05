from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI
import asyncio

app = FastAPI()

async def generate_event():
    while True:
        # Generate an event with current timestamp
        data = {"name": "John Doe"}
        # Format the event data for SSE
        event_data = f"data: {data}\n\n"
        yield event_data
        # Wait for a second before sending the next event
        await asyncio.sleep(1)

@app.get("/events")
async def get_events():
    return EventSourceResponse(generate_event())

