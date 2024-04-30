from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])  # Specify methods=['POST'] to allow POST requests
def send_message():
    if request.method == 'POST':
        data = request.get_json()
        message = data['message']
        # Create a JSON response containing the received message
        response = {'response': f'Message received: {message}'}
        return jsonify(response)
    else:
        # Return a 405 error response if a non-POST request is received
        return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
