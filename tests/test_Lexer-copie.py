# This is a test file
import re

KEYWORDS = ["if", "else", "elif", "else if", "while", "for", "switch", "null",
		"var", "let", "true", "false", "continue", "pass", "break", "return",
		"class", "fct", ",", "new", "print", "printn", ".", "do {", "} while",
		";", "{", "}", "(", ")", "&&", "and", "||", "or", "!", "not", "==",
		"!=", "<", "<=", ">", ">=", "+", "-", "++", "--", "*", "/", "**", "%",
		"=", "+=", "-=", "*=", "/=", "%=", "this", "int", "str", "float",
		"long", "boolean", "complex", "void", "case", "from", "finally", "as",
		"in", "is", "import", "try"]

spaceList = [";", ":", "!", ".", ",", "{", "}", "(", ")", "<", ">", "+", "-",
		"*", "/", "**", "%", "="]


class newType(object):
	def __init__(self, t, n = 0):
		if t in KEYWORDS[0:17]:
			self.__name__ = t.upper()
		elif t in KEYWORDS[17:18]:
			self.__name__ = "FUNCTION"
		elif t in KEYWORDS[18:19]:
			self.__name__ = "COMMA" #or TUPLE ?
		elif t in KEYWORDS[19:20]:
			self.__name__ = "NewObject"
		elif t in KEYWORDS[20:22]:
			self.__name__ = dispPrint(t)
		elif t in KEYWORDS[22:23]:
			self.__name__ = "DerefOperator"
		elif t in KEYWORDS[23:30]:
			self.__name__ = dispBlock(t, n)
		elif t in KEYWORDS[30:36]:
			self.__name__ = dispLogic(t)
		elif t in KEYWORDS[36:56]:
			self.__name__ = dispOperator(t)
		else: # "this" is after dispOperator but before this else
			self.__name__ = t
		
	def __iter__(self):
		return self.__name__
	def __repr__(self):
		return self.__name__

def dispPrint(symb):
	if symb == "print":
		return "Print"
	else:
		return "PrintNewLine"

def dispBlock(symb, n):
	if symb == "do {":
		return "OPEN do-while " + str(n)
	elif symb == "} while":
		return "CLOSE do " + str(n)
	elif symb == ";":
		return "END do-while " + str(n)
	elif symb == "{":
		return "OPEN BLOCK " + str(n) # BEGIN or OPEN ?
	elif symb == "}":
		return "CLOSE BLOCK " + str(n) # END or CLOSE ?
	elif symb == "(":
		return "OPEN PARENTH " + str(n)
	else:
		return "CLOSE PARENTH " + str(n)

def dispLogic(symb):
	if symb == "&&" or symb == "and":
		return "and"
	elif symb == "||" or symb == "or":
		return "or"
	else:
		return "not"

def dispOperator(symb):
	if symb == "==":
		return "Equal"
	elif symb == "!=":
		return "Diff"
	elif symb == "<":
		return "Smaller"
	elif symb == "<=":
		return "SmallerOrEq"
	elif symb == ">":
		return "Greater"
	elif symb == ">=":
		return "GreaterOrEQ"
	elif symb == "+":
		return "Add"
	elif symb == "-":
		return "Sub"
	elif symb == "++":
		return "Increment"
	elif symb == "--":
		return "Decrement"
	elif symb == "*":
		return "Mult"
	elif symb == "/":
		return "Div"
	elif symb == "**":
		return "Exp"
	elif symb == "%":
		return "Mod"
	elif symb == "=":
		return "Assign"
	elif symb == "+=":
		return "AddAssign"
	elif symb == "-=":
		return "SubAssign"
	elif symb == "*=":
		return "MultAssign"
	elif symb == "/=":
		return "DivAssign"
	return "ModAssign"


def mySplit(code): # TODO: do{}While and str + \t, \n 
	#t = re.split("(\s|[,.;:(){}]|\n\t|\n)", code)
	#t = re.split("(\s|[,.;:(){}])", code)
	#pattern = re.compile("^\s+|\s*,\s*|\s+$|\s|([,.;:(){}]|\t|\n)")
	pattern = re.compile("\s|([,.;:!(){}]|\t|\n)")
	t = [x for x in pattern.split(code) if x]
	#t = [x.strip() for x in re.split("(\s|[,.;:(){}])", code)]
	return t

def isFloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

def isInt(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

def isLong(value):
	try:
		long(value)
		return True
	except ValueError:
		return False

class Lexer(object):
	"""
	Creates a new type of object : 'Lexer'.
	"""
	
	def __init__(self, code):
		self.code = code
	
	def tokenize(self):
		(opBlock, clsBlock, beginDoW, do, endDoW, opPar, clsPar) = (0, 0, 0, 0, 0, 0, 0)
		self.code = re.sub(r'[\t\n\r]', ' ', self.code) # Remove '\n' and '\t'
		tokens = [] # This will hold the generated tokens
		#current_index = 0 # Number of spaces in the last opBlock
		opBlock_stack = []
		tr = mySplit(self.code)
		
		print tr
	
		for token in tr:
			if token == "{":
				opBlock += 1
				tokens.append([newType(token, opBlock)])
			elif token == "}":
				clsBlock += 1
				tokens.append([newType(token, clsBlock)])
			elif token == "do {":
				beginDoW += 1
				tokens.append([newType(token, beginDoW)])
			elif token == "} while":
				do += 1
				tokens.append([newType(token, do)])
			elif token == "(":
				opPar += 1
				tokens.append([newType(token, opPar)])
			elif token == ")":
				clsPar += 1
				tokens.append([newType(token, clsPar)])
			elif token == ";":
				endDoW += 1
				tokens.append([newType(token, endDoW)])
			elif token in KEYWORDS[0:57]: # +1 pour "this"
				tokens.append([newType(token)])
			elif token in KEYWORDS:
				tokens.append([newType(token), token])
			else:
				if isInt(token):
					tokens.append([newType("int"), token])
				elif isFloat(token):
					tokens.append([newType("float"), token])
				elif "\"" in token:
					tokens.append([newType("str"), token])
				else:
					tokens.append([newType("IDENTIFIER"), token]) # IDENTIFIER is default
	
		return (tokens, opBlock, clsBlock, beginDoW, do, endDoW, opPar, clsPar)
	
	
	def disp(self, t):
		for elem in t:
			print elem

	def verifopBlock(self, opBlock, clsBlock):
		if (opBlock != 0 or clsBlock != 0):
			s = str(opBlock) + " opened block(s) for "
			s += str(clsBlock) + " ended block(s)."
			if opBlock == clsBlock:
				print "Ok"
			else:
				print "Oops ! :("
			print s

	def verifDoW(self, beginDoW, do, endDoW):
		if (beginDoW != 0 or do != 0 or endDoW != 0):
			s = str(beginDoW) + " opened do block(s) for "
			s += str(do) + " ended do block(s) and "
			s += str(endDoW) + " while."
			if beginDoW == do == endDoW:
				print "Ok"
			else:
				print "Oops ! :("
			print s

	def verifPar(self, opPar, clsPar):
		if (opPar != 0 or clsPar != 0):
			s = str(opPar) + " opened parentheses block(s) for "
			s += str(clsPar) + " closed parentheses block(s)."
			if opPar == clsPar:
				print "Ok"
			else:
				print "Oops ! :("
			print s

if __name__ == '__main__': #TODO: comments

# Problems with strings, floats, do{}while

	code = """
class MyClass {
	var tasty: boolean
	
	fct MyClass(tasty) {
		this.tasty = tasty
	}
	
	fct Test() {
		if (!tasty && true){
			print "It's alive !"
		} else {
			if a >= 2. {
				print 2
			}
		}
		do {
			print "a"
		} while true;
	}
	
	fct Fibo(n) {
		if n != 0 {
			return n
		} elif n == 1 or n == 2 {
			return 1
		}
		return Fibo(n - 1) + Fibo(n - 2)
	}
}

maClasse = new MyClass(true)
print maClass.Fibo(5)
"""

	cod = """
class Person {

	var(bDate: Date, dDate: Date, family: Family)
	var gender, fName, lName, location: str
	var lives = true
	
	fct Person() {
		bDate = new Date(21, 06, 1994)
		this.setDate()
		(gender, fName, lName) = ("M", "John", "Smith")
		(location, family) = ("New-York, USA", new Family())
	}

}
"""

	lexer = Lexer(code)
	print lexer.code
	(tok, ind, ded, bDoW, do, eDoW, opP, clsP)  = lexer.tokenize()
	lexer.disp(tok)
	lexer.verifopBlock(ind, ded)
	lexer.verifDoW(bDoW, do, eDoW)
	lexer.verifPar(opP, clsP)
	#print mySplit(code)
