#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lexer(object):
	"""
	Creates a new type of object : 'Lexer'.
	"""
	
	KEYWORDS = ["class", "fct", "true", "false", "not", "if", "else", "elif",
		"else if", "do", "while", "for", "switch", "case", "finally", "break",
		"return", "print", "printn", "&&", "and", "||", "or", "from","continue",
		"as", "import", "in", "is", "pass", "try", "null", "var", "let", "void",
		"int", "str", "double", "float", "long", "boolean", "complex", "void"]
	
	def tokenize(code):
		code = code.strip() # Remove extra line breaks
		tokens = [] # This will hold the generated tokens
		current_index = 0 # Number of spaces in the last indent
		indent_stack = []
		i = 0 # Current character position
		while i < len(code):
			code[i : len(code)]
			
			if identifier = #chunk[/\A([a-z]\w*)/, 1]
				if identifier in KEYWORDS: # Keywords will generate [:IF, "if"]
					tokens.append([identifier.upper(), identifier])
				else
					tokens.append([:IDENTIFIER, identifier])
				i += len(identifier) # Skip what we just parsed
