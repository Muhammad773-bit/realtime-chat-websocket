# Realtime Chat Websocket

Two real-time chat apps: one with Python and FastAPI WebSockets, one with Node.js and Socket.IO.

**Tech:** Python, FastAPI WebSockets, Node.js, Socket.IO

## What's inside

- `chat-app/`: FastAPI WebSocket chat (Python)
- `Chatting-App/`: Socket.IO chat (Node.js)

## Run it

```bash
# Python
cd chat-app && pip install -r requirements.txt && uvicorn main:app --reload
# Node
cd Chatting-App && npm install socket.io express && node server.js
```

API keys are read from environment variables. Copy `.env.example` to `.env` and fill in your own keys.

---
By [Muhammad Ali](https://muhammad773-bit.github.io), BS Artificial Intelligence, SMIU Karachi.
