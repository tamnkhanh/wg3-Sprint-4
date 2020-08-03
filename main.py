import random
#############################################
#------------FUNCTIONS FOR FILES------------#

#this is a function that opens files
def open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word.lower())
		output.append(line_words)
	return (output)

#this is a function that writes files
def write_file(filename, data):
	new_file = open(filename, "w")
	for sentence in data:
		for word in sentence:
			new_file.write(word + " ")
		new_file.write("\n")
	new_file.close()

##############################################
#------------FUNCTIONS FOR CIPHER------------#

#takes a letter and a key and return the encrypted char in a random order
def encrypt_letter(letter, key):
  #gets the integer of that letter from ascii
  number_of_char = ord(letter)
  #gets the index of that letter based on alphabet length
  index_of_char = number_of_char - ord("a")
  encrypted_char = key[index_of_char]
  return encrypted_char

#takes a letter and a key and return the decrypted char in a random order  
def decrypt_letter(letter, key):
  #gets the index of that letter from the encrypted key
  index_of_char = key.index(letter)
  number_of_char = index_of_char + ord("a")
  decrypted_char = chr(number_of_char)
  return decrypted_char

#takes a word and a key and return the encrypted word in a random order 
def encrypt_word(word, key):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  cipher_word = ""
  for letter in word:
    if letter in letters:
      cipher_word += encrypt_letter(letter, key)
    else:
      cipher_word += letter
  return cipher_word

#takes a word and a key and return the decrypted word in a random order 
def decrypt_word(word, key):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  plain_word = ""
  for letter in word:
    if letter in letters:
      plain_word += decrypt_letter(letter, key)
    else:
      plain_word += letter
  return plain_word

#takes a message and a key and return the encrypted message in a random order  
def encrypt_message(message, key):
  cipher_message =[]
  for line in message:
    cipher_line = []
    for word in line:
      cipher_line.append(encrypt_word(word, key))
    cipher_message.append(cipher_line)
  return cipher_message

#takes a message and a key and return the decrypted message in a random order  
def decrypt_message(message, key):
  plain_message =[]
  for line in message:
    plain_line = []
    for word in line:
      plain_line.append(decrypt_word(word, key))
    plain_message.append(plain_line)
  return plain_message

#------------FUNCTION TO GENERATE KEY------------#
# This function generates a random key used in a random substitution cipher
def generate_key():
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  upperAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  key = []
  while len(alphabet) > 0:
    key.append(alphabet.pop(random.randint(0,len(alphabet) - 1)))

  while len(upperAlpha) > 0:
    key.append(upperAlpha.pop(random.randint(0,len(upperAlpha) - 1)))
  return key
#------------ FUNCTION PRINT KEY ------------#
# This function prints the random key
def print_key(key):
  for letter_index in range(len(key) - 26):
    print(chr(letter_index + ord("a")) + " = " + key[letter_index])

################## TESTING PROGRAM #######################

key = generate_key() #displays list 
print(key)           #of random letters
print_key(key)  #displays the mapping of the key

write_file('encrypted_key', key) #writes the encrypted key in a file

print('>>>>>>>more testing>>>>>>>>>>>')
print('encrypted letter of a is:', encrypt_letter('a', key))
print('decrypted letter of o is:', decrypt_letter('o', key))
print('encrypted letter of f is:', encrypt_letter('f', key))
print('decrypted letter of d is:', decrypt_letter('d', key))
