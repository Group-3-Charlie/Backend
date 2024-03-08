import unittest
import pandas as pd
from ai_logic import AILogic


class TestAILogic(unittest.TestCase):

    def setUp(self):
        self.ai_logic = AILogic()
        self.ai_logic.load_data('usagers.csv')  # Assuming you have a test.csv file for testing

    def test_load_data(self):
        self.assertIsInstance(self.ai_logic.df, pd.DataFrame)

    def test_select_target(self):
        self.ai_logic.select_target('grav')  # Assuming 'target_column' exists in your test.csv
        self.assertEqual(self.ai_logic.target, 'grav')

    def test_predict(self):
        self.ai_logic.select_target('grav')  # Assuming 'target_column' exists in your test.csv
        predictions = self.ai_logic.predict()
        self.assertIsInstance(predictions, list)


if __name__ == '__main__':
    unittest.main()
