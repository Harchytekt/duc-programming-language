1- Programming language Duc

Bloc:
if (…) {
	…
} elif (…) {
	…
} else 
	…
}

Fonction comme en C et Java: 🗝 + type de retour / void + nom
Puissance: 8 = 2 ** 3
Nombre complexe: a + bi = complex(a, b)
do…while: do {…} while;
do { → [BEGIN do-while]
Parenthèses facultatives
Attention:
- print: plusieurs ‘print’ seront sur la même ligne sauf si ‘\n’ → ajouter « , » après le print
- printn: va à la ligne automatiquement → print par défaut en Python


Comment déclarer/initialiser des variables ?
* myNumber = 5 → Pas de déclaration sans initialisation 😩
* int myNumber = 5 → int myNumber
* var myNumber(: int) = 5 / let myName = ’’Alexandre’’ (constante) → var myNumber: int
* var friend: str? (Optionals ?) 🤔
	Avec tuples:
* myNumber, myName = 5, ’’Alexandre’’ (parenthèses facultatives)
* let red, green, blue: Double
* let(red:  Double, green:  Double, blue:  Double) peuvent être de types différents
* Cas 1.1: int myNumber, myAge = 5, 21
* Cas 1.2:int myNumber, str myName = 5, ’’Alexandre’’
* Cas 2.1: var myNumber, yourNumber = 5, 7
* Cas 2.2: var myNumber, let myName = 5, ’’Alexandre’’
* Cas 2.3: var myNumber: int, myString: str = 5, ’’str’’

→ Peut-être: On utilise var et let, si pas utilisé alors c’est un var sous-entendu

Mots-clefs: 🗝
- class
- def, fct ? (fonction)
- true, True ?
- false, False ?
- if, else, elif
- do
- while
- for
- switch
- case
- finally
- break
- return
- print / printn
- and / &&, or / ||
- from
- !, not ? (negation)
- continue
- as
- import
- in
- is
- pass
- try
- null, None ?
- var ?
- let ?
- void
- int, str, double, float, long, boolean, void, complex

« Faire de POO plus comme en Java que comme en Python »
to_sym converts a string to a symbol. For example, "a".to_sym becomes :a