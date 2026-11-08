from flask import Blueprint, request, render_template
from model.modeleCarte import FiltreCriteres, get_communes_by_departement, get_reseaux_by_commune
from flask import Blueprint, jsonify

carte_bp = Blueprint('carte', __name__)
filtres_bp = Blueprint('filtres', __name__)

@filtres_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@filtres_bp.route("/traitement", methods=["POST"])
def traitement():
    criteres = FiltreCriteres(request.form)
    #qqchose ici pour filtrer
    print(criteres) 
    return render_template("index.html", criteres=criteres)




carte_bp = Blueprint('carte', __name__)

@carte_bp.route('/api/communes/<code_dept>')
def get_communes_api(code_dept):
    communes = get_communes_by_departement(code_dept)
    return jsonify(communes)


@carte_bp.route('/api/reseaux/<code_commune>')
def get_reseaux_json(code_commune):
    from model.modeleCarte import get_reseaux_by_commune
    reseaux = get_reseaux_by_commune(code_commune)
    return jsonify(reseaux)


@carte_bp.route('/api/communes/<code_dept>')
def get_communes_json(code_dept):
    import sqlite3
    conn = sqlite3.connect("data/json_tres_potable.db")
    cur = conn.cursor()
    cur.execute("SELECT code_commune, nom_commune FROM communes WHERE code_departement = ?", (code_dept,))
    data = [{"code": row[0], "nom": row[1]} for row in cur.fetchall()]
    conn.close()
    return jsonify(data)

def get_communes_by_departement(code_dept):
    import sqlite3
    conn = sqlite3.connect("data/json_tres_potable.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT code_commune, nom_commune
        FROM communes
        WHERE code_departement = ?
        ORDER BY nom_commune
    """, (code_dept,))
    communes = [{"code": row[0], "nom": row[1]} for row in cur.fetchall()]
    conn.close()
    return communes
