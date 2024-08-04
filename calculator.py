# A simple lexer parser program for calculations
from enum import Enum

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'

class Token:
    def __init__(self, type, value) -> None:
        self.type = type # constants defined above
        self.value = value # token value

    def __str__(self) -> str:
        # prints string of instance
        return f"Token({type}, {value})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Interpreter:
    def __init__(self, expression) -> None:
        self.expression = expression
        self.position = 0 # index/pointer for expression evaluation
        self.current_character = self.expression[self.position]
        self.current_token = None

    def next(self) -> None:
        self.position += 1
        if self.position > len(self.expression) - 1:
            self.current_character = None # end of input
        else:
            self.current_character = self.expression[self.position]

    def skip_whitespace(self) -> None:
        while self.current_character.isspace() and self.current_character is not None:
            self.next()

    def integer(self) -> int:
        result = ''
        while self.current_character.isdigit() and self.current_character is not None:
            result += self.current_character
            self.next()
        return int(result)
    
    def error(self):
        raise Exception(">Parsing Error")
    
    def eat(self, token_type) -> None:
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def get_next_token(self) -> Token:
        # lexer method - decomposes string into tokens
        token_lookup = {
            "+": Token(PLUS, "+"),
            "-": Token(MINUS, "-"),
            "*": Token(MULTIPLY, "*"),
            "/": Token(DIVIDE, "/")
        }

        while self.current_character is not None:
            if self.current_character.isspace():
                self.skip_whitespace()
                continue

            if self.current_character.isdigit():
                return Token(INTEGER, self.integer())
            
            if token := token_lookup.get(self.current_character):
                self.next()
                token.position = self.position
                return token
            
            self.error()

        return Token(EOF, None)
    
    def evaluate(self) -> int:
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        operation = self.current_token
        if operation.type == PLUS:
            self.eat(PLUS)
        # pick things up from here  

