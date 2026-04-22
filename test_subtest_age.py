import unittest

# Functions
def is_child(age):
    return 0 <= age <= 9

def is_adult(age):
    return 18 <= age <= 64

def is_golden(age):
    return age >= 65


class TestIsChild(unittest.TestCase):

    def test_child_age(self):
        for age in range(0, 9):  # 0–8 like your example
            with self.subTest(age=age):
                result = is_child(age)
                print(f"{age} is considered as a child.")
                self.assertTrue(result)


class TestIsAdult(unittest.TestCase):

    def test_adult_age(self):
        for age in range(18, 25):  # example range
            with self.subTest(age=age):
                result = is_adult(age)
                print(f"{age} is considered as an adult.")
                self.assertTrue(result)


class TestIsGolden(unittest.TestCase):

    def test_golden_age(self):
        for age in range(65, 70):  # example range
            with self.subTest(age=age):
                result = is_golden(age)
                print(f"{age} is considered as a golden age.")
                self.assertTrue(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)