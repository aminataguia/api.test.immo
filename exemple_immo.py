from fastapi import FastAPI, HTTPException, Depends
import sqlite3, uvicorn
from datetime import datetime

app = FastAPI()

database = r"Chinook.db"
con = sqlite3.connect(database)
cur = con.cursor()

# User Story 1
#En tant qu'Agent je veux pouvoir consulter le revenu fiscal moyen des foyers de ma ville (Montpellier)
def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4):
        raise HTTPException(status_code=400, detail="L'année doit être une valeur numérique de 4 chiffres")
    return year

@app.get("/revenu_fiscal_moyen/", 
description = 'Retourne le revenu fiscal moyen de la ville donnée' )
async def revenu_fiscal_moyen(year: str = Depends(validate_year), city: str = ""):
    req = f"SELECT revenu_fiscal_moyen, date, ville FROM foyers_fiscaux WHERE date = {year} AND ville = '{city}'"
    cur.execute(req)
    result = cur.fetchall()
    return result  # Retourne les résultats

# User Story 2
#En tant qu'Agent je veux consulter les 10 dernières transactions dans ma ville (Lyon)
@app.get("/dix_derniere_transaction/",
description='Donne les dernieres transaction dans la ville donnée ')
async def dix_derniere_transaction(city: str):
    query = f"SELECT * FROM transactions_sample WHERE ville LIKE '{city}' ORDER BY date_transaction DESC LIMIT 10;"
    cur.execute(query)
    result = cur.fetchall()
    return result  # Retourne les résultats

# User Story 3
#En tant qu'Agent je souhaite connaitre le nombre d'acquisitions dans ma ville (Paris) durant l'année 2022
@app.get("/transaction_ville_par_ans/",
description='Donne le nombre d\'acquisitions dans la ville donnée avec l\'année donnée')
async def transaction_ville_par_ans(year: str = Depends(validate_year), city: str = ""):
    start_date = f"{year}-01-01"
    end_date = f"{str(int(year) + 1)}-01-01"
    req = f"SELECT * FROM transactions_sample WHERE date_transaction >= '{start_date}' AND date_transaction < '{end_date}' AND ville = '{city}';"
    cur.execute(req)
    result = cur.fetchone()
    return result  # Retourne les résultats

#User story 4
#En tant qu'Agent je souhaite connaitre le nombre d'acquisitions dans ma ville (Paris) durant l'année 2022
@app.get("/prix_moyen_par_maison/",
description = 'Donne le prix au mètre carrer dans les maisons vendus dans l\'année saisie')
async def prix_moyen_par_maison(year: int):
    cur = con.cursor()
    res = cur.execute(f"SELECT AVG(prix/surface_habitable) FROM transactions_sample WHERE type_batiment LIKE 'Maison' AND strftime('%Y', date_transaction) = '{year}'")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result
       
#User story 5
#En tant qu'Agent je souhaite connaitre le prix au m2 moyen pour les maisons vendues l'année 2022
@app.get("/prix_moyen_m2/",
description='Donne le nombre d\'acquisitions de studios dans la ville souhaité et egalement l\'année saisie')
async def prix_moyen_m2(city: str, year:int):
    cur = con.cursor()
    res = cur.execute(f"SELECT AVG(prix / surface_habitable) AS prix_moyen_m2 FROM transactions_sample WHERE type_batiment = 'Maison' AND ville = '{city}' AND date_transaction LIKE '{year}%'")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result

#User story 6 
#En tant qu'Agent je souhaite connaitre le nombre d'acquisitions de studios dans ma ville (Rennes) durant l'année 2022
@app.get("/nb_acquisitions_studio/",
description='Donne la repartition des appartements vendus dans la ville souhaiter dans l\'année souhaité')
async def nombre_acquisitions_studio(year: int, departement: int):
    cur = con.cursor()
    start_date = f"{year}-01-01"
    end_date = f"{year + 1}-01-01"
    res = cur.execute(f"SELECT COUNT(id_transaction) FROM transactions_sample WHERE n_pieces = '1' AND date_transaction BETWEEN '{start_date}' AND '{end_date}' AND departement = '{departement}'")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result
#J'ai préférer mettre departement plus de chance de tomber sur des valeurs ( essayez year = 2021 et departement = 34)

#User story 7
#En tant qu'Agent je souhaite connaitre la répartition des appartements vendus (à Marseille) durant l'année 2022 en fonction du nombre de pièces
@app.get("/repartition_appart/",
description='Donne le prix au m^2 moyen dans l\'année souhaité dans le departement souhaité' )
async def repartition_appartement(year: int,departement: int):
    cur = con.cursor()
    res = cur.execute(f"SELECT COUNT(id_transaction) FROM transactions_sample WHERE type_batiment = 'Appartement' AND date_transaction LIKE '{year}%' AND departement = '{departement}';")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result
    
#User story 8
#En tant qu'Agent je souhaite connaitre le prix au m2 moyen pour les maisons vendues à Avignon l'année 2022                                                                                                                                                                                                        
@app.get("/prix_moyen_m2_par_maison/",
description='donne le nombre de transaction dans le departement voulu et ordonné par ordre décroissant')
async def prix_moyen_m2_par_maison(city: str, year:int):
    cur = con.cursor()
    res = cur.execute(f"SELECT AVG(prix / surface_habitable) AS prix_moyen_m2 FROM transactions_sample WHERE type_batiment = 'Maison' AND ville = '{city}' AND date_transaction LIKE '{year}%'")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result
    
#User story 9
#En tant que CEO, je veux consulter le nombre de transactions (tout type confondu) par département, ordonnées par ordre décroissant   
@app.get("/transaction_par_departement",
description='Donne le nombre total de ventes d\'appartement dans la ville souhaité ou le foyer fiscal est superieur à 70k')
async def transaction_par_departement(departement: int):
    cur = con.cursor()
    res = cur.execute(f"SELECT departement, COUNT(*) AS nombre_transactions FROM transactions_sample WHERE departement = '{departement}' GROUP BY departement ORDER BY nombre_transactions DESC")
    result = res.fetchone()
    if result is None:
        return "PAS DE RESULTAT"
    else:
        return result
    
    
#User story 11
#En tant que CEO, je veux consulter le top 10 des villes les plus dynamiques en termes de transactions immobilières
@app.get("/top_10_des_villes_avec_le_plus_de_transaction_immobiliere",
description='Donne le top 10 des villes les plus dynamique en terme de transaction immobiliere')
async def top_10_des_villes_avec_le_plus_de_transaction_immobiliere():
    cur = con.cursor()
    req = f"SELECT ville, COUNT(id_transaction) AS nombre_transactions FROM transactions_sample GROUP BY ville ORDER BY nombre_transactions DESC LIMIT 10;"
    cur.execute(req)
    result = cur.fetchall()
    if not result:
        return "PAS DE RESULTAT"
    else:
        return result
    
    


# Exécute l'application avec uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)