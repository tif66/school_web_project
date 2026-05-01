from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# קריאת מאגר הבדיחות
def load_jokes():
    with open("jokes.json", "r", encoding="utf-8") as f:
        return json.load(f)

# שמירת בדיחות
def save_jokes(jokes):
    with open("jokes.json", "w", encoding="utf-8") as f:
        json.dump(jokes, f, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jokes")
def jokes_page():
    return render_template("jokes.html")

@app.route("/add-joke")
def add_joke_page():
    return render_template("add-joke.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

# API – כל הבדיחות
@app.route("/api/jokes")
def get_jokes():
    return jsonify(load_jokes())

# API – בדיחה אקראית
@app.route("/api/jokes/random")
def random_joke():
    jokes = load_jokes()
    import random
    return jsonify({"joke": random.choice(jokes)})

# API – הוספת בדיחה
@app.route("/api/jokes", methods=["POST"])
def add_joke():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"success": False, "message": "לא ניתן להכניס בדיחה ריקה"}), 400

    jokes = load_jokes()
    jokes.append(text)
    save_jokes(jokes)

    return jsonify({"success": True, "message": "הבדיחה נוספה בהצלחה!"})

if __name__ == "__main__":
    app.run(debug=True)