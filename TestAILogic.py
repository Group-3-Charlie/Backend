import unittest
import pandas as pd
from code.ai_logic import AILogic


class TestAILogic(unittest.TestCase):

    def setUp(self):
        self.ai_logic = AILogic()
        self.ai_logic.load_data('usagers.csv')

    def test_load_data(self):
        self.assertIsInstance(self.ai_logic.df, pd.DataFrame)

    def test_select_target(self):
        self.ai_logic.select_target('grav')
        self.assertEqual(self.ai_logic.target, 'grav')

    def test_predict(self):
        self.ai_logic.select_target('grav')
        predictions = self.ai_logic.predict()
        self.assertIsInstance(predictions, list)


if __name__ == '__main__':
    unittest.main()
