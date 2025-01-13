import unittest
import utils  # utilsモジュールをインポート

class TestUtils(unittest.TestCase):
    def test_calculate_CER(self):
        # "hello" と "hello" のCERが0であることを確認
        self.assertEqual(utils.calculate_CER("hello", "hello"), 0)
        # 削除1回
        self.assertEqual(utils.calculate_CER("hello", "hell"), 1/5)
        # 挿入1回
        self.assertEqual(utils.calculate_CER("hello", "hellao"), 1/5)
        # 置換1回
        self.assertEqual(utils.calculate_CER("hello", "hallo"), 1/5)


    def test_calculate_MinCER(self):
        # "hello" と ["hello"] のCERが0であることを確認
        self.assertEqual(utils.calculate_MinCER(["hello", "hallo"], "hello"), 0)
        # "hello" と ["hallo", "hollo"] のCERが1/5であることを確認
        self.assertEqual(utils.calculate_MinCER(["hallo", "hollo"], "hello"), 1/5)


    def test_calculate_ACCat1(self):
        # "hello" と ["hello"] のaccuracyが1であることを確認
        self.assertEqual(utils.calculate_accuracy_at1(["hello"], "hello"), 1)
        # "hello" と ["hello", "world"] のaccuracyが1であることを確認
        self.assertEqual(utils.calculate_accuracy_at1(["hello", "world"], "hello"), 1)
        # "hello" と ["world"] のaccuracyが0であることを確認
        self.assertEqual(utils.calculate_accuracy_at1(["world"], "hello"), 0)


if __name__ == "__main__":
    unittest.main()
