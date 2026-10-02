from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    nombre = "Usuario"  # <--- Define la variable aquí
    return f"<h1>Bienvenido al portal universitario, {nombre}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    # Hotfix completado