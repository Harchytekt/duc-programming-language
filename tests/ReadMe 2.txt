2- Programming language Duc

Test du Lexer (en Ruby)

ruby test_Lexer.rb

"if tasty == true:
	print tasty"

	⁃	On obtient:

[:IF, "if"][:IDENTIFIER, "tasty"]["==", "==« ][:BOOLEAN, "true"][":", ":"][:NEWLINE, "\n"]["\t", "\t"][:PRINT, "print"][:IDENTIFIER, "tasty"]