async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    if (!input || !chatBox) {
        return;
    }

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    chatBox.innerHTML += `
        <p>
            <strong>You:</strong> ${escapeHtml(message)}
        </p>
    `;

    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error(
                "Server response failed."
            );
        }

        const data = await response.json();

        chatBox.innerHTML += `
            <p>
                <strong>RobotChat:</strong>
                ${escapeHtml(data.response)}
            </p>
        `;

    } catch (error) {

        console.error(
            "RobotChat connection error:",
            error
        );

        chatBox.innerHTML += `
            <p>
                <strong>RobotChat:</strong>
                Sorry, I couldn't connect right now.
            </p>
        `;
    }

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


function escapeHtml(value) {

    const div =
        document.createElement("div");

    div.textContent = value;

    return div.innerHTML;
}


document.addEventListener(
    "DOMContentLoaded",
    () => {

        const input =
            document.getElementById(
                "user-input"
            );

        if (!input) {
            return;
        }

        input.addEventListener(
            "keydown",
            (event) => {

                if (
                    event.key === "Enter" &&
                    !event.shiftKey
                ) {

                    event.preventDefault();

                    sendMessage();
                }
            }
        );
    }
);

document.addEventListener(
    "DOMContentLoaded",
    () => {
        const observerOptions = {
            threshold: 0.1
        };

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("visible");
                    }
                });
            },
            observerOptions
        );

        document.querySelectorAll("section").forEach((section) => {
            observer.observe(section);
        });
    }
);
