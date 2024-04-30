from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    return jsonify({'response': f'Message received: {message}'})

if __name__ == '__main__':
    app.run(debug=True)
