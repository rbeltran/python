## my rot13.py

import string ##import maketrans, translate, ascii_lowercase
import functools

ENCODE = "encode"
DECODE = "decode"

def encode_rot13( phrase ) :
	## make a translation table where ascii_lowercase translates to a 13 shifted ascii_lowercase
	translation = str.maketrans( string.ascii_lowercase, string.ascii_lowercase[13:]+string.ascii_lowercase[:13])
	# decipher = functools.partial( str.translate, table=translation )
	# print( decipher( phrase ))
	print( phrase.translate( translation ))

def decode_rot13( phrase ) :
	## make a translation table where ascii_lowercase translates to a 13 shifted ascii_lowercase
	translation = str.maketrans( string.ascii_lowercase[13:]+string.ascii_lowercase[:13], string.ascii_lowercase)
	# decipher = functools.partial( str.translate, table=translation )
	# print( decipher( phrase ))
	print( phrase.translate( translation ))

def main() :
	input_var = input("Enter something: ")

	while input_var.lower() != ENCODE and input_var.lower() != DECODE :
		input_var = input("Enter something: ")

	if input_var.lower() == ENCODE :
		phrase_var = input("Enter phrase to be encoded:")
		output_var = encode_rot13( phrase_var.lower() ) 
	elif input_var.lower() == DECODE :
		phrase_var = input("Enter phrase to be decoded:")
		decoded_var = decode_rot13( phrase_var.lower() )
	else:
		print ("you entered " +input_var)

main()


