import subprocess
import unittest

subprocess.run(['make', 'libcookie_lib.so', '-C', 'cookie-lib'])

from loader import *

class StringTest(unittest.TestCase):
    def test_put_char(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putchar(char), 1)

    def test_put_char_new_line(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putchar_nl(char), 2)

    def test_put_char_file_descriptor(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putchar_fd(char, 1), 1)

    def test_put_char_new_line_file_descriptor(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putchar_fd_nl(char, 1), 2)

    def test_put_string(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putstr(char), 1)
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(putstr(string), string.__len__())

    def test_put_string_new_line(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putstr_nl(char), 2)
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(putstr_nl(string), string.__len__() + 1)

    def test_put_string_file_descriptor(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putstr_fd(char, 1), 1)
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(putstr_fd(string, 1), string.__len__())

    def test_put_string_new_line_file_descriptor(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putstr_fd_nl(char, 1), 2)
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(putstr_fd_nl(string, 1), string.__len__() + 1)

    def test_string_compare(self):
        self.assertEqual(strcmp("test", "test"), 0)
        self.assertEqual(strcmp("test", "tese"), 1)

    def test_string_compare_n(self):
        self.assertEqual(strcmp_n("test", "test", 4), 0)
        self.assertEqual(strcmp_n("test", "tese", 4), 1)
        self.assertEqual(strcmp_n("test", "tese", 3), 1)

    def test_string_duplicate(self):
        self.assertEqual(strdup("test"), b"test")

    def test_string_len(self):
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(strlen(string), string.__len__())


if __name__ == '__main__':
    unittest.main()
