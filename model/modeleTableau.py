import requests


class FiltreColonnes:
    def __init__(self):
        self.tableau = {}

    def _init_tableau(self):
        self.tableau = {
            "Code prelevement": [],
            "Date": [],
            "Installation": [],
            "Réseau": [],
            "Parametre mesuré": [],
            "Résultat": [],
            "Département": [],
            "Commune": [],
            "Conclusion conformité": [] 
        }

    def _ajouter_ligne(self, item):
        self.tableau["Code prelevement"].append(item.get("code_prelevement"))
        self.tableau["Date"].append(item.get("date_prelevement"))
        self.tableau["Installation"].append(item.get("nom_installation_amont"))
        self.tableau["Réseau"].append(
            ", ".join(r.get("nom", "") for r in item.get("reseaux", []))
        )
        self.tableau["Parametre mesuré"].append(item.get("libelle_parametre"))
        resultat = item.get("resultat_alphanumerique")
        if resultat in (None, ""):
            resultat = item.get("resultat_numerique")
        self.tableau["Résultat"].append(resultat)
        self.tableau["Département"].append(item.get("nom_departement"))
        self.tableau["Commune"].append(item.get("nom_commune"))
        self.tableau["Conclusion conformité"].append(item.get("conclusion_conformite_prelevement")) 



    def premiers_par_code_prelevement(self):
        # init le tableau de résultats 
        self._init_tableau()

        # requête à l'API 
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            
            # Paramètres de la requête 
            params={"size": 1000}
        )

        # trie les résultats obtenus par ordre alphabétique),
        # en gérant les valeurs nulles avec `or ""` pour éviter les erreurs
        data = sorted(response.json().get("data", []), key=lambda x: x.get("code_prelevement") or "")

        # Parcourt les 50 premiers résultats triés
        for item in data[:50]:
            # Ajoute chaque résultat au tableau via une méthode interne
            self._ajouter_ligne(item)


    def derniers_par_code_prelevement(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("code_prelevement") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)

    def premiers_par_date(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("date_prelevement") or "")
        for item in data[:50]:
            self._ajouter_ligne(item)

    def derniers_par_date(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("date_prelevement") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)

    def premiers_par_nom_installation(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_installation_amont") or "")
        for item in data[:50]:
            self._ajouter_ligne(item)

    def derniers_par_nom_installation(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_installation_amont") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)

    def premiers_par_parametre(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("libelle_parametre") or "")
        for item in data[:50]:
            self._ajouter_ligne(item)

    def derniers_par_parametre(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("libelle_parametre") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)
    

    def premiers_par_departement(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_departement") or "")
        for item in data[:50]:
            self._ajouter_ligne(item)

    def derniers_par_departement(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_departement") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)

    def premiers_par_commune(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_commune") or "")
        for item in data[:50]:
            self._ajouter_ligne(item)

    def derniers_par_commune(self):
        self._init_tableau()
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis",
            params={"size": 1000}
        )
        data = sorted(response.json().get("data", []), key=lambda x: x.get("nom_commune") or "", reverse=True)
        for item in data[:50]:
            self._ajouter_ligne(item)

    def afficher_tableau(self):
        return self.tableau
