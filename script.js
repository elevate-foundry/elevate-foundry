function sendMessage() {
    var message = prompt("Enter your message:");
    if (message !== null && message !== "") {
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({message: message})
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').innerText = data.response;
        })
        .catch(error => console.error('Error:', error));
    }
}
