message = "Hello, World!"
shift = 4

FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def ceaser_shift(message, shift):
	# Result placeholder.
	result = ""	

	# Go through each of the letters in the message.
	for char in message. upper():
		if char.isalpha():
		
			#Convert character to the ASCII code.
			char_code = ord(char)
			new_char_code = char_code + shift
			
			if new_char_code > LAST_CHAR_CODE:
			    new_char_code -= CHAR_RANGE
			    
			if new_char_code < FIRST_CHAR_CODE:
			   new_char_code += CHAR_RANGE
			
			    
			new_char = chr(new_char_code)
			result += new_char
		else:
			result += char
	print(result)

ceaser_shift("Hello, World!", 4)
ceaser_shift("ABCDE!", 2)
ceaser_shift("Pizza", 6)
ceaser_shift("VOFFG", -6)

user_message = input("Message to encrypt: ")	
user_shift_key = int(input("Shift Key (integer): "))
ceaser_shift(user_message, user_shift_key)
	













