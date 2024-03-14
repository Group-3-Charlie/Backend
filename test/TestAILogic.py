import unittest
import pandas as pd
from code.ai_logic import AILogic


class TestAILogic(unittest.TestCase):
    """
    Test class for the AILogic class.
    """

    def setUp(self):
        """
        Set up the test.
        """
        self.ai_logic = AILogic()
        self.ai_logic.load_data('../dataset_examples/drinks.csv')

    def test_load_data(self):
        """
        Test the load_data method.
        :return:
        """
        self.assertIsInstance(self.ai_logic.df, pd.DataFrame)

    def test_select_target(self):
        """
        Test the select_target method.
        :return:
        """
        self.ai_logic.select_target('total_litres_of_pure_alcohol')
        self.assertEqual(self.ai_logic.target, 'total_litres_of_pure_alcohol')

    def test_predict(self):
        """
        Test the predict method.
        :return:
        """
        self.ai_logic.select_target('total_litres_of_pure_alcohol')
        predictions = self.ai_logic.predict()
        print(predictions)
        self.assertIsInstance(predictions, list)


if __name__ == '__main__':
    unittest.main()
