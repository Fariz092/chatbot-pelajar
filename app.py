from flask import Flask, request, render_template
import random

app = Flask(__name__)

# List jawaban chatbot (ABC: random, sopan, lucu)
responses = [
    "Halo! Apa yang bisa aku bantu?",
    "Tetap semangat belajar ya!",
    "Wah keren pertanyaannya!",
    "Hahaha itu lucu juga!",
    "Jangan menyerah, kamu pasti bisa!",
    "Oke, aku bantu jawab sebisa mungkin!",
    "Kamu luar biasa, teruskan!",
    "Sip, semangat ya!",
    "Belajar itu kunci sukses!",
    "Mau tanya apa lagi nih?"
]

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = random.choice(responses)
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
