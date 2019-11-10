# AES

def AES (message,encryptORdecrypt):

	key = input("Enter Password: ")
	cipher = []
	decrypted = []
	# if encrypt is called
	if encryptORdecrypt == '1':
		#enter message and key as string
		#need 4 by 4 matrix
		length = len(message)

		remainder = length%16
		num_of_blocks = int(((length-remainder)/16)+1)

		for blocks in range(num_of_blocks):
			message_block = get_message(message)
			key_block = get_key(key)
			cipher.append(encrypt(message_block,key_block))
		return ''.join(cipher)

	# if decrypt is called
	else:
		
		length = len(message)
		remainder = length%16
		num_of_blocks = int(((length-remainder)/16)+1)
		for blocks in range(num_of_blocks):
			message_block = get_message(message)
			key_block = get_key(key)
			decrypted.append(decrypt(message_block,key_block))
		
		return ''.join(decrypted)


def get_message(message):
	# only returns one of the blocks
	#convert to 4 by 4 matrix
	message = list(message)
	output = []
	#convert to ascii
	ascii_message = []
	for non_ascii in message:
		ascii_message.append(ord(non_ascii))
	while len(ascii_message)<4:
		# append with space
		ascii_message.append(32)
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

		while len(ascii_key)<4:
			# append with space
			ascii_key.append(32)
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
		output.append([ message_block[xor_row][0]^key_block[xor_row][0],
						message_block[xor_row][1]^key_block[xor_row][1],
						message_block[xor_row][2]^key_block[xor_row][2],
						message_block[xor_row][3]^key_block[xor_row][3]
			])

	#=====================================
	#STEP 2: 10 loops of sub, row shift, column mix, and XOR
	for TenLoops in range(0,10):

		#STEP 2-i row shift, 1st row, now shift, 2nd row shift by 1
		for shift_row in range(0,4):
			for shift_amount in range(0,shift_row):
				output[shift_row].append(output[shift_row].pop(0))

		#STEP 2-ii column mixer
		matrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

		for multiply_column in range(0,4):
			#matrix multiplication
			one_column = [output[0][multiply_column],output[1][multiply_column],output[2][multiply_column],output[3][multiply_column]]
			output[0][multiply_column] = int(one_column[0]*matrix[0][0])+int(one_column[1]*matrix[0][1])+int(one_column[2]*matrix[0][2])+int(one_column[3]*matrix[0][3])
			output[1][multiply_column] = int(one_column[0]*matrix[1][0])+int(one_column[1]*matrix[1][1])+int(one_column[2]*matrix[1][2])+int(one_column[3]*matrix[1][3])
			output[2][multiply_column] = int(one_column[0]*matrix[2][0])+int(one_column[1]*matrix[2][1])+int(one_column[2]*matrix[2][2])+int(one_column[3]*matrix[2][3])
			output[3][multiply_column] = int(one_column[0]*matrix[3][0])+int(one_column[1]*matrix[3][1])+int(one_column[2]*matrix[3][2])+int(one_column[3]*matrix[3][3])
		

		#STEP 2-iii XOR again
		for xor_row2 in range(0,4):
			output[xor_row2][0] = output[xor_row2][0]^key_block[xor_row2][0]
			output[xor_row2][1] = output[xor_row2][1]^key_block[xor_row2][1]
			output[xor_row2][2] = output[xor_row2][2]^key_block[xor_row2][2]
			output[xor_row2][3] = output[xor_row2][3]^key_block[xor_row2][3]

	#=============================================
	# end with row shift and XOR
	for shift_row in range(0,4):
		for shift_amount in range(0,shift_row):
			output[shift_row].append(output[shift_row].pop(0))
	for xor_row3 in range(0,4):
		output[xor_row3][0] = output[xor_row3][0]^key_block[xor_row3][0]
		output[xor_row3][1] = output[xor_row3][1]^key_block[xor_row3][1]
		output[xor_row3][2] = output[xor_row3][2]^key_block[xor_row3][2]
		output[xor_row3][3] = output[xor_row3][3]^key_block[xor_row3][3]


	#make output a string and output
	output_string = ''.join([''.join(str(x) for x in output[0]),''.join(str(x) for x in output[1]),''.join(str(x) for x in output[2]),''.join(str(x) for x in output[3])])
	return output_string


def decrypt(message_block,key_block):
	output = []
	for xor_row3 in range(0,4):
		output.append([ message_block[xor_row3][0]^key_block[xor_row3][0],
						message_block[xor_row3][1]^key_block[xor_row3][1],
						message_block[xor_row3][2]^key_block[xor_row3][2],
						message_block[xor_row3][3]^key_block[xor_row3][3]
			])

	for shift_row in range(0,4):
		for shift_amount in range(0,shift_row):
			output[shift_row].insert(0,output[shift_row].pop(3))
	#decrypt goes in reverse
	for TenLoops in range(0,10):
		#STEP 1: start with XOR
		for xor_row2 in range(0,4):
			output[xor_row2][0] = output[xor_row2][0]^key_block[xor_row2][0]
			output[xor_row2][1] = output[xor_row2][1]^key_block[xor_row2][1]
			output[xor_row2][2] = output[xor_row2][2]^key_block[xor_row2][2]
			output[xor_row2][3] = output[xor_row2][3]^key_block[xor_row2][3]


		#STEP 2: column mixer
		#encryped * inverse matrix = reverse
		inverse_matrix = [[-4/35,3/35,-11/35,17/35],[17/35,-4/35,3/35,-11/35],[-11/35,17/35,-4/35,3/35],[3/35,-11/35,17/35,-4/35]]
		for multiply_column in range(0,4):
			#matrix multiplication
			one_column = [output[0][multiply_column],output[1][multiply_column],output[2][multiply_column],output[3][multiply_column]]
			output[0][multiply_column] = round((one_column[0]*inverse_matrix[0][0])+(one_column[1]*inverse_matrix[0][1])+(one_column[2]*inverse_matrix[0][2])+(one_column[3]*inverse_matrix[0][3]))
			output[1][multiply_column] = round((one_column[0]*inverse_matrix[1][0])+(one_column[1]*inverse_matrix[1][1])+(one_column[2]*inverse_matrix[1][2])+(one_column[3]*inverse_matrix[1][3]))
			output[2][multiply_column] = round((one_column[0]*inverse_matrix[2][0])+(one_column[1]*inverse_matrix[2][1])+(one_column[2]*inverse_matrix[2][2])+(one_column[3]*inverse_matrix[2][3]))
			output[3][multiply_column] = round((one_column[0]*inverse_matrix[3][0])+(one_column[1]*inverse_matrix[3][1])+(one_column[2]*inverse_matrix[3][2])+(one_column[3]*inverse_matrix[3][3]))
		#STEP 3: row shifter
		for shift_row in range(0,4):
			for shift_amount in range(0,shift_row):
				output[shift_row].insert(0,output[shift_row].pop(3))
	#STEP 4: XOR key and ascii text
	for xor_row in range(0,4):
		output[xor_row2][0] = output[xor_row][0]^key_block[xor_row][0]
		output[xor_row2][1] = output[xor_row][1]^key_block[xor_row][1]
		output[xor_row2][2] = output[xor_row][2]^key_block[xor_row][2]
		output[xor_row2][3] = output[xor_row][3]^key_block[xor_row][3]

	original_message = []
	#STEP 5 :convert to ascii
	for ascii_row in range(0,4):
		for ascii_column in range(0,4):
			print(output)
			original_message.append(chr(output[ascii_row][ascii_column]))
	return ''.join(original_message)

message=input('enter message: ')

cipher = AES(message,'1')
print(cipher)

print('===now decrypt===')
original=AES(cipher,'0')
print(original)
