#!/usr/bin/env python3

import re
import sys

def func_finder(line):
    pattern = r'\b(\w+)\([^)]*\)'
    match = re.search(pattern, line)
    if match:
        return match.group(1)

def allowed_funcs(filename):
    allowed = []
    with open(filename) as file:
        while line := file.readline():
            funcs = line.rstrip().split(", ")
            for func in funcs:
                allowed.append(func.split(",")[0])
    return (allowed)

def interdit(filename):
    print(f"{filename}: Error!")
    allowed = ['ft_isalpha', 'ft_isdigit', 'ft_isalnum', 'ft_isascii', 'ft_isprint', 'ft_strlen', 'ft_memset', 'ft_bzero', 'ft_memcpy', 'ft_memmove', 'ft_strlcpy', 'ft_strlcat', 'ft_toupper', 'ft_tolower', 'ft_strchr', 'ft_strrchr', 'ft_strncmp', 'ft_memchr', 'ft_memcmp', 'ft_strnstr', 'ft_atoi', 'ft_strdup', 'ft_calloc', 'ft_substr', 'ft_strjoin', 'ft_strtrim', 'ft_split', 'ft_itoa', 'ft_strmapi', 'ft_striteri', 'ft_putchar_fd', 'ft_putstr_fd', 'ft_putendl_fd', 'ft_putnbr_fd', 'ft_lstnew', 'ft_lstadd_front', 'ft_lstsize', 'ft_lstlast', 'ft_lstadd_back', 'ft_lstdelone', 'ft_lstclear', 'ft_lstiter', 'ft_lstmap', 'ft_printf', 'get_next_line', 'free_strs', 'ft_printf_fd', 'handle_error', 'ft_swap']
    for each in ['open', 'close', 'read', 'write', 'malloc', 'free', 'perror', 'strerror', 'exit']:
        allowed.append(each)
    allowed.append("main")
    forbidden = []
    with open(filename) as file:
        i = 1
        forbidden_func = None
        while line := file.readline():
            forbidden_func = func_finder(line.rstrip())
            if forbidden_func and forbidden_func not in allowed:
                forbidden.append(forbidden_func)
                print("Error: FORBIDDEN_FUNC    ", end="")
                print(f"(line:   {i}):  Used forbidden function:    ", end="")
                print(forbidden_func)
            i += 1

for each in sys.argv[1:]:
    interdit(each)
