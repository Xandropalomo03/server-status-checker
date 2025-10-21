from ping3 import ping, EXCEPTIONS
from datetime import datetime
import json
import os
from modules.html_report import generate_html

# Voert serverchecks uit en genereert een HTML-rapport
def run_checks():
    # Probeer de lijst van servers in te laden uit servers.json
    try:
        with open("servers.json") as f:
            servers = json.load(f)
    except FileNotFoundError:
        print("een servers gevonden in servers.json.")
        return

    # Lijst om nieuwe checkresultaten op te slaan
    nieuwe_resultaten = []

    # Toon statusinformatie in de terminal
    print("\nServerstatus:")
    for server in servers:
        naam = server["naam"]
        adres = server["adres"]
        resultaat = ping(adres, timeout=2)  # Voer een ping uit met een timeout van 2 seconden
        status = "OK" if resultaat is not None else "NOT OK"
        tijdstip = datetime.now().isoformat()  # Huidige tijdstip in ISO-formaat

        # Print het resultaat naar de terminal
        print(f"- {naam} ({adres}): {status} om {tijdstip}")

        # Voeg het resultaat toe aan de lijst
        nieuwe_resultaten.append({
            "naam": naam,
            "adres": adres,
            "status": status,
            "tijdstip": tijdstip
        })

    # Probeer bestaande logs in te laden uit logs.json
    alle_resultaten = []
    if os.path.exists("logs.json"):
        with open("logs.json") as f:
            try:
                alle_resultaten = json.load(f)
            except json.JSONDecodeError:
                alle_resultaten = []

    # Voeg de nieuwe resultaten toe aan de bestaande logs
    alle_resultaten.extend(nieuwe_resultaten)

    # Schrijf alle resultaten terug naar logs.json
    with open("logs.json", "w") as f:
        json.dump(alle_resultaten, f, indent=2)

    # Genereer een HTML-rapport op basis van alle resultaten
    generate_html(alle_resultaten)