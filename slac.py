import os
import re
import subprocess
import time
import webbrowser
import vdf
from rich.console import Console
from reg import fetch_reg, registry_magic

console = Console()


def choice(accountnames: list[str], personanames: list[str]) -> str:
    console.print("[underline]Choose your account:[/]")
    for i in range(len(accountnames)):
        console.print(f"{i}: {accountnames[i]} | [yellow]{personanames[i]}[/]")
    while True:
        try:
            c = int(input("Choose a number: "))
            break
        except (KeyError, ValueError, IndexError):
            console.print(
                "[bold red]Invalid input. Please choose a [underline]number from the list[/underline].[/bold red]")
    return accountnames[c]


def process_magic():
    # Find and kill the Steam process
    output = subprocess.run(["tasklist"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    lines = output.split("\n")
    for line in lines:
        if "steam.exe" in line:
            pid = re.search(r"(\d+)", line).group()
            subprocess.run(["taskkill", "/pid", pid, "/f"], stdout=subprocess.DEVNULL)
    # Start a new Steam process using the steam:// protocol
    webbrowser.open("steam://open/console")
    console.print("[green]Process successfully terminated. Steam restarted.[/green]")
    time.sleep(1.5)


def fetch_loginusers():
    """
    Returns the contents of loginusers.vdf as dict
    """

    steam_path = fetch_reg('steampath')
    if '/' in steam_path:
        steam_path = steam_path.replace('/', '\\')

    vdf_file = os.path.join(steam_path, 'config', 'loginusers.vdf')
    try:
        with open(vdf_file, 'r', encoding='utf-8') as vdf_file:
            return vdf.load(vdf_file)
    except FileNotFoundError:
        return {}


def loginusers_accountnames() -> list:
    """
    Returns a list of account names from loginusers.vdf
    """
    loginusers = fetch_loginusers()
    accounts = []
    for user in loginusers['users'].values():
        accounts.append(user['AccountName'])
    return accounts


def loginusers_personanames() -> list:
    """
    Returns a list of personanames from loginusers.vdf
    """
    loginusers = fetch_loginusers()
    personanames = []
    for user in loginusers['users'].values():
        personanames.append(user['PersonaName'])
    return personanames


def main() -> None:
    accountnames = loginusers_accountnames()
    personanames = loginusers_personanames()
    usr_choice = choice(accountnames, personanames)
    registry_magic(usr_choice)
    process_magic()


if __name__ == "__main__":
    main()
