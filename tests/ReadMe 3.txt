3- Programming language Duc

Test du Lexer (en Python)

python test_Lexer.py 

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

['class', 'Person', '{', 'var', '(', 'bDate', ':', 'Date', ',', 'dDate', ':', 'Date', ',', 'family', ':', 'Family', ')', 'var', 'gender', ',', 'fName', ',', 'lName', ',', 'location', ':', 'str', 'var', 'lives', '=', 'true', 'fct', 'Person', '(', ')', '{', 'bDate', '=', 'new', 'Date', '(', '21', ',', '06', ',', '1994', ')', 'this', '.', 'setDate', '(', ')', '(', 'gender', ',', 'fName', ',', 'lName', ')', '=', '(', '"M"', ',', '"John"', ',', '"Smith"', ')', '(', 'location', ',', 'family', ')', '=', '(', '"New-York, USA"', ',', 'new', 'Family', '(', ')', ')', '}', '}']
[CLASS]
[IDENTIFIER, 'Person']
[OPEN BLOCK 1]
[VAR]
[OPEN PARENTH 1]
[IDENTIFIER, 'bDate']
[IDENTIFIER, ':']
[IDENTIFIER, 'Date']
[COMMA]
[IDENTIFIER, 'dDate']
[IDENTIFIER, ':']
[IDENTIFIER, 'Date']
[COMMA]
[IDENTIFIER, 'family']
[IDENTIFIER, ':']
[IDENTIFIER, 'Family']
[CLOSE PARENTH 1]
[VAR]
[IDENTIFIER, 'gender']
[COMMA]
[IDENTIFIER, 'fName']
[COMMA]
[IDENTIFIER, 'lName']
[COMMA]
[IDENTIFIER, 'location']
[IDENTIFIER, ':']
[str, 'str']
[VAR]
[IDENTIFIER, 'lives']
[Assign]
[TRUE]
[FONCTION]
[IDENTIFIER, 'Person']
[OPEN PARENTH 2]
[CLOSE PARENTH 2]
[OPEN BLOCK 2]
[IDENTIFIER, 'bDate']
[Assign]
[NewObject]
[IDENTIFIER, 'Date']
[OPEN PARENTH 3]
[int, '21']
[COMMA]
[int, '06']
[COMMA]
[int, '1994']
[CLOSE PARENTH 3]
[this]
[DerefOperator]
[IDENTIFIER, 'setDate']
[OPEN PARENTH 4]
[CLOSE PARENTH 4]
[OPEN PARENTH 5]
[IDENTIFIER, 'gender']
[COMMA]
[IDENTIFIER, 'fName']
[COMMA]
[IDENTIFIER, 'lName']
[CLOSE PARENTH 5]
[Assign]
[OPEN PARENTH 6]
[str, '"M"']
[COMMA]
[str, '"John"']
[COMMA]
[str, '"Smith"']
[CLOSE PARENTH 6]
[OPEN PARENTH 7]
[IDENTIFIER, 'location']
[COMMA]
[IDENTIFIER, 'family']
[CLOSE PARENTH 7]
[Assign]
[OPEN PARENTH 8]
[str, '"New-York, USA"']
[COMMA]
[NewObject]
[IDENTIFIER, 'Family']
[OPEN PARENTH 9]
[CLOSE PARENTH 8]
[CLOSE PARENTH 9]
[CLOSE BLOCK 1]
[CLOSE BLOCK 2]
Ok
2 opened block(s) for 2 ended block(s).
Ok
9 opened parentheses block(s) for 9 closed parentheses block(s).