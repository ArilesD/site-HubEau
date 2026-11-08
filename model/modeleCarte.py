import sqlite3

class FiltreCriteres:
    def __init__(self, data):
        self.qualite_eau = 'qualite_eau' in data
        self.zones_sensibles = 'zones_sensibles' in data
        self.nappes_phreatiques = 'nappes_phreatiques' in data
        self.pollution = 'pollution' in data

    def __repr__(self):
        return (f"<FiltreCriteres(qualite_eau={self.qualite_eau}, "
                f"zones_sensibles={self.zones_sensibles}, "
                f"nappes_phreatiques={self.nappes_phreatiques}, "
                f"pollution={self.pollution})>")


def get_communes_by_departement(code_dept):
    conn = sqlite3.connect("data/json_tres_potable.db")  # adapte si déplacé
    cur = conn.cursor()
    cur.execute("""
        SELECT nom_commune
        FROM communes
        WHERE code_departement = ?
        ORDER BY nom_commune
    """, (code_dept,))
    communes = [row[0] for row in cur.fetchall()]
    conn.close()
    return communes

import sqlite3

def get_reseaux_by_commune(code_commune):
    import sqlite3
    conn = sqlite3.connect("data/json_tres_potable.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT r.nom_reseau
        FROM communes_reseau cr
        JOIN reseau_udi r ON cr.code_reseau = r.code_reseau
        WHERE cr.code_commune = ?
    """, (code_commune,))
    result = [row[0] for row in cur.fetchall()]
    conn.close()
    return result



