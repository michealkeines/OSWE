
"edac 0500 0074 4e05 7479 6f72" // Hex dump of serialized data of string "Nytro"

"AC ED" -> Indentifies Serialized data in java

"00 05" -> Serialization protocal version

"74" -> Data stored is of type string

"00 05" -> length of the string

"4e 74 79 6f 72" -> the string value "Nytro" in hex

--------------------------------------------------------------------------



"AC ED" -> Indentifies that it is java serialized data

"00 05" -> protocol version

"73" -> data type object

"72" -> class description

"00 07" -> length of class name

"4C 6F 67 46  69 6C 65" -> name of the class in hex (LogFile)

"B0 31 94 4B 14 63 79 70" -> Serial UID - this can be specified in the class, if not, it is generated automatically

"02" -> flag to say that the class is serializable

"00 02" -> number of variables in the class

"4C" -> type - class

"00 0B" -> length of class variable 

"66 69 6C 65 63 6F 6E 65 6E 74" -> variable name

"74" -> string

"00 12" -> length of class name

"4C 6A 61 76 61 2F 6C 61 6E 67 2F 53 74 72 69 6E 67 3B" -> class name

"4C" -> type - class

"00 08" -> lenght of variable

"66 69 6C 65 6E 61 6D 65" -> variable name

"71" -> reference to previous object

"00 7E 00 01" -> object reference start from 

"78" -> end of block object

"70" -> null reference

"74" -> type string

"00 10" -> lenght of the string

"77 65 20 64 69 64 20 73 6F 6D 65 74 68 69 6E 67" -> string value

"74" -> type string

"00 08" -> length of the string

"65 73 74 2E 6C 6F 67" -> string value




