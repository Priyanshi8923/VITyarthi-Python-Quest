from .models import Player, Question


def ask_question(question: Question, player: Player) -> bool:
    """Display one question, validate input and update the player's progress."""
    print("\n" + "-" * 65)
    print(f"{question.topic}: {question.prompt}")
    for number, option in enumerate(question.options, start=1):
        print(f"  {number}. {option}")

    while True:
        raw = input("Your answer (number): ").strip()
        if not raw.isdigit() or not 1 <= int(raw) <= len(question.options):
            print("Please enter one of the option numbers shown above.")
            continue
        choice = int(raw) - 1
        break

    correct = choice == question.answer
    player.record_answer(question.question_id, correct, 10 if correct else 0)

    if correct:
        print("Nice! That's correct. +10 points.")
    else:
        print(f"Not quite. The correct answer is: {question.options[question.answer]}")
        print(f"Why: {question.explanation}")
    return correct


def run_unit(unit: int, player: Player, questions: list[Question]) -> None:
    """Run the learning checkpoint for one unit."""
    unit_questions = [q for q in questions if q.unit == unit]
    print(f"\n=== Unit {unit} checkpoint ===")
    print(f"You have {len(unit_questions)} questions. Take your time.")

    for question in unit_questions:
        ask_question(question, player)

    if unit not in player.completed_units:
        player.completed_units.append(unit)