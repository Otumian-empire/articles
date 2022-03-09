import unittest
from sample_2 import (contains_character, is_valid_size, is_valid_password)


class TestContainsCharacter(unittest.TestCase):
    def test_empty_password_or_and_empty_sack(self):
        self.assertFalse(contains_character())

    def test_char_i_in_str_python(self):
        self.assertFalse(contains_character("i", "python"))

    def test_str_py_in_str_python(self):
        self.assertTrue(contains_character("py", "python"))

    def test_str_python_in_str_python(self):
        self.assertTrue(contains_character("python", "python"))


class TestIsValidSize(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_size(""))

    def test_4_char_password(self):
        self.assertFalse(is_valid_size("pass"))

    def test_6_char_password(self):
        self.assertTrue(is_valid_size("passwd"))

    def test_16_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!"))

    def test_20_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!/+20"))

    def test_21_char_password(self):
        self.assertFalse(is_valid_size("ThisIs1Password!/+20&"))


class TestIsValidPassword(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_password())

    def test_password_of_size_three(self):
        self.assertFalse(is_valid_password("pas"))

    def test_password_of_size_ten(self):
        self.assertFalse(is_valid_password("Password12"))
        self.assertTrue(is_valid_password("Password1_"))

    def test_password_of_size_twenty(self):
        self.assertTrue(is_valid_password("Password12Password_$"))

    def test_password_with_invalid_special_character_semicolon(self):
        self.assertFalse(is_valid_password("Password1_;"))
        self.assertFalse(is_valid_password("Password1;"))

    def test_password_with_no_digit(self):
        self.assertFalse(is_valid_password("Password_"))

    def test_password_with_no_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1_"))

    def test_password_with_no_uppercase(self):
        self.assertFalse(is_valid_password("password1_"))

    def test_password_without_valid_special_character(self):
        self.assertFalse(is_valid_password("Password1"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password1_"))
        self.assertTrue(is_valid_password("PassWord34$"))


if __name__ == "__main__":
    unittest.main()
