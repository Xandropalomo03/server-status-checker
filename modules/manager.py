# Importeer de json-module om servergegevens op te slaan en te laden
import json

# Slaat de lijst van servers op in het bestand servers.json
def toevoegen_servers(servers):
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=2)

# Laadt de lijst van servers uit servers.json
def laad_server():
    try:
        with open("servers.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Geef een lege lijst terug als het bestand niet bestaat

def interactive_menu():
    while True:
        # Toon beschikbare opties aan de gebruiker
        print("\n[1] Voeg server toe\n[2] Verwijder server\n[3] Toon servers\n[0] Exit")

        # Laad de huidige lijst van servers
        servers = laad_server()

        # Vraag de gebruiker om een keuze te maken
        keuze = input("Keuze: ")

        # Optie 1: Voeg een nieuwe server toe
        if keuze == "1":
            naam = input("Naam: ")           # Vraag om de naam van de server
            adres = input("IP/Hostname: ")   # Vraag om het IP-adres of hostname

            # Vraag om het type en valideer de invoer
            while True:
                type_input = input("Type (website/server): ").strip().lower()
                if type_input in ["website", "server"]:
                    break
                print("Ongeldige invoer. Kies 'website' of 'server'.")
            servers.append({"naam": naam, "adres": adres, "type": type_input} )  # Voeg toe aan de lijst
            toevoegen_servers(servers)       # Sla de bijgewerkte lijst op

        # Optie 2: Verwijder een bestaande server
        elif keuze == "2":
            # Toon alle servers met hun index
            for i, s in enumerate(servers):
                print(f"[{i}] {s['naam']} ({s['adres']}) {s['type']}")
            # Vraag welke server verwijderd moet worden
            idx = int(input("Index om te verwijderen: "))
            servers.pop(idx)                 # Verwijder de gekozen server
            toevoegen_servers(servers)       # Sla de bijgewerkte lijst op

        # Optie 3: Toon alle geregistreerde servers
        elif keuze == "3":
            for server in servers:
                print(f"{server['naam']} - {server['adres']} - {server['type']}")

        # Optie 0: Stop het programma
        elif keuze == "0":
            break

        # Ongeldige invoer
        else:
            print("Geen geldige keuze")