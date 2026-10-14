def show_welcome() -> None:
    print("\n" + "=" * 65)
    print("              PYTHON QUEST: LEARN BY DOING")
    print("=" * 65)
    print("A small practice companion for Python fundamentals.")
    print("The idea is simple: learn a concept, answer a few questions,")
    print("see where you went wrong, and keep improving.")
    print("=" * 65)


def show_menu() -> None:
    print("\nWhat would you like to do?")
    print("1. Learn a unit")
    print("2. Practice a unit")
    print("3. View my progress")
    print("4. Reset progress")
    print("5. Exit")


def read_name() -> str:
    while True:
        name = input("\nWhat should I call you? ").strip()
        if name:
            return name[:40]
        print("Please enter a name so I can save your progress.")


def choose_unit() -> int:
    while True:
        raw = input("Choose a unit (1-5): ").strip()
        if raw in {"1", "2", "3", "4", "5"}:
            return int(raw)
        print("Please choose a unit from 1 to 5.")