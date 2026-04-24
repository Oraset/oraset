#!/usr/bin/env python3

import sys

class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type}, {repr(self.value)}, {self.line}, {self.column})"

class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
    
    def get_next_token(self):
        while self.position < len(self.source):
            char = self.source[self.position]
            
            # Skip whitespace
            if char.isspace():
                if char == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1
                self.position += 1
                continue
            
            # Skip comments (!! for single line, !* ... *! for multi-line)
            if char == '!' and self.position + 1 < len(self.source):
                # Check for single-line comment (!!)
                if self.source[self.position + 1] == '!':
                    self.position += 2
                    self.column += 2
                    while self.position < len(self.source) and self.source[self.position] != '\n':
                        self.position += 1
                        self.column += 1
                    continue
                # Check for multi-line comment (!* ... *!)
                elif self.source[self.position + 1] == '*':
                    self.position += 2
                    self.column += 2
                    # Skip until closing *!
                    while self.position + 1 < len(self.source) and not (self.source[self.position] == '*' and self.source[self.position + 1] == '!'):
                        if self.source[self.position] == '\n':
                            self.line += 1
                            self.column = 1
                        else:
                            self.column += 1
                        self.position += 1
                    if self.position + 1 < len(self.source):
                        self.position += 2
                        self.column += 2
                    continue
            # Include directive
            elif char == '!' and self.position + 7 < len(self.source) and self.source[self.position:self.position+8] == '!include':
                self.position += 8
                self.column += 8
                # Skip whitespace
                while self.position < len(self.source) and self.source[self.position].isspace():
                    self.position += 1
                    self.column += 1
                # Read module name in quotes
                if self.position < len(self.source) and self.source[self.position] == "'":
                    self.position += 1
                    self.column += 1
                    start = self.position
                    while self.position < len(self.source) and self.source[self.position] != "'":
                        self.position += 1
                        self.column += 1
                    if self.position < len(self.source):
                        self.position += 1
                        self.column += 1
                    module = self.source[start:self.position-1]
                    return Token('INCLUDE_DIRECTIVE', module, self.line, self.column - len(module) - 2)
            
            # String literal
            if char == '`':
                start = self.position
                self.position += 1
                self.column += 1
                value = ''
                while self.position < len(self.source) and self.source[self.position] != '`':
                    if self.source[self.position] == '\\':
                        # Handle escape sequences
                        self.position += 1
                        self.column += 1
                        if self.position < len(self.source):
                            if self.source[self.position] == 'n':
                                value += '\n'
                            elif self.source[self.position] == 't':
                                value += '\t'
                            elif self.source[self.position] == 'r':
                                value += '\r'
                            elif self.source[self.position] == '\\':
                                value += '\\'
                            elif self.source[self.position] == '`':
                                value += '`'
                            else:
                                # Unknown escape sequence, just add the character
                                value += self.source[self.position]
                            self.position += 1
                            self.column += 1
                    elif self.source[self.position] == '\n':
                        value += '\n'
                        self.line += 1
                        self.column = 1
                        self.position += 1
                    else:
                        value += self.source[self.position]
                        self.column += 1
                        self.position += 1
                if self.position < len(self.source):
                    self.position += 1
                    self.column += 1
                return Token('STRING', value, self.line, self.column - len(value) - 2)
            
            # Negative number
            if char == '-' and self.position + 1 < len(self.source) and self.source[self.position + 1].isdigit():
                start = self.position
                self.position += 1
                self.column += 1
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    self.position += 1
                    self.column += 1
                value = self.source[start:self.position]
                return Token('INT', value, self.line, self.column - len(value))
            # Number
            elif char.isdigit():
                start = self.position
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    self.position += 1
                    self.column += 1
                value = self.source[start:self.position]
                return Token('INT', value, self.line, self.column - len(value))
            
            # Identifier or keyword
            if char.isalpha() or char == '_':
                start = self.position
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                    self.position += 1
                    self.column += 1
                value = self.source[start:self.position]
                if value == 'show':
                    return Token('KEYWORD_SHOW', value, self.line, self.column - len(value))
                elif value == 'if':
                    return Token('KEYWORD_IF', value, self.line, self.column - len(value))
                elif value == 'else':
                    return Token('KEYWORD_ELSE', value, self.line, self.column - len(value))
                elif value == 'while':
                    return Token('KEYWORD_WHILE', value, self.line, self.column - len(value))
                elif value == 'def':
                    return Token('KEYWORD_DEF', value, self.line, self.column - len(value))
                elif value == 'class':
                    return Token('KEYWORD_CLASS', value, self.line, self.column - len(value))
                elif value == 'return':
                    return Token('KEYWORD_RETURN', value, self.line, self.column - len(value))
                elif value == 'import':
                    return Token('KEYWORD_IMPORT', value, self.line, self.column - len(value))
                else:
                    return Token('IDENTIFIER', value, self.line, self.column - len(value))
            
            # Operators and punctuation
            if char == '+' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '+':
                self.position += 2
                self.column += 2
                return Token('PLUS_PLUS', '++', self.line, self.column - 2)
            elif char == '-' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '-':
                self.position += 2
                self.column += 2
                return Token('MINUS_MINUS', '--', self.line, self.column - 2)
            elif char == '+' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('PLUS_EQUALS', '+=', self.line, self.column - 2)
            elif char == '-' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('MINUS_EQUALS', '-=', self.line, self.column - 2)
            elif char == '*' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('MULTIPLY_EQUALS', '*=', self.line, self.column - 2)
            elif char == '/' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('DIVIDE_EQUALS', '/=', self.line, self.column - 2)
            elif char == '=' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('EQUALS', '==', self.line, self.column - 2)
            elif char == '=':
                self.position += 1
                self.column += 1
                return Token('ASSIGN', '=', self.line, self.column - 1)
            elif char == '!' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('NOT_EQUALS', '!=', self.line, self.column - 2)
            elif char == '@':
                self.position += 1
                self.column += 1
                return Token('AT', '@', self.line, self.column - 1)
            elif char == '.':
                self.position += 1
                self.column += 1
                return Token('DOT', '.', self.line, self.column - 1)
            elif char == '<' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('LESS_EQUAL', '<=', self.line, self.column - 2)
            elif char == '>' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '=':
                self.position += 2
                self.column += 2
                return Token('GREATER_EQUAL', '>=', self.line, self.column - 2)
            elif char == '&' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '&':
                self.position += 2
                self.column += 2
                return Token('AND', '&&', self.line, self.column - 2)
            elif char == '|' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '|':
                self.position += 2
                self.column += 2
                return Token('OR', '||', self.line, self.column - 2)
            elif char == '@':
                # Check if it's an include directive
                if self.position + 7 < len(self.source) and self.source[self.position+1:self.position+8] == 'include':
                    # It's an include directive
                    # Move past '@include'
                    self.position += 8
                    self.column += 8
                    # Skip whitespace after include
                    while self.position < len(self.source) and self.source[self.position].isspace():
                        self.position += 1
                        self.column += 1
                    # Get the module name
                    if self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position] == '_'):
                        start = self.position
                        while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                            self.position += 1
                        module_name = self.source[start:self.position]
                        self.column += len(module_name)
                        return Token('INCLUDE_DIRECTIVE', module_name, self.line, self.column - len(module_name))
                # Otherwise, it's an unknown token
                self.position += 1
                self.column += 1
            elif char == '!':
                # It's a NOT operator
                self.position += 1
                self.column += 1
                return Token('NOT', '!', self.line, self.column - 1)
            elif char == '+':
                self.position += 1
                self.column += 1
                return Token('PLUS', '+', self.line, self.column - 1)
            elif char == '-':
                self.position += 1
                self.column += 1
                return Token('MINUS', '-', self.line, self.column - 1)
            elif char == '*':
                self.position += 1
                self.column += 1
                return Token('MULTIPLY', '*', self.line, self.column - 1)
            elif char == '/':
                self.position += 1
                self.column += 1
                return Token('DIVIDE', '/', self.line, self.column - 1)
            elif char == '=':
                self.position += 1
                self.column += 1
                return Token('ASSIGN', '=', self.line, self.column - 1)
            elif char == '<':
                self.position += 1
                self.column += 1
                return Token('LESS', '<', self.line, self.column - 1)
            elif char == '>':
                self.position += 1
                self.column += 1
                return Token('GREATER', '>', self.line, self.column - 1)
            elif char == '(':
                self.position += 1
                self.column += 1
                return Token('LPAREN', '(', self.line, self.column - 1)
            elif char == ')':
                self.position += 1
                self.column += 1
                return Token('RPAREN', ')', self.line, self.column - 1)
            elif char == ';':
                self.position += 1
                self.column += 1
                return Token('SEMICOLON', ';', self.line, self.column - 1)
            elif char == ',':
                self.position += 1
                self.column += 1
                return Token('COMMA', ',', self.line, self.column - 1)
            elif char == '{':
                self.position += 1
                self.column += 1
                return Token('LBRACE', '{', self.line, self.column - 1)
            elif char == '}':
                self.position += 1
                self.column += 1
                return Token('RBRACE', '}', self.line, self.column - 1)
            elif char == '[':
                self.position += 1
                self.column += 1
                return Token('LBRACKET', '[', self.line, self.column - 1)
            elif char == ']':
                self.position += 1
                self.column += 1
                return Token('RBRACKET', ']', self.line, self.column - 1)
            
            # Unknown character
            self.position += 1
            self.column += 1
        
        return Token('EOF', None, self.line, self.column)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self, message):
        # For Windows PowerShell compatibility, use simple error messages without ANSI codes
        error_msg = f"Syntax Error at line {self.current_token.line}, column {self.current_token.column}: {message}"
        # Add more context information
        if hasattr(self.lexer, 'source'):
            # Get the line where the error occurred
            lines = self.lexer.source.split('\n')
            if self.current_token.line - 1 < len(lines):
                error_line = lines[self.current_token.line - 1]
                # Add the error line to the error message
                error_msg += f"\nLine {self.current_token.line}: {error_line}"
                # Add a pointer to the error position
                error_msg += f"\n" + ' ' * (len(f"Line {self.current_token.line}: ") + self.current_token.column - 1) + "^"
        # Add specific error messages for common errors
        if "Expected SEMICOLON" in message:
            error_msg += "\nHint: Missing semicolon at the end of the statement."
        elif "Expected LPAREN" in message:
            error_msg += "\nHint: Missing opening parenthesis '('."
        elif "Expected RPAREN" in message:
            error_msg += "\nHint: Missing closing parenthesis ')'."
        elif "Expected LBRACE" in message:
            error_msg += "\nHint: Missing opening brace '{'."
        elif "Expected RBRACE" in message:
            error_msg += "\nHint: Missing closing brace '}'."
        raise Exception(error_msg)
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type}, got {self.current_token.type}")
    
    def factor(self):
        token = self.current_token
        if token.type == 'INT':
            self.eat('INT')
            return {'type': 'literal', 'value': token.value}
        elif token.type == 'STRING':
            self.eat('STRING')
            return {'type': 'literal', 'value': token.value}
        elif token.type == 'IDENTIFIER':
            # Check if it's a function call or array index
            save_position = self.lexer.position
            save_line = self.lexer.line
            save_column = self.lexer.column
            
            # Look ahead to see if it's a function call or array index
            is_function_call = False
            is_array_index = False
            pos = save_position
            while pos < len(self.lexer.source) and self.lexer.source[pos].isspace():
                pos += 1
            if pos < len(self.lexer.source):
                if self.lexer.source[pos] == '(':
                    is_function_call = True
                elif self.lexer.source[pos] == '[':
                    is_array_index = True
                elif self.lexer.source[pos] == '.':
                    # Handle dot notation (e.g., math.abs)
                    is_function_call = True
            
            # Restore the lexer position
            self.lexer.position = save_position
            self.lexer.line = save_line
            self.lexer.column = save_column
            
            if is_function_call:
                # It's a function call (could be with dot notation)
                name = self.current_token.value
                self.eat('IDENTIFIER')
                
                # Handle dot notation
                while self.current_token.type == 'DOT':
                    self.eat('DOT')
                    name += '.' + self.current_token.value
                    self.eat('IDENTIFIER')
                
                self.eat('LPAREN')
                arguments = []
                if self.current_token.type != 'RPAREN':
                    arguments.append(self.expression())
                    while self.current_token.type == 'COMMA':
                        self.eat('COMMA')
                        arguments.append(self.expression())
                self.eat('RPAREN')
                return {
                    'type': 'function_call',
                    'name': name,
                    'arguments': arguments
                }
            elif is_array_index:
                # It's an array index
                name = self.current_token.value
                self.eat('IDENTIFIER')
                self.eat('LBRACKET')
                index = self.expression()
                self.eat('RBRACKET')
                return {
                    'type': 'array_index',
                    'name': name,
                    'index': index
                }
            else:
                # It's a simple identifier
                self.eat('IDENTIFIER')
                return {'type': 'identifier', 'name': token.value}
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            return expr
        else:
            self.error(f"Unexpected token {token.type}")
    
    def statement(self):
        if self.current_token.type == 'INCLUDE_DIRECTIVE':
            return self.include_directive()
        elif self.current_token.type == 'KEYWORD_SHOW':
            return self.function_call()
        elif self.current_token.type == 'KEYWORD_IF':
            return self.if_statement()
        elif self.current_token.type == 'KEYWORD_WHILE':
            return self.while_statement()
        elif self.current_token.type == 'KEYWORD_DEF':
            return self.def_statement()
        elif self.current_token.type == 'KEYWORD_CLASS':
            return self.class_statement()
        elif self.current_token.type == 'KEYWORD_RETURN':
            return self.return_statement()
        elif self.current_token.type == 'KEYWORD_IMPORT':
            return self.import_statement()
        elif self.current_token.type == 'AT':
            return self.import_statement()
        elif self.current_token.type == 'IDENTIFIER':
            # Check if it's a function call by looking ahead
            # We need to save the current position first
            save_position = self.lexer.position
            save_line = self.lexer.line
            save_column = self.lexer.column
            
            # Look ahead to see if it's a function call
            is_function_call = False
            pos = save_position
            while pos < len(self.lexer.source) and self.lexer.source[pos].isspace():
                pos += 1
            if pos < len(self.lexer.source) and self.lexer.source[pos] == '(':
                is_function_call = True
            
            # Restore the lexer position
            self.lexer.position = save_position
            self.lexer.line = save_line
            self.lexer.column = save_column
            
            if is_function_call:
                # It's a function call (handled in factor)
                # The function call is already parsed as part of the expression
                # So we just need to parse the expression and add a semicolon
                expr = self.expression()
                self.eat('SEMICOLON')
                return expr
            else:
                # It's an assignment
                return self.assignment()
        else:
            self.error(f"Unexpected token {self.current_token.type}")
    
    def term(self):
        node = self.factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
            else:
                self.eat('DIVIDE')
            node = {
                'type': 'binary_op',
                'op': token.value,
                'left': node,
                'right': self.factor()
            }
        return node
    
    def expression(self):
        node = self.logical_or()
        return node
    
    def logical_or(self):
        node = self.logical_and()
        while self.current_token.type == 'OR':
            token = self.current_token
            self.eat('OR')
            node = {
                'type': 'binary_op',
                'op': token.value,
                'left': node,
                'right': self.logical_and()
            }
        return node
    
    def logical_and(self):
        node = self.equality()
        while self.current_token.type == 'AND':
            token = self.current_token
            self.eat('AND')
            node = {
                'type': 'binary_op',
                'op': token.value,
                'left': node,
                'right': self.equality()
            }
        return node
    
    def equality(self):
        node = self.comparison()
        while self.current_token.type in ('EQUALS', 'NOT_EQUALS'):
            token = self.current_token
            if token.type == 'EQUALS':
                self.eat('EQUALS')
            else:
                self.eat('NOT_EQUALS')
            node = {
                'type': 'binary_op',
                'op': token.value,
                'left': node,
                'right': self.comparison()
            }
        return node
    
    def comparison(self):
        node = self.term()
        while self.current_token.type in ('PLUS', 'MINUS', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            elif token.type == 'LESS':
                self.eat('LESS')
            elif token.type == 'LESS_EQUAL':
                self.eat('LESS_EQUAL')
            elif token.type == 'GREATER':
                self.eat('GREATER')
            else:
                self.eat('GREATER_EQUAL')
            node = {
                'type': 'binary_op',
                'op': token.value,
                'left': node,
                'right': self.term()
            }
        return node
    
    def assignment(self):
        token = self.current_token
        self.eat('IDENTIFIER')
        if self.current_token.type == 'ASSIGN':
            self.eat('ASSIGN')
            value = self.expression()
            # Check if there's a semicolon, but don't require it
            if self.current_token.type == 'SEMICOLON':
                self.eat('SEMICOLON')
            return {
                'type': 'assignment',
                'name': token.value,
                'value': value
            }
        elif self.current_token.type in ('PLUS_EQUALS', 'MINUS_EQUALS', 'MULTIPLY_EQUALS', 'DIVIDE_EQUALS'):
            op_token = self.current_token
            if op_token.type == 'PLUS_EQUALS':
                self.eat('PLUS_EQUALS')
            elif op_token.type == 'MINUS_EQUALS':
                self.eat('MINUS_EQUALS')
            elif op_token.type == 'MULTIPLY_EQUALS':
                self.eat('MULTIPLY_EQUALS')
            else:
                self.eat('DIVIDE_EQUALS')
            value = self.expression()
            # Check if there's a semicolon, but don't require it
            if self.current_token.type == 'SEMICOLON':
                self.eat('SEMICOLON')
            # Create compound assignment as binary operation
            compound_op = op_token.value[0]  # Get the first character (e.g., '+' from '+=')
            return {
                'type': 'assignment',
                'name': token.value,
                'value': {
                    'type': 'binary_op',
                    'op': compound_op,
                    'left': {'type': 'identifier', 'name': token.value},
                    'right': value
                }
            }
        else:
            self.error(f"Expected assignment operator, got {self.current_token.type}")
    
    def function_call(self):
        token = self.current_token
        self.eat('KEYWORD_SHOW')
        self.eat('LPAREN')
        arguments = []
        if self.current_token.type != 'RPAREN':
            arguments.append(self.expression())
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                arguments.append(self.expression())
        self.eat('RPAREN')
        # Check if there's a semicolon, but don't require it
        if self.current_token.type == 'SEMICOLON':
            self.eat('SEMICOLON')
        return {
            'type': 'function_call',
            'name': token.value,
            'arguments': arguments
        }
    
    def block(self):
        self.eat('LBRACE')
        statements = []
        while self.current_token.type != 'RBRACE' and self.current_token.type != 'EOF':
            statements.append(self.statement())
        self.eat('RBRACE')
        return {'type': 'block', 'statements': statements}
    
    def if_statement(self):
        self.eat('KEYWORD_IF')
        self.eat('LPAREN')
        condition = self.expression()
        self.eat('RPAREN')
        then_branch = self.block()
        else_branch = None
        
        if self.current_token.type == 'KEYWORD_ELSE':
            self.eat('KEYWORD_ELSE')
            if self.current_token.type == 'KEYWORD_IF':
                else_branch = self.if_statement()
            else:
                else_branch = self.block()
        
        return {
            'type': 'if_statement',
            'condition': condition,
            'then_branch': then_branch,
            'else_branch': else_branch
        }
    
    def while_statement(self):
        self.eat('KEYWORD_WHILE')
        self.eat('LPAREN')
        condition = self.expression()
        self.eat('RPAREN')
        body = self.block()
        return {
            'type': 'while_statement',
            'condition': condition,
            'body': body
        }
    
    def return_statement(self):
        self.eat('KEYWORD_RETURN')
        value = self.expression()
        # 检查是否需要分号（在函数体中可能不需要分号）
        if self.current_token.type == 'SEMICOLON':
            self.eat('SEMICOLON')
        return {
            'type': 'return_statement',
            'value': value
        }
    
    def def_statement(self):
        self.eat('KEYWORD_DEF')
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('LPAREN')
        parameters = []
        if self.current_token.type != 'RPAREN':
            parameters.append(self.current_token.value)
            self.eat('IDENTIFIER')
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                parameters.append(self.current_token.value)
                self.eat('IDENTIFIER')
        self.eat('RPAREN')
        body = self.block()
        return {
            'type': 'def_statement',
            'name': name,
            'parameters': parameters,
            'body': body
        }
    
    def import_statement(self):
        # Handle both @library and import library syntax
        if self.current_token.type == 'AT':
            self.eat('AT')
        elif self.current_token.type == 'KEYWORD_IMPORT':
            self.eat('KEYWORD_IMPORT')
        module = self.current_token.value
        self.eat('IDENTIFIER')
        # Check if there's a semicolon, but don't require it
        if self.current_token.type == 'SEMICOLON':
            self.eat('SEMICOLON')
        return {
            'type': 'import_statement',
            'module': module
        }
    
    def include_directive(self):
        module = self.current_token.value
        self.eat('INCLUDE_DIRECTIVE')
        # Check if there's a semicolon, but don't require it
        if self.current_token.type == 'SEMICOLON':
            self.eat('SEMICOLON')
        return {
            'type': 'include_directive',
            'module': module
        }
    
    def class_statement(self):
        self.eat('KEYWORD_CLASS')
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('LBRACE')
        methods = []
        while self.current_token.type != 'RBRACE' and self.current_token.type != 'EOF':
            if self.current_token.type == 'KEYWORD_DEF':
                methods.append(self.def_statement())
            else:
                self.error(f"Expected function definition in class, got {self.current_token.type}")
        self.eat('RBRACE')
        return {
            'type': 'class_statement',
            'name': name,
            'methods': methods
        }
    
    def statement(self):
        if self.current_token.type == 'INCLUDE_DIRECTIVE':
            return self.include_directive()
        elif self.current_token.type == 'KEYWORD_SHOW':
            return self.function_call()
        elif self.current_token.type == 'KEYWORD_IF':
            return self.if_statement()
        elif self.current_token.type == 'KEYWORD_WHILE':
            return self.while_statement()
        elif self.current_token.type == 'KEYWORD_DEF':
            return self.def_statement()
        elif self.current_token.type == 'KEYWORD_CLASS':
            return self.class_statement()
        elif self.current_token.type == 'KEYWORD_RETURN':
            return self.return_statement()
        elif self.current_token.type == 'KEYWORD_IMPORT':
            return self.import_statement()
        elif self.current_token.type == 'AT':
            return self.import_statement()
        elif self.current_token.type == 'IDENTIFIER':
            # Check if it's a function call
            if self.lexer.position + 1 < len(self.lexer.source) and self.lexer.source[self.lexer.position] == '(':
                # It's a function call
                name = self.current_token.value
                self.eat('IDENTIFIER')
                self.eat('LPAREN')
                arguments = []
                if self.current_token.type != 'RPAREN':
                    arguments.append(self.expression())
                    while self.current_token.type == 'COMMA':
                        self.eat('COMMA')
                        arguments.append(self.expression())
                self.eat('RPAREN')
                self.eat('SEMICOLON')
                return {
                    'type': 'function_call',
                    'name': name,
                    'arguments': arguments
                }
            else:
                # It's an assignment
                return self.assignment()
        else:
            self.error(f"Unexpected token {self.current_token.type}")
    
    def parse(self):
        statements = []
        while self.current_token.type != 'EOF':
            statements.append(self.statement())
        return {'type': 'block', 'statements': statements}

class Interpreter:
    def __init__(self):
        import math
        import time
        import random
        import os
        import subprocess
        import hashlib
        
        self.symbols = {}
        self.functions = {
            # 字符串和数组函数
            'len': lambda s: str(len(eval(s)) if s.startswith('[') and s.endswith(']') else len(s)),
            'upper': lambda s: s.upper(),
            'lower': lambda s: s.lower(),
            'substring': lambda s, start, end: s[int(start):int(end)],
            # 数组函数
            'arr': lambda *args: str(list(args)),
            'push': lambda arr, item: str(eval(arr) + [item]),
            'pop': lambda arr: str(eval(arr)[:-1]),
            'indexOf': lambda arr, item: str(eval(arr).index(item) if item in eval(arr) else -1),
            'join': lambda arr, sep: sep.join(eval(arr)),
            'reverse': lambda arr: str(list(reversed(eval(arr)))),
            'sort': lambda arr: str(sorted(eval(arr))),
            'slice': lambda arr, start, end: str(eval(arr)[int(start):int(end)]),
            # 数学库
            'math.abs': lambda x: str(abs(float(x))),
            'math.sqrt': lambda x: str(float(x) ** 0.5),
            'math.pow': lambda x, y: str(float(x) ** float(y)),
            'math.sin': lambda x: str(math.sin(math.radians(float(x)))),
            'math.cos': lambda x: str(math.cos(math.radians(float(x)))),
            'math.tan': lambda x: str(math.tan(math.radians(float(x)))),
            'math.asin': lambda x: str(math.degrees(math.asin(float(x)))),
            'math.acos': lambda x: str(math.degrees(math.acos(float(x)))),
            'math.atan': lambda x: str(math.degrees(math.atan(float(x)))),
            'math.pi': lambda: str(math.pi),
            'math.e': lambda: str(math.e),
            'math.max': lambda *args: str(max(float(arg) for arg in args)),
            'math.min': lambda *args: str(min(float(arg) for arg in args)),
            'math.random': lambda: str(random.random()),
            'math.randint': lambda a, b: str(random.randint(int(a), int(b))),
            # 日期时间库
            'time.now': lambda: str(int(time.time())),
            'time.sleep': lambda seconds: (time.sleep(float(seconds)), 'Done')[1],
            'time.format': lambda timestamp, format_str: time.strftime(format_str, time.localtime(float(timestamp))),
            # JSON库
            'json.parse': lambda json_str: str(eval(json_str)),
            'json.stringify': lambda obj: str(obj),
            # 加密库
            'crypto.md5': lambda s: hashlib.md5(s.encode()).hexdigest(),
            'crypto.sha1': lambda s: hashlib.sha1(s.encode()).hexdigest(),
            'crypto.sha256': lambda s: hashlib.sha256(s.encode()).hexdigest(),
            # 字符串操作库
            'string.split': lambda s, sep: str(list(s)) if sep == '' else str(s.split(sep)),
            'string.upper': lambda s: s.upper(),
            'string.lower': lambda s: s.lower(),
            'string.trim': lambda s: s.strip(),
            'string.replace': lambda s, old, new: s.replace(old, new),
            'string.startsWith': lambda s, prefix: str(s.startswith(prefix)),
            'string.endsWith': lambda s, suffix: str(s.endswith(suffix)),
            'string.substring': lambda s, start, end: s[int(start):int(end)],
            'string.indexOf': lambda s, substr: str(s.find(substr)),
            'string.length': lambda s: str(len(s)),
            'string.contains': lambda s, substr: str(substr in s),
            'string.concat': lambda s1, s2: s1 + s2,
            'string.repeat': lambda s, n: s * int(n),
            'string.reverse': lambda s: s[::-1],
            'string.includes': lambda s, substr: str(substr in s),
            'string.lastIndexOf': lambda s, substr: str(s.rfind(substr)),
            'string.padStart': lambda s, length, char: s.rjust(int(length), char),
            'string.padEnd': lambda s, length, char: s.ljust(int(length), char),
            # 数组操作库
            'array.length': lambda arr: str(len(eval(arr))),
            'array.push': lambda arr, item: str(eval(arr) + [item]),
            'array.pop': lambda arr: str(eval(arr)[:-1]),
            'array.shift': lambda arr: str(eval(arr)[1:]),
            'array.unshift': lambda arr, item: str([item] + eval(arr)),
            'array.indexOf': lambda arr, item: str(eval(arr).index(item) if item in eval(arr) else -1),
            'array.lastIndexOf': lambda arr, item: str(len(eval(arr)) - 1 - eval(arr)[::-1].index(item) if item in eval(arr) else -1),
            'array.includes': lambda arr, item: str(item in eval(arr)),
            'array.join': lambda arr, sep: sep.join(eval(arr)),
            'array.reverse': lambda arr: str(list(reversed(eval(arr)))),
            'array.sort': lambda arr: str(sorted(eval(arr))),
            'array.slice': lambda arr, start, end: str(eval(arr)[int(start):int(end)]),
            # 工具库
            'util.random': lambda: str(random.random()),
            'util.randint': lambda a, b: str(random.randint(int(a), int(b))),
            'util.round': lambda x, n=0: str(round(float(x), int(n))),
            'util.abs': lambda x: str(abs(float(x))),
            'util.min': lambda *args: str(min(float(arg) for arg in args)),
            'util.max': lambda *args: str(max(float(arg) for arg in args)),
            'util.sum': lambda *args: str(sum(float(arg) for arg in args)),
            'util.average': lambda *args: str(sum(float(arg) for arg in args) / len(args)) if args else '0',
            'util.isNumber': lambda x: str(x.replace('.', '', 1).replace('-', '', 1).isdigit()),
            'util.isString': lambda x: str(isinstance(x, str)),
            'util.isArray': lambda x: str(x.startswith('[') and x.endswith(']')),
            'util.toNumber': lambda x: str(float(x)),
            'util.toString': lambda x: str(x),
            'util.typeof': lambda x: 'array' if x.startswith('[') and x.endswith(']') else 'number' if x.replace('.', '', 1).replace('-', '', 1).isdigit() else 'string' if isinstance(x, str) else 'unknown',
            # 其他函数
            'input': lambda prompt: input(prompt),
            'int': lambda s: str(int(s)),
            'str': lambda x: str(x),
            # 网络请求函数
            'http_get': self.http_get,
            'http_post': self.http_post,
            # 文件操作函数
            'file_read': self.file_read,
            'file_write': self.file_write,
            'file_exists': self.file_exists,
            # 系统函数
            'system': self.system,
            'get_env': self.get_env
        }
        self.classes = {}
        self.return_value = None
        self.modules = {}
        
        # 模块引用
        self.math = math
        self.time = time
        self.random = random
        self.os = os
        self.subprocess = subprocess
        self.hashlib = hashlib
    
    def error(self, message, line=0, column=0):
        # For Windows PowerShell compatibility, use simple error messages without ANSI codes
        error_msg = "Runtime Error"
        if line > 0 and column > 0:
            error_msg += f" at line {line}, column {column}"
        error_msg += f": {message}"
        raise Exception(error_msg)
    
    def http_get(self, url):
        """Send HTTP GET request"""
        try:
            import urllib.request
            import json
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                return data
        except Exception as e:
            return f"Error: {str(e)}"
    
    def http_post(self, url, data):
        """Send HTTP POST request"""
        try:
            import urllib.request
            import urllib.parse
            import json
            data = data.encode('utf-8')
            req = urllib.request.Request(url, data=data, method='POST')
            req.add_header('Content-Type', 'application/json')
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                return response_data
        except Exception as e:
            return f"Error: {str(e)}"
    
    def file_read(self, filename):
        """Read file content"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def file_write(self, filename, content):
        """Write content to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                return "Success"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def file_exists(self, filename):
        """Check if file exists"""
        try:
            return str(1 if self.os.path.exists(filename) else 0)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def time_now(self):
        """Get current time"""
        try:
            return str(self.time.time())
        except Exception as e:
            return f"Error: {str(e)}"
    
    def time_sleep(self, seconds):
        """Sleep for specified seconds"""
        try:
            self.time.sleep(float(seconds))
            return "Success"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def random_int(self, min_val, max_val):
        """Generate random integer between min and max"""
        try:
            return str(self.random.randint(int(min_val), int(max_val)))
        except Exception as e:
            return f"Error: {str(e)}"
    
    def random_float(self):
        """Generate random float between 0 and 1"""
        try:
            return str(self.random.random())
        except Exception as e:
            return f"Error: {str(e)}"
    
    def system(self, command):
        """Execute system command"""
        try:
            result = self.subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_env(self, var_name):
        """Get environment variable"""
        try:
            value = self.os.environ.get(var_name, "")
            return value
        except Exception as e:
            return f"Error: {str(e)}"
    
    def evaluate(self, node):
        if node['type'] == 'literal':
            return node['value']
        elif node['type'] == 'identifier':
            if node['name'] in self.symbols:
                return self.symbols[node['name']]
            else:
                raise Exception(f"Undefined variable: {node['name']}")
        elif node['type'] == 'array_index':
            # Handle array indexing
            array_value = self.symbols.get(node['name'])
            if array_value is None:
                raise Exception(f"Undefined variable: {node['name']}")
            # Evaluate the index expression
            index_value = self.evaluate(node['index'])
            # Convert array string to actual list
            try:
                array = eval(array_value)
                if isinstance(array, list):
                    index = int(index_value)
                    if 0 <= index < len(array):
                        return array[index]
                    else:
                        raise Exception(f"Array index out of range: {index}")
                else:
                    raise Exception(f"Variable {node['name']} is not an array")
            except Exception as e:
                raise Exception(f"Error accessing array: {str(e)}")
        elif node['type'] == 'binary_op':
            left = self.evaluate(node['left'])
            right = self.evaluate(node['right'])
            
            # Check if both operands are numbers for arithmetic operations
            if left.isdigit() and right.isdigit():
                left_num = int(left)
                right_num = int(right)
                
                if node['op'] == '+':
                    return str(left_num + right_num)
                elif node['op'] == '-':
                    return str(left_num - right_num)
                elif node['op'] == '*':
                    return str(left_num * right_num)
                elif node['op'] == '/':
                    if right_num == 0:
                        raise Exception("Division by zero")
                    return str(left_num // right_num)
                elif node['op'] == '==':
                    return str(1 if left_num == right_num else 0)
                elif node['op'] == '!=':
                    return str(1 if left_num != right_num else 0)
                elif node['op'] == '<':
                    return str(1 if left_num < right_num else 0)
                elif node['op'] == '<=':
                    return str(1 if left_num <= right_num else 0)
                elif node['op'] == '>':
                    return str(1 if left_num > right_num else 0)
                elif node['op'] == '>=':
                    return str(1 if left_num >= right_num else 0)
            else:
                # String operations
                if node['op'] == '+':
                    return left + right
                elif node['op'] == '==':
                    return str(1 if left == right else 0)
                elif node['op'] == '!=':
                    return str(1 if left != right else 0)
                else:
                    raise Exception("Unsupported operation for non-numeric values")
            
            # Logical operations
            if node['op'] == '&&':
                return str(1 if (int(left) != 0 and int(right) != 0) else 0)
            elif node['op'] == '||':
                return str(1 if (int(left) != 0 or int(right) != 0) else 0)
        elif node['type'] == 'function_call':
            # Handle function calls in expressions
            if node['name'] in self.symbols and callable(self.symbols[node['name']]):
                # Check if it's a function from a module (like pylang or bflang)
                func = self.symbols[node['name']]
                args = [self.evaluate(arg) for arg in node['arguments']]
                return func(*args)
            elif node['name'] in self.functions:
                # Check if it's a built-in function (lambda)
                func = self.functions[node['name']]
                if callable(func):
                    # Check if it's a library function that requires import
                    if '.' in node['name']:
                        # Extract library name from function name (e.g., math.abs -> math)
                        library_name = node['name'].split('.')[0]
                        # Check if the library is imported
                        if library_name not in self.modules:
                            self.error(f"Library '{library_name}' not imported. Use '@{library_name}' to import it.")
                    # Check if it's an HTTP function that requires http module
                    if (node['name'] == 'http_get' or node['name'] == 'http_post') and 'http' not in self.modules:
                        self.error("HTTP module not imported. Use '@http' to import it.")
                    # It's a built-in function
                    args = [self.evaluate(arg) for arg in node['arguments']]
                    return func(*args)
                else:
                    # It's a user-defined function
                    # Create local symbol table
                    local_symbols = self.symbols.copy()
                    # Assign arguments to parameters
                    for i, param in enumerate(func['parameters']):
                        if i < len(node['arguments']):
                            local_symbols[param] = self.evaluate(node['arguments'][i])
                        else:
                            local_symbols[param] = '0'  # Default value
                    # Save current symbol table and return value
                    old_symbols = self.symbols
                    old_return_value = self.return_value
                    # Set local symbol table
                    self.symbols = local_symbols
                    # Reset return value
                    self.return_value = None
                    # Execute function body
                    self.interpret(func['body'])
                    # Get return value
                    return_value = self.return_value
                    # Restore symbol table and return value
                    self.symbols = old_symbols
                    self.return_value = old_return_value
                    # Return the value (ensure it's a string)
                    if return_value is not None:
                        return str(return_value)
                    return return_value
            else:
                self.error(f"Unknown function: {node['name']}")
        else:
            raise Exception(f"Unknown node type: {node['type']}")
    
    def interpret(self, node):
        if isinstance(node, list):
            for stmt in node:
                result = self.interpret(stmt)
                if result is not None:
                    return result
        elif node['type'] == 'block':
            for stmt in node['statements']:
                result = self.interpret(stmt)
                if result is not None:
                    return result
        elif node['type'] == 'assignment':
            value = self.evaluate(node['value'])
            self.symbols[node['name']] = value
        elif node['type'] == 'function_call':
            if node['name'] == 'show':
                for arg in node['arguments']:
                    value = self.evaluate(arg)
                    print(value, end=' ')
                print()
            elif node['name'] in self.symbols and callable(self.symbols[node['name']]):
                # Check if it's a function from a module (like pylang or bflang)
                func = self.symbols[node['name']]
                args = [self.evaluate(arg) for arg in node['arguments']]
                result = func(*args)
                return result
            elif node['name'] in self.functions:
                # Check if it's a built-in function (lambda)
                func = self.functions[node['name']]
                if callable(func):
                    # Check if it's a library function that requires import
                    if '.' in node['name']:
                        # Extract library name from function name (e.g., math.abs -> math)
                        library_name = node['name'].split('.')[0]
                        # Check if the library is imported
                        if library_name not in self.modules:
                            self.error(f"Library '{library_name}' not imported. Use '@{library_name}' to import it.")
                    # Check if it's an HTTP function that requires http module
                    if (node['name'] == 'http_get' or node['name'] == 'http_post') and 'http' not in self.modules:
                        self.error("HTTP module not imported. Use '@http' to import it.")
                    # It's a built-in function
                    args = [self.evaluate(arg) for arg in node['arguments']]
                    result = func(*args)
                    return result
                else:
                    # It's a user-defined function
                    # Create local symbol table
                    local_symbols = self.symbols.copy()
                    # Assign arguments to parameters
                    for i, param in enumerate(func['parameters']):
                        if i < len(node['arguments']):
                            local_symbols[param] = self.evaluate(node['arguments'][i])
                        else:
                            local_symbols[param] = '0'  # Default value
                    # Save current symbol table and return value
                    old_symbols = self.symbols
                    old_return_value = self.return_value
                    # Set local symbol table
                    self.symbols = local_symbols
                    # Reset return value
                    self.return_value = None
                    # Execute function body
                    self.interpret(func['body'])
                    # Get return value
                    return_value = self.return_value
                    # Restore symbol table and return value
                    self.symbols = old_symbols
                    self.return_value = old_return_value
                    # Return the value (ensure it's a string)
                    if return_value is not None:
                        return str(return_value)
                    return return_value
            elif node['name'] in self.functions and 'math.' in node['name']:
                # Check if it's a math function
                func = self.functions[node['name']]
                if callable(func):
                    # It's a math function
                    args = [self.evaluate(arg) for arg in node['arguments']]
                    result = func(*args)
                    return result
            else:
                self.error(f"Unknown function: {node['name']}")
        elif node['type'] == 'if_statement':
            condition = self.evaluate(node['condition'])
            if int(condition) != 0:
                self.interpret(node['then_branch'])
            elif node['else_branch']:
                self.interpret(node['else_branch'])
        elif node['type'] == 'while_statement':
            while True:
                condition = self.evaluate(node['condition'])
                if int(condition) == 0:
                    break
                self.interpret(node['body'])
                # Check for return statement
                if self.return_value is not None:
                    break
        elif node['type'] == 'def_statement':
            # Store function definition
            self.functions[node['name']] = {
                'parameters': node['parameters'],
                'body': node['body']
            }
        elif node['type'] == 'class_statement':
            # Store class definition
            self.classes[node['name']] = {
                'methods': {}
            }
            for method in node['methods']:
                self.classes[node['name']]['methods'][method['name']] = {
                    'parameters': method['parameters'],
                    'body': method['body']
                }
        elif node['type'] == 'return_statement':
            # Set return value
            self.return_value = self.evaluate(node['value'])
        elif node['type'] == 'import_statement':
            # Handle import statement
            module = node['module']
            self.modules[module] = True
            # Here you can add module-specific initialization
            if module == 'http':
                # HTTP module is already initialized in functions
                pass
            elif module == 'math':
                # Add math functions to the current scope
                pass
        elif node['type'] == 'include_directive':
            # Handle include directive
            module = node['module']
            self.modules[module] = True
            
            # Check if it's a built-in module
            if module == 'response':
                # Enable HTTP request functions
                pass
            else:
                # Try to load from includes folder
                import os
                include_path = os.path.join('includes', f'{module}.oraset')
                if os.path.exists(include_path):
                    try:
                        with open(include_path, 'r', encoding='utf-8') as f:
                            source = f.read()
                        # Parse and interpret the included file
                        lexer = Lexer(source)
                        parser = Parser(lexer)
                        ast = parser.parse()
                        self.interpret(ast)
                        print(f"Successfully included module: {module}")
                    except Exception as e:
                        print(f"Error including module {module}: {e}")
                else:
                    print(f"Warning: Module {module} not found in includes folder")
        else:
            raise Exception(f"Unknown node type: {node['type']}")

import base64
import zlib

def pack_file(input_file, output_file):
    """Pack .oas file into .osp file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Compress the source code
        compressed = zlib.compress(source.encode('utf-8'))
        # Encode as base64
        encoded = base64.b64encode(compressed)
        
        with open(output_file, 'wb') as f:
            f.write(encoded)
        
        print(f"Successfully packed {input_file} into {output_file}")
        return 0
    except Exception as e:
        print(f"Error packing file: {e}")
        return 1

def unpack_file(input_file):
    """Unpack .osp file and return the source code"""
    try:
        with open(input_file, 'rb') as f:
            encoded = f.read()
        
        # Decode from base64
        compressed = base64.b64decode(encoded)
        # Decompress
        source = zlib.decompress(compressed).decode('utf-8')
        
        return source
    except Exception as e:
        print(f"Error unpacking file: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print(f"Usage:")
        print(f"  {sys.argv[0]} <filename.oas|.oraset>  # Run .oas or .oraset file")
        print(f"  {sys.argv[0]} pack <filename.oas|.oraset>  # Pack .oas or .oraset file into .osp")
        print(f"  {sys.argv[0]} -osp <filename.osp>    # Run .osp file")
        return 1
    
    if sys.argv[1] == 'pack':
        if len(sys.argv) != 3:
            print(f"Usage: {sys.argv[0]} pack <filename.oas|.oraset>")
            return 1
        input_file = sys.argv[2]
        output_file = input_file.replace('.oas', '.osp').replace('.oraset', '.osp')
        return pack_file(input_file, output_file)
    elif sys.argv[1] == '-osp':
        if len(sys.argv) != 3:
            print(f"Usage: {sys.argv[0]} -osp <filename.osp>")
            return 1
        input_file = sys.argv[2]
        source = unpack_file(input_file)
        if source is None:
            return 1
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                source = f.read()
        except FileNotFoundError:
            print(f"Error: Could not open file {filename}")
            return 1
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    try:
        ast = parser.parse()
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    interpreter = Interpreter()
    try:
        interpreter.interpret(ast)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
