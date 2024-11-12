import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        r = main.hello_world()
        self.assertIsNotNone(r)


if __name__ == '__main__':
    unittest.main()
