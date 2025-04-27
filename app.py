from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Selamat datang di Chatbot Pelajar!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pesan = data.get('pesan', '')
    jawaban = f"Kamu mengirim: {pesan}"
    return jsonify({"jawaban": jawaban})

if __name__ == '__main__':
    app.run()
