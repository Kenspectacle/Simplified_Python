from enum import Enum
import re

class Tokenizer:
    def __init__(self):
        self.math_symbols = ["(", "+", ")", "="]
        
    def tokenize(self, input: str) -> list: 
        tokens = []
        
        def check_integer(input, pos) -> (int, int):
            integer_string = ""
            while input[pos].isdigit():
                integer_string += input[pos]
                pos += 1
            integer = int(integer_string)
            return integer, pos

        def check_identifier(input, pos) -> (str, int):
            identifier = ""
            while input[pos].isalpha() or input[pos].isdigit():
                identifier += input[pos]
                pos += 1
            return identifier, pos
        
        pos = 0
        limiter = 0
        while pos < len(input) and limiter < 15:
            print(input[pos], tokens)
            print(input[pos + 1])
            # ignore white space and next line
            if input[pos] == " " or input[pos] == "\n":
                pos += 1
                continue
            # check for integer
            if input[pos].isdigit():
                current_int, pos = check_integer(input, pos)
                tokens.append(current_int)
            # check print
            if input[pos:pos + 5] == 'print':
                pos += 5
                tokens.append('Print')
            # check ID
            if input[pos].isalpha():
                current_identifier, pos = check_identifier(input, pos)
                tokens.append(current_identifier)
            # check math symbols
            if input[pos] in self.math_symbols:
                tokens.append(input[pos])
                pos += 1
            # semi colon
            if input[pos] == ';':
                tokens.append(';')
                pos += 1
            limiter += 1
        return tokens
        
        