from flask import Blueprint, request, render_template

from model.modeleTableau import FiltreColonnes, HubEauIndisponible


tableau_bp = Blueprint("tableau", __name__)
TRIS = {
    "1": ("code_prelevement", False),
    "2": ("code_prelevement", True),
    "3": ("date_prelevement", False),
    "4": ("date_prelevement", True),
    "5": ("nom_installation_amont", False),
    "6": ("nom_installation_amont", True),
    "7": ("libelle_parametre", False),
    "8": ("libelle_parametre", True),
    "9": ("nom_departement", False),
    "10": ("nom_departement", True),
    "11": ("nom_commune", False),
    "12": ("nom_commune", True),
}


@tableau_bp.get("/tableau")
def afficher_tableau():
    tri = request.args.get("tri", "1")
    if tri not in TRIS:
        tri = "1"

    filtre = FiltreColonnes()
    try:
        filtre.trier(*TRIS[tri])
    except HubEauIndisponible:
        return render_template("tableau.html", tri=tri, indisponible=True), 503

    return render_template("tableau.html", tri=tri, tableau=filtre.afficher_tableau())
