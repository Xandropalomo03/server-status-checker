# Genereert een HTML-rapport op basis van serverresultaten
def generate_html(resultaten):
    # Probeer de HTML-template in te laden vanuit de templates-map
    try:
        with open("templates/report_template.html") as f:
            template = f.read()  # Lees de volledige inhoud van het templatebestand
    except FileNotFoundError:
        print("HTML template niet gevonden.")  # Meld als het templatebestand ontbreekt
        return  # Stop de functie als er geen template is

    # Bouw dynamische HTML-rijen op basis van de resultaten
    rows = ""
    for r in resultaten:
        # Bepaal de visuele statuskleur met Bootstrap-klassen
        kleur_klasse = "text-success" if r["status"] == "OK" or r["status"] == "200 OK" else "text-danger"
        
        # Voeg een tabelrij toe met servergegevens en status
        rows += (
            f"<tr>"
            f"<td>{r['naam']}</td>"
            f"<td>{r['adres']}</td>"
            f"<td class='{kleur_klasse}'>{r['status']}</td>"
            f"<td>{r['tijdstip']}</td>"
            f"</tr>\n"
        )

    # Vervang de placeholder {{ROWS}} in het template door de gegenereerde rijen
    html = template.replace("{{ROWS}}", rows)

    # Schrijf het volledige HTML-rapport weg naar report.html
    with open("report.html", "w") as f:
        f.write(html)  # Sla het gegenereerde HTML-bestand op