# This is a test file

#code = "Alexandre"
#i = 0

#while (i < code.size)
#	chunk = code[i..-1]
#	print chunk
#	print "\n"
#	print chunk.upcase#.to_sym
#	print "\n"
#	i += 1
#end

KEYWORDS = ["class", "fct", "true", "false", "not", "if", "else", "elif",
		"else if", "do", "while", "for", "switch", "case", "finally", "break",
		"return", "print", "printn", "&&", "and", "||", "or", "from","continue",
		"as", "import", "in", "is", "pass", "try", "null", "var", "let", "void",
		"int", "str", "double", "float", "long", "boolean", "complex", "void"]

cod = "if tasty == true:
	print tasty"

def tokenize(code)
	code.chomp! # Remove extra line breaks
	tokens = [] # This will hold the generated tokens
	current_indent = 0 # Number of spaces in the last indent
	indent_stack = []
	
	i = 0
	while i < code.size
		chunk = code[i..-1]
		
		if identifier = chunk[/\A([a-z]\w*)/, 1]
			#print identifier
			#print "     "
			#print chunk[/\A([a-z]\w*)/, 1]
			#print "\n"
			if KEYWORDS.include?(identifier) # Keywords will generate [:IF, "if"]
				if identifier == "true" || identifier == "false" # Booleans added
					tokens << [:BOOLEAN, identifier]
				else
					tokens << [identifier.upcase.to_sym, identifier] # a.to_sym ==> :a
				end
			else
				tokens << [:IDENTIFIER, identifier]
			end
			i += identifier.size # Skip what we just parsed
			
		elsif constant = chunk[/\A([A-Z]\w*)/, 1]
			tokens << [:CONSTANT, constant]
			i += constant.size
		
		elsif number = chunk[/\A([0-9]+)/, 1]
			tokens << [:NUMBER, number.to_i]
			i += number.size
		
		elsif string = chunk[/\A"([^"]*)"/, 1]
			tokens << [:STRING, string]
			i += string.size + 2 # Skip two more to exclude the '"'
		
		elsif indent = chunk[/\A\:\n( +)/m, 1] # Matches ": <newline> <spaces>"
			if indent.size <= current_indent # indent should go up when creating a new block
				raise "Bad indent level, got #{indent.size} indents, " + 
				"expected > #{current_indent}"
			end
			current_indent = indent.size
			indent_stack.push(current_indent)
			tokens << [:INDENT, indent.size]
			i += indent.size + 2
		
		elsif indent = chunk[/\A\n( *)/m, 1] # Matches "<newline> <spaces>"
			if indent.size == current_indent # Case 2
				tokens << [:NEWLINE, "\n"] # Nothing to do, we're still in the same block
			elsif indent.size < current_indent # Case 3
				while indent.size < current_indent
					indent_stack.pop
					current_indent = indent_stack || 0
					tokens << [:DEDENT, indent.size]
				end
				tokens << [:NEWLINE, "\n"]
			else # indent.size > current_indent, error
				raise "Missing ':'" # Cannot increase indent level without using ":"
			end
			i += indent.size + 1
		
		elsif operator = chunk[/\A(\|\||&&|==|!=|<=|>=)/, 1]
			tokens << [:OPERATOR, operator] # Or if == ==> EQUAL
			i += operator.size
		
		elsif chunk.match(/\A /)
			i += 1
		
		else
			value = chunk[0, 1]
			tokens << [value, value]
			i += 1
		
		end
	end
	
	while indent = indent_stack.pop
		tokens << [:DEDENT, indent_stack.first || 0]
	end
	
	return tokens
end

def disp(toke)
	for elem in toke
		print elem
	end
end

tok = tokenize(cod)
disp(tok)
