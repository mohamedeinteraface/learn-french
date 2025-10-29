from flask import Flask, render_template

app = Flask(__name__)

# ===== Page d'accueil =====
@app.route("/")
def index():
    return render_template("index.html")

# ===== Lettres A-Z =====
@app.route("/letters")
def letters():
    letters_data = []
    for i in range(ord('A'), ord('Z') + 1):  # de A à Z
        char = chr(i)
        letters_data.append({
            "char": char,
            "image": f"{char.lower()}.png",
            "sound": f"{char.lower()}.mp3"
        })
    return render_template("letters.html", letters=letters_data)

# ===== Chiffres 1-99 =====
@app.route("/numbers")
def numbers():
    numbers_data = []
    for i in range(1, 100):  # de 1 à 99
        numbers_data.append({
            "num": str(i),
            "image": f"{i}.png",
            "sound": f"{i}.mp3"
        })
    return render_template("numbers.html", numbers=numbers_data)

if __name__ == "__main__":
    app.run(debug=True)
