from flask_socketio import emit

from app import socketio


@socketio.on("connect")
def connect():
    print("New connection")
    emit("connect", "ok")
