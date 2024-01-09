# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

#User story 1 : En tant qu'Agent je veux pouvoir consulter le revenu fiscal moyen des foyers de ma ville (Montpellier)
# @app.get("/revenu_fiscal_moyen/")
# async def read_item(year: int, city: str):
#     return f"SELECT revenu_fiscal_moyen, date, ville FROM foyers_fiscaux WHERE date = {year} AND ville = {city}"

#User story 2 : En tant qu'Agent je veux consulter les 10 dernières transactions dans ma ville (Lyon)

from fastapi import FastAPI

app = FastAPI()

@app.get("/Derniere_transaction/")
async def read_item(year: int, city: str):
    query = f"SELECT * FROM transactions_sample WHERE ville LIKE '{city}' ORDER BY date_transaction DESC LIMIT 10;"
    return query

if __name__ == "__main__":
    import uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
