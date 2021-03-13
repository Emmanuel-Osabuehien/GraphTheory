# Graph Theory Project 2021
# Author: Emmanuel Osabuehien
# Module: Graph Theory
# 30/04/2021

"""Creating a program that helps you search text files"""
"""I will be using regular expression wihtin this code"""

findText = []
with open('examplesText.txt') as find:
    findText = find.readlines()

count = 0
for text in findText:
    count += 1
    print(f'line {count}: {text}')
