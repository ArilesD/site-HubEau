from flask import Flask, redirect, render_template
from controller.controlCarte import filtres_bp , carte_bp
from controller.controlTableau import tableau_bp

app = Flask(__name__)

#Routes Flask 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/carte")
def carte():
    return render_template("carte_de_france.html")

@app.route("/documentation")
def documentation():
    return redirect("https://hubeau.eaufrance.fr/page/api-qualite-eau-potable")


# blueprints pour réutiliser routes
app.register_blueprint(filtres_bp)
app.register_blueprint(tableau_bp)
app.register_blueprint(carte_bp)

if __name__ == "__main__":
    app.run(debug=True)




