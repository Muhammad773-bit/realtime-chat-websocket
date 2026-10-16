// server.js
const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.static(".")); // serve index.html from current folder

const users = {};

io.on("connection", (socket) => {
    // User joins
    socket.on("join", (username) => {
        users[socket.id] = username;
        socket.broadcast.emit("system", `${username} joined the chat`);
    });

    // User sends a message
    socket.on("chat", (msg) => {
        const user = users[socket.id];
        io.emit("chat", { user, msg });
    });

    // User disconnects
    socket.on("disconnect", () => {
        const user = users[socket.id];
        if (user) {
            socket.broadcast.emit("system", `${user} left the chat`);
            delete users[socket.id];
        }
    });
});

server.listen(3000, () => console.log("Server running on http://localhost:3000"));
