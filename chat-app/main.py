from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

clients = {}

@app.get("/")
async def get():
    return HTMLResponse(open("index.html").read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    username = await websocket.receive_text()
    clients[websocket] = username

    join_message = f"🟢 {username} joined the chat"
    await broadcast(join_message)

    try:
        while True:
            message = await websocket.receive_text()
            time = datetime.now().strftime("%H:%M")

            full_message = f"[{time}] {username}: {message}"
            await broadcast(full_message)

    except WebSocketDisconnect:
        clients.pop(websocket)
        leave_message = f"🔴 {username} left the chat"
        await broadcast(leave_message)


async def broadcast(message: str):
    for client in clients:
        await client.send_text(message)
