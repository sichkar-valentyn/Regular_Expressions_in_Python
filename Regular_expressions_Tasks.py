# File: Regular_expressions_Tasks.py
# Description: Example on how to use regular expressions in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Example on how to use regular expressions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Regular_Expressions_in_Python (date of access: XX.XX.XXXX)


# Attention!
# Not to stuck in one of the task and run the task you need -
# - comment all other tasks you're not testing now

# Reading all strings one by one from standard input stream non-stop

import sys
import re

# Implementing the task 1
# Finding inclusions of 'cat' in the meaning of substring in the input string
# That meets at least two times
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'cat'
#     inclusions = re.findall(pattern, line)
#
#     if len(inclusions) >= 2:
#         print(line)


# Implementing the task 2
# Finding inclusions of 'cat' in the meaning of word in the input string
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'\bcat\b'
#     inclusions = re.findall(pattern, line)
#
#     match_object = re.match(pattern, line)
#
#     if len(inclusions) > 0:
#         print(line)
#
#     # Or we can use function 'match'
#
#     if match_object != 'None':
#         print(line)


# Implementing task 3
# Finding inclusions of three symbols between z and z
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'z[\w]{3}z'
#     inclusions = re.findall(pattern, line)
#
#     match_object = re.match(pattern, line)
#
#     if len(inclusions) > 0:
#         print(line)
#
#     # Or we can use function 'match'
#
#     if match_object != None:
#         print(line)


# Implementing task 4
# Finding inclusions of back-slash \ in the sinput string
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'\\'
#     inclusions = re.findall(pattern, line)
#
#     match_object = re.match(pattern, line)
#
#     if len(inclusions) > 0:
#         print(line)
#
#     # Or we can use function 'match'
#
#     if match_object != None:
#         print(line)


# Implementing task 5
# Finding inclusions of word that consists of two equal parts
# blabla
# testtest
# 123123
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'\b(\w+)\1\b'
#     inclusions = re.findall(pattern, line)
#
#     match_object = re.match(pattern, line)
#
#     search_object = re.search(pattern, line)
#
#     if len(inclusions) > 0:
#         print(line)
#
#     # Or we can use function 'match'
#
#     if match_object != None:
#         print(line)
#
#     # Or we can use function 'search'
#
#     if search_object != None:
#         print(line)


# Implementing task 6
# Replacing all inclusions of substring 'human' to substring 'computer'
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'human'
#     replace = re.sub(pattern, 'computer', line)
#
#     print(replace)


# Implementing task 7
# Replacing first found word that consists only with letters 'a' with no metters of case
# by 'argh'
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'\ba+\b'
#     replace = re.sub(pattern, 'argh', line, count=1, flags=re.IGNORECASE)
#
#     print(replace)


# Implementing task 8
# Changing positions of two first letters with each other in the all words
# for line in sys.stdin:
#     line = line.rstrip()
#
#     pattern = r'\b(\w)(\w)(\w*)\b'
#     fixed = re.sub(pattern, r'\2\1\3', line)
#
#     print(fixed)


# Implementing task 9
# Deleting duplicates of the letters in one letter
for line in sys.stdin:
    line = line.rstrip()

    pattern = r'(\w)(\1)+'
    duplicates = re.sub(pattern, r'\1', line)

    print(duplicates)
