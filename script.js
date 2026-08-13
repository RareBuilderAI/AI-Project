async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;

    if (message.trim() === "") {
        return;
    }

    chatBox.innerHTML += `
        <p><strong>You:</strong> ${message}</p>
    `;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <p><strong>RobotChat:</strong> ${data.response}</p>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}