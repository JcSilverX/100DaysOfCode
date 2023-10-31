"""
    Day 08 - Project: Caesar Cipher -- Encrption & Decription

    Coded by JcSilverX
"""

ALPHABETS = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift:int):
	cipher_text = ''

	for chr in plain_text:
		if chr in ALPHABETS:
			curr_pos = ALPHABETS.index(chr)
			new_pos = (curr_pos + shift) % 26
			cipher_text += ALPHABETS[new_pos]
		else:
			cipher_text += chr
	return cipher_text


def decrypt(cipher_text, shift:int):
	plain_text = ''

	for chr in cipher_text:
		if chr in ALPHABETS:
			curr_pos = ALPHABETS.index(chr)
			new_pos = (curr_pos - shift) % 26
			plain_text += ALPHABETS[new_pos]
		else:
			plain_text += chr
	return plain_text


def validate_input(inp):
	try:
		input_value = int(inp)
		if (input_value < 0):
			err_exit(error='cannot be negative.')
		return input_value
	except ValueError as err:
		err_exit(error=err)


def err_exit(error):
	print(error)
	exit()


if __name__ == '__main__':
	flag = False

	while not flag:
		direction = input('Type `encode` to encrypt, type `decode` to decrypt: ')
		text = input('Type your message: ').lower()
		shift = validate_input(input('Type the shift number: '))

		if direction == 'encode':
			cipher_text = ''
			print(f'The encoded text is {encrypt(plain_text=text, shift=shift)}')
		elif direction == 'decode':
			print(f'The decoded text is {decrypt(cipher_text=text, shift=shift)}')
		else:
			print('Invalid choice...')

		choice = str(input('Type `yes` if you want to go again. Otherwise type `no`. '))
		if choice == 'no':
			flag = True


