import re

KEYWORDS = ["class", "fct", "true", "false", "not", "if", "else", "elif",
		"else if", "do", "while", "for", "switch", "case", "finally", "break",
		"return", "print", "printn", "&&", "and", "||", "or", "from","continue",
		"as", "import", "in", "is", "pass", "try", "null", "var", "let", "void",
		"int", "str", "double", "float", "long", "boolean", "complex", "void"]

code = """if tasty == true {
	print b
} else {
	if a >= 2. {
		print 2
	}
}
"""

strRegex = "[\"]+"
identifierRegex = "[a-z]+"
idRegex = "\A([a-z]+\w*)"
#floatRegex = r"-?[0-9]+\.[0-9]+([eE]-?[0-9]+)?"

#print code
#print re.findall(strRegex, code)
print re.findall(identifierRegex, code)
#print re.findall(floatRegex, code)


i, j, k = 0, 0, 0
constante, identifier = [], []
while i < len(code):
	code = code[i : len(code)]
	i = 0
	if code[0].isalpha() and code[0] != " ":
		constante.append(re.findall(idRegex, code)[0])
		
		
		i = len(constante[j])
		
		if constante[j] in KEYWORDS:
			identifier.append(constante.pop())
			j -= 1
		
		j += 1
	else:
		i += 1

print constante
print identifier
