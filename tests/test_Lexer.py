# This is a test file
import re

KEYWORDS = ["if", "else", "elif", "else if", "while", "for", "switch", "null",
		"var", "let", "true", "false", "continue", "pass", "break", "return",
		"class", "fct", "ctor", ",", "new", "print", "printn", ".", "do {",
		"} while", ";", "{", "}", "(", ")", "&&", "and", "||", "or", "!",
		"not", "==", "!=", "<", "<=", ">", ">=", "+", "-", "++", "--", "*",
		"/", "**", "%", "=", "+=", "-=", "*=", "/=", "%=", "this", "int",
		"str", "float", "long", "boolean", "complex", "void", "case", "from",
		"finally", "as", "in", "is", "import", "try"]

spaceList = [";", ":", "!", ".", ",", "{", "}", "(", ")", "<", ">", "+", "-",
		"*", "/", "**", "%", "="]


class newType(object):
	"""
	Creates a new type according to the given object.
	"""
	
	def __init__(self, t, n = 0):
		"""
		Initializes the name of the new type.
		"""
		if t in KEYWORDS[0:17]:
			self.__name__ = t.upper()
		elif t in KEYWORDS[17:18]:
			self.__name__ = "FUNCTION"
		elif t in KEYWORDS[18:19]:
			self.__name__ = "CONSTRUCTOR"
		elif t in KEYWORDS[19:20]:
			self.__name__ = "COMMA"
		elif t in KEYWORDS[20:21]:
			self.__name__ = "NewObject"
		elif t in KEYWORDS[21:23]:
			self.__name__ = dispPrint(t)
		elif t in KEYWORDS[23:24]:
			self.__name__ = "DerefOperator"
		elif t in KEYWORDS[24:31]:
			self.__name__ = dispBlock(t, n)
		elif t in KEYWORDS[31:37]:
			self.__name__ = dispLogic(t)
		elif t in KEYWORDS[37:57]:
			self.__name__ = dispOperator(t)
		else: # "this" is after dispOperator but before this else
			self.__name__ = t
	
	
	def __iter__(self):
		return self.__name__
	
	
	def __repr__(self):
		return self.__name__


def dispPrint(symb):
	"""
	Returns the wanted name of new type for print.
	"""
	if symb == "print":
		return "Print"
	else:
		return "PrintNewLine"


def dispBlock(symb, n):
	"""
	Returns the wanted name of new type for blocks.
	"""
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
	"""
	Returns the wanted name of new type for logical operators.
	"""
	if symb == "&&" or symb == "and":
		return "and"
	elif symb == "||" or symb == "or":
		return "or"
	else:
		return "not"


def dispOperator(symb):
	"""
	Returns the wanted name of new type for the other operators.
	"""
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


def mySplit(code):
	"""
	Splits the given code into a list of tokens.
	"""
	t = []
	i = 0
	while i < len(code):
		s = ""
		if code[i] in spaceList:
			if code[i: i + 7] == "} while":
				t.append("} while")
				i += 7
			elif code[i : i + 6] == "}while": #Find how to do this if-elif in 1
				t.append("} while")
				i += 6
			elif (i + 1 < len(code) and code[i + 1] in ["=", "+", "-", "*"]):
				t.append(code[i] + code[i + 1])
				i += 1
			else:
				t.append(code[i])
		elif code[i] == "\"":
			s += "\""
			j = i + 1
			while (j < len(code) and code[j] != "\""):
				s += code[j]
				j += 1
			s += "\""
			i = j
			t.append(s)
		elif (code[i] != " " and not code[i] in spaceList):
			s += code[i]
			j = i + 1
			while (j < len(code) and code[j] != " " and not code[j] in spaceList):
				s += code[j]
				if s == "do":
					if code[j + 1] == " " and code[j + 2] == "{":
						j += 2
					elif code[j + 1] == "{":
						j += 1
					s = "do {"
				j += 1
			i = j - 1
			t.append(s)
		i += 1
	return t


def isFloat(value):
	"""
	Returns True if the given value is a float, False otherwise.
	"""
	try:
		float(value)
		return True
	except ValueError:
		return False


def isInt(value):
	"""
	Returns True if the given value is an integer, False otherwise.
	"""
	try:
		int(value)
		return True
	except ValueError:
		return False


def isLong(value):
	"""
	Returns True if the given value is a long, False otherwise.
	"""
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
		"""
		Initializes the object.
		"""
		self.code = code
	
	
	def tokenize(self):
		"""
		Creates the list and fills it with the encountered tokens.
		"""
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
			elif token in KEYWORDS[0:64]: # +1 for "this" +6 for types
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
	
	
	def display(self, t):
		"""
		Displays each element of the token list.
		"""
		for elem in t:
			print elem
	
	
	def verifopBlock(self, opBlock, clsBlock):
		"""
		Verifies if the number of opened blocks is the same of closed one.
		"""
		if (opBlock != 0 or clsBlock != 0):
			s = str(opBlock) + " opened block(s) for "
			s += str(clsBlock) + " ended block(s)."
			if opBlock == clsBlock:
				print "Ok"
			else:
				print "Oops ! :("
			print s
	
	
	def verifDoW(self, beginDoW, do, endDoW):
		"""
		Verifies if the number of opened do-while is the same of closed one.
		"""
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
		"""
		Verifies if the number of opened parentheses is the same of closed one.
		"""
		if (opPar != 0 or clsPar != 0):
			s = str(opPar) + " opened parentheses block(s) for "
			s += str(clsPar) + " closed parentheses block(s)."
			if opPar == clsPar:
				print "Ok"
			else:
				print "Oops ! :("
			print s
	
	
if __name__ == '__main__': #TODO: comments

	cod = """
class MyClass {
	var tasty: boolean
	
	fct MyClass(tasty) {
		this.tasty = tasty
	}
	
	fct test() {
		if (!tasty && true){
			print "It's alive !"
		} else {
			if a >= 2. {
				print 2
			}
		}
		do {
			print "a"
			break
		} while true;
	}
	
	fct int fibo(int n) {
		if n == 0 {
			return n
		} elif n == 1 or n == 2 {
			return 1
		}
		return fibo(n - 1) + fibo(n - 2)
	}
}

maClasse = new MyClass(true)
print maClass.Fibo(5)
"""

	code = """
class Person {

	var(bDate: Date, dDate: Date, family: Family)
	var gender, fName, lName, location: str
	var lives = true
	
	ctor Person() {
		bDate = new Date(21, 06, 1994)
		this.setDate()
		(gender, fName, lName) = ("M", "John", "Smith")
		(location, family) = ("New-York, USA", new Family())
	}

	ctor Person(Date bDate, str gender, str fName, String lName, str location) {
		(family, this.bDate) = (new Family(), bDate)
		(this.fName, this.lName, this.location) = (fName, lName, location)
		try {
			if (gender.upper() != 'M' && gender.upper() != 'F' &&
					gender.upper() != 'U') {
				throw new GenderException()
			}
		} catch (GenderException ge){}
		this.gender = gender
	}

	ctor Person(Date bDate, Date dDate, str gender, str fName, String lName, str location) {
		(family, this.bDate, this.dDate) = (new Family(), bDate, dDate)
		(this.fName, this.lName, this.location) = (fName, lName, location)
		setLives(false)
		try {
			if (gender.upper() != 'M' && gender.upper() != 'F' &&
					gender.upper() != 'U') {
				throw new GenderException()
			}
		} catch (GenderException ge) {}
		this.gender = gender
	}

	fct str toString() {
		str res = fName + " " + lName
		if (lives) {
			res += " is a " + getStringAge() + " who lives in "
		} else {
			res += " was a " + getStringAge() + " who lived in "
		}
		return res + location + "."
	}

}
"""

	lexer = Lexer(code)
	print lexer.code
	(tok, ind, ded, bDoW, do, eDoW, opP, clsP)  = lexer.tokenize()
	lexer.display(tok)
	lexer.verifopBlock(ind, ded)
	lexer.verifDoW(bDoW, do, eDoW)
	lexer.verifPar(opP, clsP)
