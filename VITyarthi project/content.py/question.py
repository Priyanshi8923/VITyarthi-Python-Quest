from .models import Question


QUESTIONS = [
    # Unit 1
    Question("U1-Q1", 1, "Problem Solving",
            "What is the main idea of Top-Down Design?",
            ["Write everything in one function",
             "Break a large problem into smaller manageable parts",
             "Avoid planning before coding",
             "Skip algorithm design"],
            1, "Top-Down Design starts with the main problem and divides it into smaller tasks."),
    Question("U1-Q2", 1, "Algorithms",
            "Which representation normally uses ovals, rectangles and diamonds?",
            ["Pseudo code", "Flowchart", "Python interpreter", "Machine code"],
            1, "Flowcharts use standard symbols to show the flow of an algorithm."),
    Question("U1-Q3", 1, "Efficiency",
            "Which two measures are commonly used to discuss algorithm efficiency?",
            ["Colour and layout", "Time and space complexity",
             "Comments and variable names", "File size and font"],
            1, "Time complexity considers running time; space complexity considers memory use."),

    # Unit 2
    Question("U2-Q1", 2, "Python Basics",
            "What happens with print('Python') and print(\"Python\")?",
            ["Only the first works", "Only the second works",
             "Both print Python", "Both cause an error"],
            2, "Python accepts both single and double quotes for ordinary strings."),
    Question("U2-Q2", 2, "Variables",
            "After a, b = 10, 20 and a, b = b, a, what is a?",
            ["10", "20", "0", "It becomes a tuple"],
            1, "Tuple assignment lets Python swap the two values without a temporary variable."),
    Question("U2-Q3", 2, "Operators",
            "What is the output of print(2 + 3 * 4)?",
            ["20", "14", "24", "10"],
            1, "Multiplication has higher precedence than addition, so 3*4 is calculated first."),
    Question("U2-Q4", 2, "Functions",
            "In def add(x, y):, what are x and y?",
            ["Arguments", "Parameters", "Modules", "Comments"],
            1, "Parameters are the names written in a function definition."),

    # Unit 3
    Question("U3-Q1", 3, "Algorithms",
            "Which function converts a character to its Unicode code point?",
            ["int()", "ord()", "chr()", "ascii()"],
            1, "ord('A') returns the code point for A; chr() performs the reverse conversion."),
    Question("U3-Q2", 3, "Loops",
            "What is the output of total=0; for i in range(1,5): total += i?",
            ["5", "10", "15", "4"],
            1, "range(1,5) gives 1, 2, 3 and 4; their sum is 10."),
    Question("U3-Q3", 3, "Number Systems",
            "When converting decimal to binary manually, what is repeatedly done?",
            ["Multiply by 2", "Divide by 2 and collect remainders",
             "Divide by 10", "Subtract 1"],
            1, "Repeated division by 2 gives binary remainders from which the binary value is formed."),
    Question("U3-Q4", 3, "Conditionals",
            "Which statement about a Python if block is correct?",
            ["Braces are required", "A colon is followed by an indented block",
             "Python uses elseif", "and means either condition is true"],
            1, "Python uses a colon and indentation to define the block."),

    # Unit 4
    Question("U4-Q1", 4, "GCD",
            "Which algorithm uses repeated remainders to find the GCD?",
            ["Binary Search", "Euclid's Algorithm", "Bubble Sort", "Linear Search"],
            1, "Euclid's Algorithm repeatedly replaces the pair with (b, a % b)."),
    Question("U4-Q2", 4, "Prime Numbers",
            "What makes a number prime?",
            ["It is odd", "It has exactly two positive divisors",
             "It is divisible by 2", "It ends in 1 or 3"],
            1, "A prime number has exactly two positive divisors: 1 and itself."),
    Question("U4-Q3", 4, "Random Numbers",
            "Why are computer-generated random values often called pseudo-random?",
            ["They are fake", "They come from a deterministic process",
             "They are always decimals", "They only work on Linux"],
            1, "A deterministic algorithm generates them, even though the sequence can look random."),
    Question("U4-Q4", 4, "Fibonacci",
            "Which approach efficiently computes Fibonacci values using constant extra space?",
            ["Repeated plain recursion", "Iterative updates of two variables",
             "Sorting first", "Random guessing"],
            1, "Keeping the previous two values avoids repeatedly calculating earlier terms."),

    # Unit 5
    Question("U5-Q1", 5, "Data Structures",
            "Which Python data structure is immutable?",
            ["List", "Set", "Tuple", "Dictionary"],
            2, "A tuple cannot be changed after it is created."),
    Question("U5-Q2", 5, "Data Structures",
            "Which structure automatically stores unique elements?",
            ["List", "Set", "Tuple", "String"],
            1, "A set keeps unique values and removes duplicates."),
    Question("U5-Q3", 5, "Dictionaries",
            "What is a common trade-off of dictionaries compared with lists?",
            ["More memory for fast key lookup", "They cannot store strings",
             "They cannot store values", "They are always slower"],
            0, "Dictionaries generally use more memory but provide fast lookup by key."),
    Question("U5-Q4", 5, "Lists",
            "What is nums[::-1] for [10, 20, 30]?",
            ["[10, 20, 30]", "[30, 20, 10]", "[20, 10, 30]", "Error"],
            1, "A slice with a step of -1 returns the list in reverse order."),
]


def get_questions(unit=None):
    """Return all questions or only the questions for one unit."""
    if unit is None:
        return QUESTIONS.copy()
    return [q for q in QUESTIONS if q.unit == unit]


def get_units():
    return sorted({q.unit for q in QUESTIONS})