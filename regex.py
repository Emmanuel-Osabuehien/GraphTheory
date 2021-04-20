# Graph Theory Project 2021
# Author: Emmanuel Osabuehien
# Module: Graph Theory
# 30/04/2021

import argparse

"""Creating a program that helps you search text files"""
"""I will be using regular expression wihtin this code"""

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

findText = open("randomtext2.txt")
find = findText.read()         
findText.close()                  
print(find)      

