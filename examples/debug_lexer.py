#!/usr/bin/env python3

import sys
sys.path.insert(0, 'f:/Oraset')

from oraset import Lexer

source = '''input username "test"'''

lexer = Lexer(source)
tokens = []
while True:
    tok = lexer.get_next_token()
    tokens.append(tok)
    print(f"Token: type={tok.type}, value={repr(tok.value)}, line={tok.line}, col={tok.column}")
    if tok.type == 'EOF':
        break