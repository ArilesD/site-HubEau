from flask import Blueprint, request, render_template
from model.modeleTableau import FiltreColonnes

tableau_bp = Blueprint('tableau', __name__)

@tableau_bp.route("/tableau", methods=["GET"])
def afficher_tableau():
    tri = request.args.get("tri", default="1", type=str)

    filtre = FiltreColonnes()

    if tri == "1":
        filtre.premiers_par_code_prelevement()
    elif tri == "2":
        filtre.derniers_par_code_prelevement()
    elif tri == "3":
        filtre.premiers_par_date()
    elif tri == "4":
        filtre.derniers_par_date()
    elif tri == "5":
        filtre.premiers_par_nom_installation()
    elif tri == "6":
        filtre.derniers_par_nom_installation()
    elif tri == "7":
        filtre.premiers_par_parametre()
    elif tri == "8":
        filtre.derniers_par_parametre()
    elif tri == "9":
        filtre.premiers_par_departement()
    elif tri == "10":
        filtre.derniers_par_departement()
    elif tri == "11":
        filtre.premiers_par_commune()
    elif tri == "12":
        filtre.derniers_par_commune()
    else:
        filtre.premiers_par_code_prelevement()  # tri par défaut

    tableau = filtre.afficher_tableau()
    return render_template("tableau.html", tableau=tableau)
