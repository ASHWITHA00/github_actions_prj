from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

def add(a, b):
    """A simple function to add two numbers."""
    return a + b

@app.route('/')
def home():
    """Home route."""
    return "Hello, World! This is a simple Flask app."

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    """Route to add two numbers."""
    result = add(a, b)
    return jsonify({"result": result})

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to be accessible inside a Docker container
    app.run(host='0.0.0.0', port=5000)
