import click
from modules import manager, checker

@click.group()
def cli():
    pass

@cli.command()
def manage():
    manager.interactive_menu()

@cli.command()
def check():
    checker.run_checks()

if __name__ == '__main__':
    cli()