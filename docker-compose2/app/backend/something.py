from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, template_folder=os.path.join("..", "frontend", "templates")
)

@app.route("/")
def index():
    return render_template("something.html")

#tirar a rota aqui do python (que serve o html)

@app.route("/api")
def mensagem():
    return jsonify({"mensagem": "Olá, esta mensagem veio do backend!"})

if __name__ == "__main__":
    app.run(debug=True)
