# Hub’Eau - Exploration des données sur l’eau potable

Projet universitaire réalisé en équipe. Cette application Flask propose deux parcours pour explorer les données publiques sur l’eau potable en France.

- **Carte** - Sélectionner un département, afficher ses communes puis consulter les réseaux d’eau associés. Cette vue s’appuie sur une base SQLite locale.
- **Tableau** - Consulter les résultats d’analyses de l’[API Hub’Eau](https://hubeau.eaufrance.fr/page/api-qualite-eau-potable) et trier les lignes par date, lieu ou paramètre. Le tri porte sur les enregistrements récupérés par l’application. Cette vue nécessite une connexion Internet.

## Démarrer en local

Avec Python 3.12, crée puis active un environnement virtuel depuis la racine du dépôt.

```bash
python -m venv .venv
```

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS ou Linux
source .venv/bin/activate
```

Installe les dépendances, prépare les fichiers nécessaires et lance Flask.

```bash
python -m pip install -r requirements.txt
python prepare_data.py
python -m flask --app app run
```

Ouvre [http://127.0.0.1:5000](http://127.0.0.1:5000). La commande de préparation récupère la base locale et le logo depuis `site-HubEau.zip`, qui contient l’état d’origine du projet.

## Lire le code

| Fichier ou dossier | Rôle |
| --- | --- |
| `app.py` | Point d’entrée Flask. |
| `controller/` | Routes de la carte et du tableau. |
| `model/` | Requêtes SQLite et récupération des analyses Hub’Eau. |
| `templates/` et `static/` | Pages HTML et styles. |
