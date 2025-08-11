"""
Step 0:
    Supposed to make a lexer? and a parser?
    parser:
        as far as i have figured out its the conversion between json and python 
        as in how they can go back and forth between them 
        eg:
            json.load()

    must read a .json file
    
    should put out a code 0 for valid 
    should put out a code 1 for invalid

    report to standered output stream?:
        terminal in and out put
    
"""

import json
import os

def check_files():
    
    try:
        #valid_file = open(r"D:\_personal_stuff\_codingProjects\json_files\valid.json")
        #invalid_file = open(r"D:\_personal_stuff\_codingProjects\json_files\invalid.json")
        file_input = input().strip()

        with open(file_input,"r") as f:
            file = f"File has code: {check_if_valid(f)}"
        
    except FileNotFoundError:
        print("File not found")
    except OSError:
        print("couldnt open file")
    except:
        print(file)


def check_if_valid(file):
    try:
        json.load(file)
        return 0
    except json.JSONDecodeError as e:
        print(f"error: {e}")
        return 1

check_files()