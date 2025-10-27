from ping3 import ping
from datetime import datetime
import json
import os
import requests
from modules import html_report
from modules.manager import laad_server

def run_checks():
    servers = laad_server()
    if not servers:
        print("Geen servers gevonden in servers.json.")
        return

    nieuwe_resultaten = []
    print("\nServerstatus:")

    for server in servers:
        naam = server.get("naam", "onbekend")
        adres = server.get("adres", "onbekend")
        type_ = server.get("type", "onbekend").strip().lower()
        tijdstip = datetime.now().isoformat()

        # SERVER: ping uitvoeren
        if type_ == "server":
            resultaat = ping(adres, timeout=2)
            status = "OK" if resultaat is not None else "NOT OK"
            print(f"- {naam} ({adres}) [server]: {status} om {tijdstip}")

        # WEBSITE: HTTP-status ophalen
        elif type_ == "website":
            try:
                response = requests.get(f"http://{adres}", timeout=5)
                code = response.status_code

                # Vertaal statuscode naar betekenis
                if 200 <= code < 300:
                    status = f"{code} OK"
                elif 300 <= code < 400:
                    status = f"{code} Redirect"
                elif code == 404:
                    status = "404 Niet gevonden"
                elif 500 <= code < 600:
                    status = f"{code} Serverfout"
                else:
                    status = f"{code} Onbekende status"

                print(f"- {naam} ({adres}) [website]: {status} om {tijdstip}")

            except requests.exceptions.RequestException as e:
                status = f"Website fout: {str(e)}"
                print(f"- {naam} ({adres}) [website]: {status} om {tijdstip}")

        # ONBEKEND TYPE
        else:
            status = f"Onbekend type: {type_}"
            print(f"- {naam} ({adres}) [onbekend]: {status} om {tijdstip}")

        # Voeg resultaat toe aan log
        nieuwe_resultaten.append({
            "naam": naam,
            "adres": adres,
            "type": type_,
            "status": status,
            "tijdstip": tijdstip
        })

    # Voeg toe aan bestaande logs
    alle_resultaten = []
    if os.path.exists("logs.json"):
        with open("logs.json") as f:
            try:
                alle_resultaten = json.load(f)
            except json.JSONDecodeError:
                alle_resultaten = []

    alle_resultaten.extend(nieuwe_resultaten)

    with open("logs.json", "w") as f:
        json.dump(alle_resultaten, f, indent=2)

    html_report.generate_html(alle_resultaten)