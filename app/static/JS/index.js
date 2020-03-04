let socket = io();

socket.on("connect", data => {
    if (data === "ok") {
        console.log("Connected !")
    }
});
