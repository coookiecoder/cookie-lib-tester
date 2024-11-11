import subprocess

subprocess.run(['make', 'libcookie_lib.so', '-C', 'cookie-lib'])

import unittest

from loader import *

class MainTest(unittest.TestCase):
    def test_putchar(self):
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for char in array:
            self.assertEqual(putchar(char), 1)
    def test_strlen(self):
        array = ["test", "", "eoieurtowpeiutwer", "dfhdfg", "dfglhkjdfglkhjdflkhjdflhkjfgh"]
        for string in array:
            self.assertEqual(strlen(string), string.__len__())
            print("string : " + string)
            print("strlen : " + str(strlen(string)))



if __name__ == '__main__':
    unittest.main()
