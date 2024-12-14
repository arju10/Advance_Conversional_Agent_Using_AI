from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# API Route for Query Handling
@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query', '')
    # Placeholder for response logic
    response = {"response": f"You said: {user_query}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
