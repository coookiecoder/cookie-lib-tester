from ctypes import *

cookie_lib = CDLL("./cookie-lib/libcookie_lib.so")
cookie_lib.cookie_put_char.argtypes = [c_char]
cookie_lib.cookie_put_char.restype = c_uint64
cookie_lib.cookie_put_char_nl.argtypes = [c_char]
cookie_lib.cookie_put_char_nl.restype = c_uint64
cookie_lib.cookie_put_char_fd.argtypes = [c_char, c_int]
cookie_lib.cookie_put_char_fd.restype = c_uint64
cookie_lib.cookie_put_char_fd_nl.argtypes = [c_char, c_int]
cookie_lib.cookie_put_char_fd_nl.restype = c_uint64

cookie_lib.cookie_put_str.argtypes = [c_char_p]
cookie_lib.cookie_put_str.restype = c_uint64
cookie_lib.cookie_put_str_nl.argtypes = [c_char_p]
cookie_lib.cookie_put_str_nl.restype = c_uint64
cookie_lib.cookie_put_str_fd.argtypes = [c_char_p, c_int]
cookie_lib.cookie_put_str_fd.restype = c_uint64
cookie_lib.cookie_put_str_fd_nl.argtypes = [c_char_p, c_int]
cookie_lib.cookie_put_str_fd_nl.restype = c_uint64

cookie_lib.cookie_strcmp.argtypes = [c_char_p, c_char_p]
cookie_lib.cookie_strcmp.restype = c_uint64
cookie_lib.cookie_strcmp_n.argtypes = [c_char_p, c_char_p, c_uint64]
cookie_lib.cookie_strcmp_n.restype = c_uint64

cookie_lib.cookie_str_dup.argtypes = [c_char_p]
cookie_lib.cookie_str_dup.restype = c_char_p

cookie_lib.cookie_strlen.argtypes = [c_char_p]
cookie_lib.cookie_strlen.restype = c_uint64

def putchar(c):
    return cookie_lib.cookie_put_char(c.encode("utf-8"))

def putchar_nl(c):
    return cookie_lib.cookie_put_char_nl(c.encode("utf-8"))

def putchar_fd(c, fd):
    return cookie_lib.cookie_put_char(c.encode("utf-8"), fd)

def putchar_fd_nl(c, fd):
    return cookie_lib.cookie_put_char_nl(c.encode("utf-8"), fd)

def putstr(s):
    return cookie_lib.cookie_put_str(s.encode("utf-8"))

def putstr_nl(s):
    return cookie_lib.cookie_put_str_nl(s.encode("utf-8"))

def putstr_fd(s, fd):
    return cookie_lib.cookie_put_str_fd(s.encode("utf-8"), fd)

def putstr_fd_nl(s, fd):
    return cookie_lib.cookie_put_str_fd_nl(s.encode("utf-8"), fd)

def strcmp(s1, s2):
    return cookie_lib.cookie_strcmp(s1.encode("utf-8"), s2.encode("utf-8"))

def strcmp_n(s1, s2, n):
    return cookie_lib.cookie_strcmp(s1.encode("utf-8"), s2.encode("utf-8"), n)

def strdup(s):
    return cookie_lib.cookie_str_dup(s.encode("utf-8"))

def strlen(s):
    return cookie_lib.cookie_strlen(s.encode("utf-8"))