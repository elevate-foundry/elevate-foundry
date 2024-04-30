function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    appendMessage("User: " + userInput);
    document.getElementById("user-input").value = "";
    fetch("https://saudade.cloud/send-message", {  // Update the URL to your GitHub Pages URL
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => appendMessage("ChatBot: " + data.response))
    .catch(error => console.error('Error:', error));
}

function appendMessage(message) {
    var chatDisplay = document.getElementById("chat-display");
    chatDisplay.innerHTML += "<div>" + message + "</div>";
}
