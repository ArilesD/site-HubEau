import requests


URL_RESULTATS = "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis"
TAILLE_ECHANTILLON = 1000
LIMITE_AFFICHAGE = 50


class HubEauIndisponible(Exception):
    """L’API ne fournit pas de résultats exploitables."""


class FiltreColonnes:
    def __init__(self):
        self.tableau = {
            "Code prélèvement": [],
            "Date": [],
            "Installation": [],
            "Réseau": [],
            "Paramètre mesuré": [],
            "Résultat": [],
            "Département": [],
            "Commune": [],
            "Conclusion du prélèvement": [],
        }

    def trier(self, champ, decroissant=False):
        try:
            response = requests.get(
                URL_RESULTATS,
                params={"size": TAILLE_ECHANTILLON},
                timeout=(3.05, 8),
            )
            response.raise_for_status()
            contenu = response.json()
        except requests.exceptions.RequestException as erreur:
            raise HubEauIndisponible from erreur

        resultats = contenu.get("data") if isinstance(contenu, dict) else None
        if not isinstance(resultats, list) or any(not isinstance(item, dict) for item in resultats):
            raise HubEauIndisponible

        lignes = sorted(resultats, key=lambda item: str(item.get(champ) or ""), reverse=decroissant)
        for item in lignes[:LIMITE_AFFICHAGE]:
            self._ajouter_ligne(item)

    def _ajouter_ligne(self, item):
        self.tableau["Code prélèvement"].append(item.get("code_prelevement"))
        self.tableau["Date"].append(item.get("date_prelevement"))
        self.tableau["Installation"].append(item.get("nom_installation_amont"))
        reseaux = item.get("reseaux")
        noms_reseaux = []
        if isinstance(reseaux, list):
            noms_reseaux = [
                reseau["nom"] for reseau in reseaux
                if isinstance(reseau, dict) and isinstance(reseau.get("nom"), str) and reseau["nom"]
            ]
        self.tableau["Réseau"].append(", ".join(noms_reseaux))
        self.tableau["Paramètre mesuré"].append(item.get("libelle_parametre"))

        resultat = item.get("resultat_alphanumerique")
        if resultat in (None, ""):
            resultat = item.get("resultat_numerique")
        unite_brute = item.get("libelle_unite")
        unite = unite_brute.strip() if isinstance(unite_brute, str) else ""
        if resultat is not None and unite and unite.casefold() != "sans objet":
            resultat = f"{resultat} {unite}"
        self.tableau["Résultat"].append(resultat)

        self.tableau["Département"].append(item.get("nom_departement"))
        self.tableau["Commune"].append(item.get("nom_commune"))
        self.tableau["Conclusion du prélèvement"].append(item.get("conclusion_conformite_prelevement"))

    def afficher_tableau(self):
        return self.tableau
