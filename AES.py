# AES

def AES (message):
	key = input("Enter Key: ")

	cipher_string = ''
	#enter message and key as string
	#need 4 by 4 matrix
	length = len(message)
	remainder = length%16
	num_of_blocks = ((length-remainder)/16)+1
	for blocks in range(num_of_blocks):
		message_block = get_message(message)


def get_message(message):
	# only returns one of the blocks
	#convert to 4 by 4 matrix
	message = list(message)
	output = []
	#convert to ascii
	ascii_message = []
	for non_ascii in message:
		ascii_message.append(ord(non_ascii))

	for row_of_4 in range(4):
		output.append((ascii_message[0:4]))
		#delete thatthe first 4
		del ascii_message[0:4]
		while len(ascii_message)<4:
			# append with space
			ascii_message.append(32)
	return output

def get_key(key):
	#gets the key in a block
	if len(key)<=16:
		#must input ascii number in the block
		key = list(key)
		output = []
		#convert to ascii
		ascii_key = []
		for non_ascii in key:
			ascii_key.append(ord(non_ascii))

		for row_of_4 in range(4):
			output.append((ascii_key[0:4]))
			#delete thatthe first 4
			del ascii_key[0:4]
			while len(ascii_key)<4:
				# append with space
				ascii_key.append(32)
	elif len(key)>16:
		# if length is longer than 16, need to group it
		key = list(key)
		output = []
		#convert to ascii
		ascii_key = []
		for non_ascii in key:
			ascii_key.append(ord(non_ascii))

		for row_of_4 in range(4):
			output.append((ascii_key[0:4]))
			#delete thatthe first 4
			del ascii_key[0:4]
			#add remaining to other first few

		while len(ascii_key)!=0:
			# add remainig ones to first couple
			for row in range(0,4):
				for column in range(0,4):
					if len(ascii_key)==0:
						break
					output[row][column] += ascii_key[0]
					del ascii_key[0]
	return output

	#NOTE formating block[row][column]
def encrypt(message_block,key_block):
	output = []
	#STEP 1: XOR key and ascii text
	for xor_row in range(0,4):
		output.append([message_block[xor_row][0]^key_block[xor_row][0],
						message_block[xor_row][1]^key_block[xor_row][1]
						message_block[xor_row][2]^key_block[xor_row][2]
						message_block[xor_row][3]^key_block[xor_row][3]
			])
def decrypt(cipher,key):
	pass
