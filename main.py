from models import (
    create_player,
    get_player,
    list_players,
    update_player,
    delete_player,
)
from db import init_db

MENU = """
1. Create player
2. List players
3. View player
4. Update player
5. Delete player
0. Quit
"""

def prompt_int(prompt, default=None):
    while True:
        s = input(f"{prompt}{' ['+str(default)+']' if default is not None else ''}: ")
        if not s and default is not None:
            return default
        try:
            return int(s)
        except ValueError:
            print("Please enter a number.")

def do_create():
    name = input("Name: ").strip()
    level = prompt_int("Level", 1)
    score = prompt_int("Score", 0)
    pid = create_player(name, level, score)
    print(f"Created player with id {pid}")

def do_list():
    for p in list_players():
        print(f"{p['id']:3} | {p['name']:<15} Lv {p['level']}  Score {p['score']}")

def do_view():
    pid = prompt_int("Player id")
    p = get_player(pid)
    if p:
        print(p)
    else:
        print("Not found")

def do_update():
    pid = prompt_int("Player id")
    p = get_player(pid)
    if not p:
        print("Not found"); return
    name = input(f"Name [{p['name']}]: ") or p["name"]
    level = prompt_int("Level", p["level"])
    score = prompt_int("Score", p["score"])
    if update_player(pid, name=name, level=level, score=score):
        print("Updated")
    else:
        print("Failed")

def do_delete():
    pid = prompt_int("Player id")
    if delete_player(pid):
        print("Deleted")
    else:
        print("Not found")

def main():
    init_db()
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            do_create()
        elif choice == "2":
            do_list()
        elif choice == "3":
            do_view()
        elif choice == "4":
            do_update()
        elif choice == "5":
            do_delete()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
