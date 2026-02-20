from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your first web app!", "status": "success"})

@app.route('/api/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name', 'World')
        return jsonify({"message": f"Hello, {name}!"})
    return jsonify({"message": "Hello, World!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)