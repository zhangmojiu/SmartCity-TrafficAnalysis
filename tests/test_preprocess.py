import unittest
from src.data_processing.preprocess import DataPreprocessor
import pandas as pd


class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.data_dir = 'data/raw/'  # 假设数据目录
        self.preprocessor = DataPreprocessor(self.data_dir)

    def test_load_data(self):
        data = self.preprocessor.load_data()
        self.assertEqual(isinstance(data, dict), True)


if __name__ == '__main__':
    unittest.main()