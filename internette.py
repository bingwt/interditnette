#!/usr/bin/env python3

import re
import sys

allowed = ['ft_isalpha', 'ft_isdigit', 'ft_isalnum', 'ft_isascii', 'ft_isprint', 'ft_strlen', 'ft_memset', 'ft_bzero', 'ft_memcpy', 'ft_memmove', 'ft_strlcpy', 'ft_strlcat', 'ft_toupper', 'ft_tolower', 'ft_strchr', 'ft_strrchr', 'ft_strncmp', 'ft_memchr', 'ft_memcmp', 'ft_strnstr', 'ft_atoi', 'ft_strdup', 'ft_calloc', 'ft_substr', 'ft_strjoin', 'ft_strtrim', 'ft_split', 'ft_itoa', 'ft_strmapi', 'ft_striteri', 'ft_putchar_fd', 'ft_putstr_fd', 'ft_putendl_fd', 'ft_putnbr_fd', 'ft_lstnew', 'ft_lstadd_front', 'ft_lstsize', 'ft_lstlast', 'ft_lstadd_back', 'ft_lstdelone', 'ft_lstclear', 'ft_lstiter', 'ft_lstmap', 'ft_printf', 'get_next_line', 'free_strs', 'ft_printf_fd', 'handle_error', 'ft_swap']

def func_def(line):
    pattern = r'\b\w+\s+[*]*?(\w+)\([^)]*\)'
    match = re.search(pattern, line)
    if match:
        return match.group(1)

def func_use(line):
    pattern = r'\b(\w+)\([^)]*\)'
    match = re.search(pattern, line)
    if match:
        return match.group(1)

def func_permise(filename):
    with open(filename) as file:
        while line := file.readline():
            funcs = line.rstrip().split(", ")
            for func in funcs:
                allowed.append(func.split(",")[0])

def permise(filename):
    with open(filename) as file:
        i = 1
        allowed_func = None
        while line := file.readline():
            allowed_func = func_def(line.rstrip())
            if allowed_func:
                allowed.append(allowed_func)

def interdit(filename):
    p_flag = 0
    for each in ['open', 'close', 'read', 'write', 'malloc', 'free', 'perror', 'strerror', 'exit']:
        allowed.append(each)
    allowed.append("main")
    forbidden = []
    with open(filename) as file:
        i = 1
        forbidden_func = None
        while line := file.readline():
            if len(forbidden) == 1 and not p_flag:
                print(f"{filename}: Error!")
                p_flag = 1
            forbidden_func = func_use(line.rstrip())
            if forbidden_func and forbidden_func not in allowed:
                forbidden.append(forbidden_func)
                print("Error: FORBIDDEN_FUNC    ", end="")
                print(f"(line:   {i}):  Used forbidden function:    ", end="")
                print(forbidden_func)
            i += 1
        if not len(forbidden):
            print(f"{filename}: OK!")

for each in sys.argv[1:]:
    if each.endswith(".permise"):
        func_permise(each)
    permise(each)
for each in sys.argv[1:]:
    interdit(each)
