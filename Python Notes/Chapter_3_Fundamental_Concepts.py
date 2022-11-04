#Lexical analysis is the process of breaking up source code into indentified tokens.
#Syntax analysis (or parsing) is the process of constructing a parse tree using the tokens provided by the lexer. Parsing provides more context about how the code should run.
#Semantic analysis is the process of applying the language's rules to the parse tree. This includes raising erors when rules are broken. Some examples are:
#Type mismatch
#Undeclared variable
#Parameter mismatch
#Ex. of a line of code converting Celsius into Fahrenheit:
f = (c * 9 / 5) + 32