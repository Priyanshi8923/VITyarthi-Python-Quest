LESSONS = {
    1: {
        "title": "Problem Solving & Algorithm Thinking",
        "points": [
            "Break a large problem into smaller tasks before coding.",
            "Use algorithms, flowcharts and pseudo code to plan a solution.",
            "Think about correctness, time complexity and space complexity."
        ],
    },
    2: {
        "title": "Python Basics",
        "points": [
            "Python executes statements and expressions using clear syntax.",
            "Variables can hold values of different types.",
            "Functions make repeated work easier to organise and reuse."
        ],
    },
    3: {
        "title": "Algorithms & Control Flow",
        "points": [
            "Loops repeat work and conditionals make decisions.",
            "Algorithms such as counting, summation and base conversion use simple steps.",
            "break and continue change how loops progress."
        ],
    },
    4: {
        "title": "Math & Algorithmic Techniques",
        "points": [
            "Euclid's Algorithm is useful for finding a GCD.",
            "Prime numbers and factorisation are basic number-theory tools.",
            "An iterative Fibonacci solution avoids unnecessary repeated work."
        ],
    },
    5: {
        "title": "Lists, Tuples, Sets & Dictionaries",
        "points": [
            "Choose a data structure according to what the program needs.",
            "Lists are ordered and mutable; tuples are ordered and immutable.",
            "Sets hold unique values and dictionaries provide key-value lookup."
        ],
    },
}


def show_lesson(unit: int) -> None:
    lesson = LESSONS[unit]
    print(f"\n--- {lesson['title']} ---")
    for point in lesson["points"]:
        print(f"• {point}")