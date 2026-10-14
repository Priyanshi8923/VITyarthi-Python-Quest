# test_questions

import unittest
from app.questions import get_questions, get_units


class TestQuestionBank(unittest.TestCase):
    def test_all_units_present(self):
        self.assertEqual(get_units(), [1, 2, 3, 4, 5])

    def test_each_question_has_valid_answer(self):
        for question in get_questions():
            self.assertGreaterEqual(question.answer, 0)
            self.assertLess(question.answer, len(question.options))


if __name__ == "__main__":
    unittest.main()


# test_storage.py

import unittest
from unittest.mock import patch
from pathlib import Path
from app.models import Player
import app.storage as storage


class TestStorage(unittest.TestCase):
    def test_save_and_load(self):
        temp_file = Path("data/test_progress.json")
        with patch.object(storage, "SAVE_FILE", temp_file):
            player = Player("Test Student")
            player.score = 30
            storage.save_player(player)
            loaded = storage.load_player()
            self.assertEqual(loaded.name, "Test Student")
            self.assertEqual(loaded.score, 30)
            storage.clear_progress()


if __name__ == "__main__":
    unittest.main()


 # test_models.py

    import unittest
from app.models import Player


class TestPlayer(unittest.TestCase):
    def test_accuracy(self):
        player = Player("Aarav")
        player.record_answer("Q1", True, 10)
        player.record_answer("Q2", False)
        self.assertEqual(player.accuracy, 50.0)
        self.assertEqual(player.score, 10)

    def test_serialization(self):
        player = Player("Aarav")
        player.completed_units.append(1)
        data = player.to_dict()
        restored = Player.from_dict(data)
        self.assertEqual(restored.name, "Aarav")
        self.assertEqual(restored.completed_units, [1])


if __name__ == "__main__":
    unittest.main()