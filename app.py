from flask import Flask, request, jsonify, render_template
from my_llm import generate_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            return jsonify({"response": " Please enter a prompt!"})

        output = generate_text(prompt)

        return jsonify({"response": output})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)