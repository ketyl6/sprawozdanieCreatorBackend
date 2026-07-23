from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Sprawozdania AI API")

# 3. Konfiguracja CORS - pozwala frontendowi (np. z portu 3000) pytać ten serwer
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # W produkcji zamienimy na ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    temat_cwiczenia: str
    dane_pomiarowe: str # Np. zawartość tabelki wrzucona jako tekst
    dodatkowe_uwagi: str = "" # Pole opcjonalne

@app.get("/")
def health_check():
    return {"status": "Serwer działa, silniki odpalone!"}

@app.post("/generate-conclusion")
def generate_conclusion(data: StudentData):
    print(f"Otrzymano temat do analizy: {data.temat_cwiczenia}")
    
    return {
        "message": "Odebrano dane pomyślnie",
        "temat": data.temat_cwiczenia,
        "ai_wnioski": "Tutaj wkrótce pojawi się tekst wygenerowany przez AI na podstawie pomiarów..."
    }