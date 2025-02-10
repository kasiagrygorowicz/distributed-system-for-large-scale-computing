from fastapi import FastAPI
import asyncio
import uvicorn
import logging

from dtos.WorkerNode import WorkerNode
from schemas.Primary import Primary

app = FastAPI()
primary = Primary()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Background task for the master node
async def background_task():
    while True:
        logging.info("Master is performing other tasks...")
        await asyncio.sleep(5)  # Simulate some work

# REST endpoint for worker registration
@app.post("/register-worker")
async def register_worker(worker: WorkerNode):
    logging.debug(f"Received registration request from {worker.hostname}")
    primary.add_worker(worker.id, worker.hostname)
    logger.info(f"Registered workers: {primary.nodes}")
    return {"status": "success"}

# Start the background task when the application starts
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_task())

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080)