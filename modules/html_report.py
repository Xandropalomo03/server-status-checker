def generate_html(resultaten):
    # Probeer de HTML-template in te laden vanuit de templates-map
    try:
        with open("templates/report_template.html") as f:
            template = f.read()
    except FileNotFoundError:
        print("HTML template niet gevonden.")
        return  # Stop als het templatebestand ontbreekt

    # Bouw de HTML-rijen op basis van de resultaten
    rows = ""
    for r in resultaten:
        # Bepaal de CSS-klasse op basis van de status
        kleur_klasse = "ok" if r["status"] == "OK" else "not-ok"
        # Voeg een tabelrij toe met servergegevens en status
        rows += f"<tr><td>{r['naam']}</td><td>{r['adres']}</td><td class='{kleur_klasse}'>{r['status']}</td><td>{r['tijdstip']}</td></tr>\n"

    # Vervang de placeholder in het template door de gegenereerde rijen
    html = template.replace("{{ROWS}}", rows)

    # Schrijf het volledige HTML-rapport weg naar rapport.html
    with open("rapport.html", "w") as f:
        f.write(html)

    # Bevestiging in de terminal dat het rapport is gegenereerd
    print("HTML-rapport gegenereerd: rapport.html")