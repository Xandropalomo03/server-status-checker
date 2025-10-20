# Importeer benodigde modules
import sys
from modules import manager, checker

# Startpunt van de applicatie
def main():
    # Controleer of er een command-line argument is meegegeven
    if len(sys.argv) < 2:
        print("Gebruik: python main.py [manage|check]")
        return  # Stop het programma als er geen modus is opgegeven

    # Lees de gekozen modus uit het eerste argument
    mode = sys.argv[1]

    # Management modus: servers toevoegen, verwijderen of bekijken
    if mode == 'manage':
        manager.interactive_menu()  # Start het interactieve menu uit manager.py

    # Check modus: voer ping-checks uit en genereer rapport
    elif mode == 'check':
        checker.run_checks()  # Start de checkroutine uit checker.py

    # Ongeldige modus opgegeven
    else:
        print("Geen geldige mode. Gebruik 'manage' of 'check'.")

# Voer de main-functie uit als dit script direct wordt gestart
main()