from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()


# Model za ulazne podatke
class Broj(BaseModel):
    broj: int


@app.get("/")
async def home():
    return {"poruka": "API za izračun faktora broja!"}


@app.post("/izracunaj/")
async def izracunaj(broj: Broj):
    n = broj.broj
    if n < 0 or n > 1000:
        raise HTTPException(status_code=400, detail="Broj mora biti između 0 i 1000.")

    rezultat = math.factorial(n)
    return {"broj": n, "faktorijal": rezultat}
