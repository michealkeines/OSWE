REGULAR EXPRESSIONS

-literal strings or number can be 

eg: test, beak, a, 1 etc, will directly find matches for those words or numbers

-alternation this or that.. use this '|'

eg: what is test , what is okay.. we can match any of it using test|okay

-character sets can be used to look for different characters in a place with '[]'

eg: consensus can be greped as con[sc]en[sc]us, this takes anyone one of the
character in that given location.
this if [cat] it will look for three characters in that location not the word cat
^ is for negation inside the brackets
if [^cat] it will accept any character expect whats in that 'c','a','t'

'\' can be used to escape key terms like '.' etc

- '.' can be used to accept any character

eg: .... this will grep any 4 charcter words

remember within any character set we only match one character

-ranges can be used to give a range for charcter sets using '-'

eg: [4-6] or [a-z] or [A-Z] or [c-v] we can have multipe ranges [a-zA-Z0-9]

-short hand character class

\w - word character [a-zA-Z0-9_]
\d - digit character [0-9]
\s - whitespace like single space, tab, carraige return line break

the negated version of those classes are

\W - non-word character
\D - non digit character
\S - non whitespace character

grouping

we can group parts for more dynamic approach we use '()'

i love (cat | dog) this look for i love and either cat or dog

inside groups dont leave space that will be also be considered as a part of the regex
sor (cat|dog)

qunatifiers

fixed quantifiers
that character to classes to matched can be repeated a we want '{}'

eg: roa{3}r this accepts roar, roaar , roaaar this we can and {3,7} min and max to 
make it more dynamic

optional quantifiers

to make a grep optional that 0 or 1 occurence, thus we use '?'

eg: humou?r , here u is optional it be either present or not 


to make a grep optional that 0 or 1 or many time we use '*'

eg: meo*w, this any number of 'o' will get accepted
meow, meooooow, meooow etc

to make a grep 1 or more then we use '+'

eg: meo+w this will take anythin with meow atleast one 0
meow, meooow ..mew will not be taken as it doesnt have 1 'o'

anchors

^ to grep that it should start with the given word
$ to grep that it shoudl end wiht the given word

eg: ^test is best$ - this will only take sentence starting with test and ending with best


/*codecademy explantion


    Regular expressions are special sequences of characters that describe a pattern of text that is to be matched

    We can use literals to match the exact characters that we desire

    Alternation, using the pipe symbol |, allows us to match the text preceding or following the |

    Character sets, denoted by a pair of brackets [], let us match one character from a series of characters

    Wildcards, represented by the period or dot ., will match any single character (letter, number, symbol or whitespace)
    Ranges allow us to specify a range of characters in which we can make a match

    Shorthand character classes like \w, \d and \s represent the ranges representing word characters, digit characters, and whitespace characters, respectively

    Groupings, denoted with parentheses (), group parts of a regular expression together, and allows us to limit alternation to part of a regex

    Fixed quantifiers, represented with curly braces {}, let us indicate the exact quantity or a range of quantity of a character we wish to match

    Optional quantifiers, indicated by the question mark ?, allow us to indicate a character in a regex is optional, or can appear either 0 times or 1 time

    The Kleene star, denoted with the asterisk *, is a quantifier that matches the preceding character 0 or more times

    The Kleene plus, denoted by the plus +, matches the preceding character 1 or more times

    The anchor symbols hat ^ and dollar sign $ are used to match text at the start and end of a string, respectively
 
