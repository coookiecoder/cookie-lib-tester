from ctypes import *

cookie_lib = CDLL("./cookie-lib/libcookie_lib.so")
cookie_lib.cookie_put_char.argtypes = [c_char]
cookie_lib.cookie_put_char.restype = c_uint64

cookie_lib.cookie_strlen.argtypes = [c_char_p]
cookie_lib.cookie_strlen.restype = c_uint64

def putchar(c):
    return cookie_lib.cookie_put_char(c.encode("utf-8"))

def strlen(s):
    return cookie_lib.cookie_strlen(s.encode("utf-8"))