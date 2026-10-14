

def create_player(name):
    """Creates a new player dictionary with starting stats."""
    return {
        "name": name,
        "score": 0,
        "questions_attempted": 0,
        "correct_answers": 0,
        "completed_units": [],
        "mistakes": []
    }

def record_player_answer(player, question_id, correct, points=50):
    """Updates player score and stats after an answer."""
    player["questions_attempted"] += 1
    if correct:
        player["correct_answers"] += 1
        player["score"] += points
    else:
        player["mistakes"].append(question_id)

def calculate_accuracy(player):
    """Calculates accuracy percentage."""
    attempted = player["questions_attempted"]
    if attempted == 0:
        return 0.0
    return round((player["correct_answers"] / attempted) * 100, 1)

def create_question(q_id, unit, topic, prompt, options, answer, explanation):
    """Creates a question dictionary."""
    return {
        "question_id": q_id,
        "unit": unit,
        "topic": topic,
        "prompt": prompt,
        "options": options,
        "answer": answer,
        "explanation": explanation
    }