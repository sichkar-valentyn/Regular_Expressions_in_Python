# File: Regular_expressions.py
# Description: Example on how to use regular expressions in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Example on how to use regular expressions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Regular_Expressions_in_Python (date of access: XX.XX.XXXX)


# Importing module 're' to match some pattern to the string or text
# Considering four functions in the module
# match, search, findall, sub
# Considering meta-symbols

import re

# match function
pattern = r'abc'
string = 'abcd'
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='abc'>

# [] -- it is possible to write set of symbols in it
pattern = r'a[abc]c'  # Here we specify that the second symbol can be one from [] - a, b or c
string = 'abcd'  # Also, ab, ac will match
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='abc'>

# search function
string = 'babcd'
match_object = re.search(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(1, 4), match='abc'>

# findall function
string = 'abc, acc, aac'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abc', 'acc', 'aac']

# sub function
fixed_typos = re.sub(pattern, 'abc', string)  # Here we changed all matches to the string 'abc'
print(fixed_typos)  # abc, abc, abc

# If we want to find the question mark, we need to put backslash before
pattern = r' English\?'
string = 'Do you speak English?'
match = re.search(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(12, 21), match=' English?'>

# Question mark and other special symbols are using for regular expressions
# They are called meta-symbols
# . ^ $ * + ? { } \ | ( )
pattern = r'a[a-c]c'  # Range of letters between a to c
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='acc'>

string = 'abc, acc, aac'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abc', 'acc', 'aac']

fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)  # abc, abc, abc

# Letters that we don't want to count with meta-symbol ^
pattern = r'a[^a-c]c'
string = 'a.c'
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='a.c'>

# There are short forms to write the meta-symbols
# \d - [0-9]
# \D - [^0-9]
# \s - [ \t\n\r\f\v]
# \S - [^ \t\n\r\f\v]
# \w - [a-zA-Z0-9_]
# \W - [^a-zA-Z0-0_]

pattern = r'a\wc'  # looking for all letters and numbers by \w
# pattern = r'a[\w.]c'  # looking for all letters and numbers plus dot
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='acc'>

string = 'abc, a.c, aac, a-c, aBc, azc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abc', 'aac', 'aBc', 'azc']

# By using only dot we will find any symbol between a and c
pattern = r'a.c'  # any symbol between a and c
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)  # <_sre.SRE_Match object; span=(0, 3), match='acc'>

string = 'abc, a.c, aac, a-c, aBc, azc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abc', 'a.c', 'aac', 'a-c', 'aBc', 'azc']

# Also, there is possible to specify number of symbols we need to be counted
# In this case we use meta-symbol '*'
pattern = r'ab*a'  # We want any number of b, even 0 - no b, b, bb, bbb, etc
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba', 'abba']

# If we want only positive number of inclusions, we can write meta-symbol '+'
pattern = r'ab+a'  # We want any number of 'b' starting from 1
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aba', 'abba']

# By using meta-symbol '?' we specify that we need only 0 or 1 of the inclusions
pattern = r'ab?a'  # We want only 0 or 1 inclusion of letter 'b'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba']

# If we want to specify number of inclusions we use '{3}'
pattern = r'ab{3}a'  # We specify that number of letters 'b' has to be '{3}'
# To specify the interval we have to write '{2,3}'
string = 'aa, aba, abba, abbba, abbbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abbba']

# Also, it is possible to group symbols and repeat them
# In this case we use meta-symbol '()' and add '*':
pattern = r'(test)*'
string = 'testtest'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 8), match='testtest'>

# We use symbol '|' in square brackets to show groups of symbols to choose from
pattern = r'(test|text)*'
string = 'testtext'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 8), match='testtext'>

# More complex usage of meta-symbol '|'
pattern = r'abc|(test|text)*'
string = 'abc'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 3), match='abc'>

# Showing the groups with function 'match'
pattern = r'((abc)|(test|text)*)'
string = 'abc'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 3), match='abc'>
print(match.groups())  # ('abc', 'abc', None)

# More complex example with using groups
pattern = r'Hello (abc|test)'
string = 'Hello abc'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 9), match='Hello abc'>
print(match.group(0))  # Hello abc
print(match.group(1))  # abc

# Another example by using group number inside the pattern
pattern = r'(\w+)-\1'  # We say here - any letters and numbers (at least one by putting '+')
                       # And after the dash - the first group it'll find (by '\1')
string = 'test-test'
match = re.match(pattern, string)
print(match)  # <_sre.SRE_Match object; span=(0, 9), match='test-test'>

# The same example but using the function 'sub'
pattern = r'(\w+)-\1'
string = r'test-test chow-chow'
duplicates = re.sub(pattern, r'\1', string)  # We replace duplicates by first group
print(duplicates)  # test chow

# By using the function 'findall' we'll get the tuple of groups
pattern = r'(\w+)-\1'
string = r'test-test chow-chow'
duplicates = re.findall(pattern, string)
print(duplicates)  # ['test', 'chow']

# Another, more complex example with function 'findall'
pattern = r'((\w+)-\2)'
string = r'test-test chow-chow'
duplicates = re.findall(pattern, string)
print(duplicates)  # [('test-test', 'test'), ('chow-chow', 'chow')]

# To ignore the case of the letters we need to specify it by flag
x = re.match(r'text', 'TEXT', re.IGNORECASE)
print(x)  # <_sre.SRE_Match object; span=(0, 4), match='TEXT'>

# Another, more complex example with flags
x = re.match(r'(te)*xt', 'TEXT', re.IGNORECASE | re.DEBUG)
print(x)  # MAX_REPEAT 0 MAXREPEAT
          #   SUBPATTERN 1
          #     LITERAL 116
          #     LITERAL 101
          # LITERAL 120
          # LITERAL 116
          # <_sre.SRE_Match object; span=(0, 4), match='TEXT'>
