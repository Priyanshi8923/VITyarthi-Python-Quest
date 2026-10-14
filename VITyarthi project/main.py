"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             PYTHON QUEST: ACADEMIC ADVENTURE
      Complete Coverage of Unit 1 to Unit 5 Syllabus Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



def print_header():
    print("\n" + "~" * 65)
    print("        WELCOME TO PYTHON QUEST: ACADEMIC EDITION          ")
    print("~" * 65)


def print_hud(name, score, room_name):
    print("\n" + "*" * 65)
    print(" HERO: " + name.upper() + " | SCORE: " + str(score) + " | LOCATION: " + room_name)
    print("-" * 65)


def ask_interactive_question(question, options, correct_index, explanation):
    attempts = 0
    while True:
        attempts += 1
        print("\n[CHALLENGE]: " + question + "\n")
        for idx, opt in enumerate(options, 1):
            print("  [" + str(idx) + "] " + opt)

        choice = input("\nSelect your choice (1-" + str(len(options)) + "): ").strip()

        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                if choice_num == correct_index:
                    print("\n[SUCCESS!] " + explanation)
                    if attempts == 1:
                        print("Perfect! You earned +50 Score on your first try!")
                        return 50
                    else:
                        print("Correct! You earned +25 Score on retry.")
                        return 25
                else:
                    print("\n[INCORRECT!] " + explanation)
                    print(">>> Try Again! Read carefully and choose the correct answer. <<<\n")
            else:
                print("Invalid option number! Choose between 1 and " + str(len(options)) + ".")
        else:
            print("Invalid input! Please enter a number.")


def ask_code_output(question, correct_answer, explanation):
    attempts = 0
    while True:
        attempts += 1
        print("\n[CODE OUTPUT PUZZLE]: " + question)
        ans = input("Type your answer: ").strip()

        # Normalize spacing so minor formatting differences (extra/missing
        # spaces around commas, brackets etc.) don't count as wrong.
        normalized_ans = ans.replace(" ", "")
        normalized_correct = correct_answer.replace(" ", "")

        if normalized_ans == normalized_correct:
            print("\n[EXCELLENT!] " + explanation)
            if attempts == 1:
                print("Perfect! You earned +50 Score on your first try!")
                return 50
            else:
                print("Correct! You earned +25 Score on retry.")
                return 25
        else:
            print("\n[INCORRECT!] Expected: " + correct_answer)
            print(">>> Try Again! Check syntax, spaces, and quotes carefully. <<<\n")


# ============================================================
#                      UNIT 1: TEACHING & QUIZ
# ============================================================
def teach_and_quiz_unit1(player_name, score):
    room_name = "Unit 1: Problem Solving Vault"
    print_hud(player_name, score, room_name)

    print("\n=== LESSON 1.1: Problem Solving & Top-Down Design ===")
    print("- Problem Solving Aspect: Breaking real-world issues into systematic steps.")
    print("- Top-Down Design: Breaking a complex master problem into smaller, solvable sub-modules.")
    input("\n[Press ENTER to attempt Challenge 1.1...]")

    q1 = "What is the primary objective of Top-Down Design in software development?"
    opts1 = [
        "To write code without planning",
        "To break a complex system into smaller, manageable sub-problems",
        "To execute code directly in hardware",
        "To skip algorithm design entirely"
    ]
    exp1 = "Top-Down Design divides high-level tasks into detailed sub-tasks."
    score += ask_interactive_question(q1, opts1, 2, exp1)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 1.2: Algorithms, Flowcharts, & Pseudo Code ===")
    print("- Algorithm: Finite, step-by-step logic to solve a problem.")
    print("- Flowchart: Diagrammatic representation of algorithms using standard symbols.")
    print("- Pseudo Code: Plain-text readable blueprint of code before writing actual programming statements.")
    print("- Programming Language: The final, real code (like Python) that a computer can actually run.")
    print("  These three (flowchart, pseudo code, programming language) are the 3 ways to")
    print("  IMPLEMENT an algorithm.")
    input("\n[Press ENTER to attempt Challenge 1.2...]")

    q2 = "Which representation uses visual standard symbols like ovals, rectangles, and diamonds?"
    opts2 = ["Pseudo Code", "Python Interpreter", "Flowchart", "Machine Code"]
    exp2 = "Flowcharts use geometric shapes to visually map logic flow."
    score += ask_interactive_question(q2, opts2, 3, exp2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 1.3: Program Verification & Algorithm Efficiency ===")
    print("- Program Verification: Proving that an algorithm produces correct output for all valid inputs.")
    print("- Efficiency & Analysis: Evaluating an algorithm based on Time Complexity and Space Complexity.")
    input("\n[Press ENTER to attempt Challenge 1.3...]")

    q3 = "How is the efficiency of an algorithm primarily evaluated?"
    opts3 = [
        "By how colorful the output looks",
        "By Time Complexity (speed) and Space Complexity (memory)",
        "By the number of lines of comments written",
        "By using single quotes instead of double quotes"
    ]
    exp3 = "Algorithm efficiency measures time and memory consumption."
    score += ask_interactive_question(q3, opts3, 2, exp3)

    return score


# ============================================================
#                      UNIT 2: TEACHING & QUIZ
# ============================================================
def teach_and_quiz_unit2(player_name, score):
    room_name = "Unit 2: Python Data & Statements Labyrinth"
    print_hud(player_name, score, room_name)

    print("\n=== LESSON 2.1: Python Interpreter & Interactive Mode ===")
    print("- Interpreter: Executes Python code line-by-line.")
    print("- Interactive Mode (REPL): Executes code instantly line-by-line.")
    print("- Quotes Detail: Both single quotes ('hello') and double quotes (\"hello\") are identical in Python!")
    print("- Colon (:) Detail: Used after control statements (if, for, def) to open an indented block.")
    input("\n[Press ENTER to attempt Challenge 2.1...]")

    q1 = "What is the result of executing print('Python') vs print(\"Python\")?"
    opts1 = [
        "Single quotes cause a Syntax Error",
        "Double quotes print in capital letters",
        "Both produce the exact same output: Python",
        "Single quotes are used only for numbers"
    ]
    exp1 = "Python treats single and double quotes identically for strings."
    score += ask_interactive_question(q1, opts1, 3, exp1)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 2.2: Values, Types, Variables & Tuple Assignment ===")
    print("- Values & Types: int (10), float (10.5), str ('hi'), bool (True).")
    print("- Tuple Assignment: Assigning multiple variables in one line! (e.g., x, y = 5, 10)")
    print("- Value Swapping: x, y = y, x (Swaps x and y effortlessly!).")
    input("\n[Press ENTER to attempt Challenge 2.2...]")

    q2 = "After running: a, b = 10, 20  followed by: a, b = b, a ... What is the value of 'a'?"
    opts2 = ["10", "20", "Tuple Error", "0"]
    exp2 = "Tuple assignment swaps values, so 'a' becomes 20."
    score += ask_interactive_question(q2, opts2, 2, exp2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 2.3: Precedence of Operators & Expressions ===")
    print("- Operator Precedence (PEMDAS): Parentheses (), Exponentiation **, Mult/Div *, /, Add/Sub +, -")
    print("- Statement vs Expression: A STATEMENT is a full line of code that does something")
    print("  (like x = 5). An EXPRESSION is anything that produces a value (like 5 * 2).")
    print("- Comments: Lines starting with '#' are ignored by Python.")
    input("\n[Press ENTER to attempt Challenge 2.3...]")

    q_code = "What is the exact output of: print(2 + 3 * 4) ?"
    exp_code = "Multiplication (*) happens before addition (+), so 3*4=12, then +2 = 14."
    score += ask_code_output(q_code, "14", exp_code)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 2.4: Modules, Functions, Execution & Arguments ===")
    print("- Module: A file containing pre-written Python code (functions/variables) you can reuse.")
    print("  You bring a module into your program using: import math")
    print("- Function Definition: Created using `def function_name(parameter):`.")
    print("- Flow of Execution: Function bodies are executed ONLY when called.")
    print("- Parameters vs Arguments:")
    print("  - Parameter: Variable in function definition -> `def greet(name):`")
    print("  - Argument: Actual value passed in call -> `greet('VIT')`")
    input("\n[Press ENTER to attempt Challenge 2.4...]")

    q3 = "In `def add(x, y):`, what are `x` and `y` called?"
    opts3 = ["Arguments", "Parameters", "Modules", "Return Statements"]
    exp3 = "Variables inside the function header definition are called Parameters."
    score += ask_interactive_question(q3, opts3, 2, exp3)

    q4 = "Which statement correctly imports the built-in 'math' module in Python?"
    opts4 = ["include math", "import math", "using math", "math.import()"]
    exp4 = "The `import` keyword is used to bring a module's code into your program."
    score += ask_interactive_question(q4, opts4, 2, exp4)

    return score


# ============================================================
#         UNIT 3: FUNDAMENTAL ALGORITHMS & CONTROL FLOW
# ============================================================
def teach_and_quiz_unit3(player_name, score):
    room_name = "Unit 3: Fundamental Algorithms Chamber"
    print_hud(player_name, score, room_name)

    print("\n=== LESSON 3.1: Exchange, Factorial, Fibonacci & Char Conversion ===")
    print("- Swapping Values: `a, b = b, a` swaps two variables instantly in Python.")
    print("- Factorial Computation: Product of integers from 1 to N (e.g., 5! = 120).")
    print("- Fibonacci Sequence: Series where next number is sum of previous two (0, 1, 1, 2, 3, 5...).")
    print("- Character to Number Conversion: `ord('A')` returns 65, `chr(65)` returns 'A'.")
    input("\n[Press ENTER to attempt Challenge 3.1...]")

    q1 = "Which built-in Python function converts a character to its numerical ASCII value?"
    opts1 = ["int()", "ord()", "chr()", "ascii()"]
    exp1 = "`ord()` converts character to ASCII, while `chr()` converts ASCII number back to character."
    score += ask_interactive_question(q1, opts1, 2, exp1)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 3.2: Counting & Summation ===")
    print("- Counting: Using a loop with a counter variable (starting at 0) that increases by")
    print("  1 every time a condition is met. Used to count how many items match something.")
    print("- Summation: Using a loop with a total variable (starting at 0) that adds each")
    print("  number to itself as the loop runs, to get a running total.")
    print("  Example:")
    print("    total = 0")
    print("    for i in range(1, 5):")
    print("        total += i")
    print("    print(total)")
    input("\n[Press ENTER to attempt Challenge 3.2...]")

    q_code2 = "What is the output of:\ntotal = 0\nfor i in range(1, 5):\n    total += i\nprint(total) ?"
    exp_code2 = "range(1, 5) gives 1, 2, 3, 4. Sum = 1 + 2 + 3 + 4 = 10."
    score += ask_code_output(q_code2, "10", exp_code2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 3.3: Reverse & Base Conversion ===")
    print("- Reverse (a number): Repeatedly take the last digit using `% 10` (modulus) and")
    print("  remove it using `// 10` (integer division), building the reversed number.")
    print("  Example: 123 becomes 321.")
    print("- Base Conversion: To convert a decimal number to binary manually, you repeatedly")
    print("  DIVIDE the number by 2 and collect the remainders (0 or 1); reading the")
    print("  remainders bottom-to-top gives the binary number.")
    input("\n[Press ENTER to attempt Challenge 3.3...]")

    q2 = "To manually convert a decimal number to binary, what operation do you repeat?"
    opts2 = [
        "Repeated division by 2, collecting the remainders",
        "Repeated multiplication by 2",
        "Repeated division by 10",
        "Repeated subtraction of 1"
    ]
    exp2 = "Dividing by 2 repeatedly and reading remainders bottom-to-top gives the binary form."
    score += ask_interactive_question(q2, opts2, 1, exp2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 3.4: Python Conditionals & Logic ===")
    print("- Branching Keywords: `if`, `elif`, `else`.")
    print("- Boolean Operators: `and` (both True), `or` (at least one True), `not` (reverses state).")
    print("- Indentation Detail: Python uses indentation (usually 4 spaces) after a colon (`:`)")
    print("  to open a block, instead of curly braces { } like other languages.")
    input("\n[Press ENTER to attempt Challenge 3.4...]")

    q3 = "Which statement is true regarding Python conditional execution?"
    opts3 = [
        "Braces {} are required to define an 'if' block.",
        "A colon (:) follows condition, and code inside block must be indented.",
        "'elseif' is used instead of 'elif' in Python.",
        "'and' operator returns True if any one condition is True."
    ]
    exp3 = "Python uses colon (:) and indentation instead of curly braces."
    score += ask_interactive_question(q3, opts3, 2, exp3)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 3.5: Loops & Jump Control Statements ===")
    print("- Loops: `while` (runs until condition is False), `for` (iterates over sequence/range).")
    print("- Jump Keywords:")
    print("  - `break`: Terminates loop execution completely.")
    print("  - `continue`: Skips current iteration and moves to next turn.")
    print("  - `pass`: Placeholder that does nothing (avoids syntax error).")
    input("\n[Press ENTER to attempt Challenge 3.5...]")

    q4 = "Which keyword skips the current iteration of a loop and moves to the next turn?"
    opts4 = ["break", "continue", "pass", "stop"]
    exp4 = "`continue` skips current cycle, whereas `break` exits the entire loop."
    score += ask_interactive_question(q4, opts4, 2, exp4)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 3.6: Practical Code Output ===")
    q_code = "What is the output of:\ncount = 0\nfor x in range(3):\n    count += x\nprint(count) ?"
    exp_code = "range(3) generates 0, 1, 2. Sum = 0 + 1 + 2 = 3."
    score += ask_code_output(q_code, "3", exp_code)

    return score


# ============================================================
#         UNIT 4: FACTORING METHODS & MATH ALGORITHMS
# ============================================================
def teach_and_quiz_unit4(player_name, score):
    room_name = "Unit 4: Factoring Methods Cavern"
    print_hud(player_name, score, room_name)

    print("\n=== LESSON 4.1: Divisors, GCD & Prime Numbers ===")
    print("- Smallest Divisor: Finding the smallest integer > 1 that divides N evenly.")
    print("- GCD (Greatest Common Divisor): Solved efficiently using Euclid's Algorithm.")
    print("- Prime Numbers: Numbers with exactly TWO positive factors: 1 and itself (2, 3, 5, 7, 11...).")
    print("- Prime Factors: Expressing a number as a product of prime numbers (e.g., 12 = 2 * 2 * 3).")
    input("\n[Press ENTER to attempt Challenge 4.1...]")

    q1 = "Which algorithm is used to compute the Greatest Common Divisor (GCD) using repeated remainder operation?"
    opts1 = ["Binary Search", "Euclid's Algorithm", "Bubble Sort", "Linear Search"]
    exp1 = "Euclid's Algorithm efficiently computes GCD using modulus: gcd(a, b) = gcd(b, a % b)."
    score += ask_interactive_question(q1, opts1, 2, exp1)

    q2 = "What makes a number 'Prime'?"
    opts2 = [
        "It is an odd number",
        "It has exactly two distinct positive divisors: 1 and itself",
        "It can be divided by 2",
        "It ends with 1 or 3"
    ]
    exp2 = "Prime numbers have no other divisors except 1 and themselves (Note: 1 is NOT a prime number)."
    score += ask_interactive_question(q2, opts2, 2, exp2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 4.2: Random Numbers & Raising to Large Power ===")
    print("- Pseudo-Random Numbers: Numbers generated using deterministic math algorithms (looks random).")
    print("  In Python: `import random; random.randint(1, 10)`.")
    print("- Raising to Large Power: Python handles large integer arithmetic automatically using `**`.")
    print("  Example: `2 ** 10` gives 1024.")
    print("- Square Root: Computed using exponentiation `x ** 0.5` or `math.sqrt(x)`.")
    input("\n[Press ENTER to attempt Challenge 4.2...]")

    q3 = "Why are computer-generated random numbers called 'Pseudo-Random'?"
    opts3 = [
        "Because they are entirely fake numbers",
        "Because they are generated using a deterministic mathematical formula/seed",
        "Because they are only decimal values",
        "Because they can only be generated in Linux"
    ]
    exp3 = "Pseudo-random numbers appear random but are produced by deterministic algorithm logic."
    score += ask_interactive_question(q3, opts3, 2, exp3)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 4.3: Computing the Nth Fibonacci Number Efficiently ===")
    print("- The basic Fibonacci sequence (Unit 3) can be slow if you recompute earlier terms")
    print("  again and again using plain recursion.")
    print("- The EFFICIENT method keeps just TWO variables (previous, current) and updates")
    print("  them in a loop, so each number is calculated only once.")
    print("  Example:")
    print("    a, b = 0, 1")
    print("    for _ in range(n):")
    print("        a, b = b, a + b")
    input("\n[Press ENTER to attempt Challenge 4.3...]")

    q4 = "Which approach efficiently computes the nth Fibonacci number using only two variables updated in a loop?"
    opts4 = [
        "Plain recursion without storing any previous results",
        "Iterative approach with two variables (a, b) updated each loop",
        "Sorting the numbers first",
        "Randomly guessing until correct"
    ]
    exp4 = "Using two variables and updating them each loop avoids repeated recomputation."
    score += ask_interactive_question(q4, opts4, 2, exp4)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 4.4: Practical Code Output ===")
    q_code = "What is the output of: print(16 ** 0.5) ?"
    exp_code = "Raising a number to power 0.5 computes its square root, so 16 ** 0.5 = 4.0."
    score += ask_code_output(q_code, "4.0", exp_code)

    return score


# ============================================================
#   UNIT 5: DATA STRUCTURES (LISTS, TUPLES, SETS, DICTS) & ARRAYS
# ============================================================
def teach_and_quiz_unit5(player_name, score):
    room_name = "Unit 5: Array Techniques Library"
    print_hud(player_name, score, room_name)

    print("\n=== LESSON 5.1: Data Structures Comparison ===")
    print("- LIST [1, 2, 3]: Ordered, Mutable (changeable), allows duplicates.")
    print("- TUPLE (1, 2, 3): Ordered, IMMUTABLE (cannot be modified after creation).")
    print("- SET {1, 2, 3}: Unordered, Mutable, stores ONLY UNIQUE elements (no duplicates).")
    print("- DICTIONARY {'a': 1}: Key-Value pairs, fast lookup by Key.")
    print("- Time Tradeoff: Sets/Dicts offer much faster searching than Lists, but use more memory.")
    input("\n[Press ENTER to attempt Challenge 5.1...]")

    q1 = "Which Python data structure is IMMUTABLE and cannot be modified after creation?"
    opts1 = ["List []", "Set {}", "Tuple ()", "Dictionary {}"]
    exp1 = "Tuples are immutable sequences in Python."
    score += ask_interactive_question(q1, opts1, 3, exp1)

    q2 = "Which data structure automatically removes all duplicate values?"
    opts2 = ["List", "Set", "Tuple", "Array"]
    exp2 = "Sets store unique elements only and discard any duplicates automatically."
    score += ask_interactive_question(q2, opts2, 2, exp2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 5.2: Array Reversal & Finding the Maximum ===")
    print("- Reversal: Reversing elements using slicing `arr[::-1]` or `.reverse()`.")
    print("- Maximum Finding: Tracking current largest element using `max()` or a custom loop")
    print("  that compares each element to the largest one found so far.")
    input("\n[Press ENTER to attempt Challenge 5.2...]")

    q3 = "What is the primary trade-off when using Dictionaries over Lists?"
    opts3 = [
        "Dictionaries use more memory but offer faster key lookups",
        "Dictionaries cannot store strings",
        "Lists use more memory than Dictionaries",
        "Dictionaries do not allow values"
    ]
    exp3 = "Dictionaries trade extra memory usage (hash tables) for faster lookup speeds."
    score += ask_interactive_question(q3, opts3, 1, exp3)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 5.3: Array Counting, Duplicate Removal & Partitioning ===")
    print("- Array Counting: Looping through an array and using a counter variable to count how")
    print("  many elements match a condition (e.g., counting even numbers).")
    print("- Removal of Duplicates (from a SORTED array): Since equal elements sit next to each")
    print("  other, you compare each element to the PREVIOUS one; if they match, it's a duplicate.")
    print("- Partitioning: Splitting an array around a chosen PIVOT value so smaller elements")
    print("  go to the left and larger elements go to the right (the core idea behind Quicksort).")
    input("\n[Press ENTER to attempt Challenge 5.3...]")

    q4 = "In a SORTED array, which condition identifies a duplicate element in a single loop pass?"
    opts4 = [
        "The current element equals the previous element",
        "The current index equals 0",
        "The current element is even",
        "The current element is negative"
    ]
    exp4 = "In a sorted array, duplicates always sit next to each other, so comparing with the previous element works."
    score += ask_interactive_question(q4, opts4, 1, exp4)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 5.4: Finding the Kth Smallest Element ===")
    print("- The simplest method: SORT the array in ascending order, then the Kth smallest")
    print("  element is at index (K - 1), since Python lists start counting from index 0.")
    print("  Example: arr = [7, 2, 9, 4]  ->  sorted: [2, 4, 7, 9]")
    print("  The 2nd smallest (K=2) is at index 1, which is 4.")
    input("\n[Press ENTER to attempt Challenge 5.4...]")

    q_code2 = "What is the output of:\narr = [7, 2, 9, 4]\narr.sort()\nprint(arr[1]) ?"
    exp_code2 = "Sorting gives [2, 4, 7, 9]. Index 1 (the 2nd element) is 4."
    score += ask_code_output(q_code2, "4", exp_code2)

    print_hud(player_name, score, room_name)
    print("\n=== LESSON 5.5: Practical Code Output ===")
    q_code = "What is the output of:\nnums = [10, 20, 30]\nprint(nums[::-1]) ?"
    exp_code = "`[::-1]` slices the list in reverse order, resulting in `[30, 20, 10]`."
    score += ask_code_output(q_code, "[30, 20, 10]", exp_code)

    return score


# ============================================================
#                     FINAL MEGA QUIZ (ALL UNITS)
# ============================================================
def final_mega_quiz(player_name, score):
    room_name = "FINAL BOSS: The Mega Quiz Chamber"
    print_hud(player_name, score, room_name)
    print("\nThe Grand Wizard of Pythonia appears before you.")
    print("To finally break the curse, you must prove mastery over")
    print("EVERYTHING you have learned, across all 5 Units!\n")

    print_hud(player_name, score, room_name)
    q1 = "(Unit 1) What does Program Verification prove about an algorithm?"
    opts1 = [
        "That it looks visually appealing",
        "That it produces correct output for all valid inputs",
        "That it uses the fewest characters possible",
        "That it never uses variables"
    ]
    exp1 = "Verification proves correctness of the algorithm's output."
    score += ask_interactive_question(q1, opts1, 2, exp1)

    q2 = "(Unit 2) What are 'x' and 'y' called in: x, y = 5, 10 ?"
    opts2 = ["A Loop", "Tuple Assignment", "A Function Call", "A Comment"]
    exp2 = "Assigning multiple variables in one line using commas is Tuple Assignment."
    score += ask_interactive_question(q2, opts2, 2, exp2)

    q_code3 = "(Unit 3) What is the output of:\nn = 5\nfact = 1\nfor i in range(1, n + 1):\n    fact *= i\nprint(fact) ?"
    exp_code3 = "This computes 5! = 1*2*3*4*5 = 120."
    score += ask_code_output(q_code3, "120", exp_code3)

    q4 = "(Unit 4) Which Python operator is used to raise a number to a power?"
    opts4 = ["^", "**", "%%", "//"]
    exp4 = "The `**` operator performs exponentiation in Python, e.g. 2 ** 3 = 8."
    score += ask_interactive_question(q4, opts4, 2, exp4)

    q5 = "(Unit 5) Which data structure would you choose for the FASTEST lookup by a unique key?"
    opts5 = ["List", "Tuple", "Dictionary", "String"]
    exp5 = "Dictionaries use key-value pairs for very fast lookups."
    score += ask_interactive_question(q5, opts5, 3, exp5)

    q_code6 = "(Mixed Recap) What is the output of:\na, b = 3, 7\na, b = b, a\nprint(a, b) ?"
    exp_code6 = "Tuple-swap: a becomes 7, b becomes 3, so it prints: 7 3"
    score += ask_code_output(q_code6, "7 3", exp_code6)

    return score


# ============================================================
#                           MAIN GAME LOOP
# ============================================================
def main():
    print_header()

    print("\nSTORYLINE:")
    print("You are trapped in the 'Code Citadel'. To escape and graduate,")
    print("you must learn the core concepts of Python and solve all room challenges!\n")

    player_name = input("Enter your Hero Name: ").strip()
    if not player_name:
        player_name = "Coder"

    score = 0
    print("\nWelcome, " + player_name + "! Prepare for your quest.")
    input("\nPress [ENTER] to enter Unit 1...")

    score = teach_and_quiz_unit1(player_name, score)
    print("\n" + "*" * 65)
    print(" CONGRATULATIONS! You passed UNIT 1: Computer Problem Solving!")
    print(" Current Score: " + str(score))
    print("*" * 65)
    input("\nPress [ENTER] to unlock and enter Unit 2...")

    score = teach_and_quiz_unit2(player_name, score)
    print("\n" + "*" * 65)
    print(" CONGRATULATIONS! You passed UNIT 2: Python Data & Statements!")
    print(" Current Score: " + str(score))
    print("*" * 65)
    input("\nPress [ENTER] to unlock and enter Unit 3...")

    score = teach_and_quiz_unit3(player_name, score)
    print("\n" + "*" * 65)
    print(" CONGRATULATIONS! You passed UNIT 3: Fundamental Algorithms!")
    print(" Current Score: " + str(score))
    print("*" * 65)
    input("\nPress [ENTER] to unlock and enter Unit 4...")

    score = teach_and_quiz_unit4(player_name, score)
    print("\n" + "*" * 65)
    print(" CONGRATULATIONS! You passed UNIT 4: Factoring Methods!")
    print(" Current Score: " + str(score))
    print("*" * 65)
    input("\nPress [ENTER] to unlock and enter Unit 5...")

    score = teach_and_quiz_unit5(player_name, score)
    print("\n" + "*" * 65)
    print(" CONGRATULATIONS! You passed UNIT 5: Arrays & Data Structures!")
    print(" Current Score: " + str(score))
    print("*" * 65)
    input("\nPress [ENTER] to face the FINAL MEGA QUIZ...")

    score = final_mega_quiz(player_name, score)

    print_header()
    print("\nVICTORY! YOU HAVE COMPLETED THE ENTIRE PYTHON QUEST!")
    print("Final Score: " + str(score) + " / 1550")
    print("You now have rock-solid fundamentals across the FULL syllabus:")
    print("Problem Solving, Python Basics, Algorithms, Factoring Methods,")
    print("and Arrays & Data Structures!")


if __name__ == "__main__":
    main()
