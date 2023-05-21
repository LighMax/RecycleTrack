import serial
import re
from update_card import *
from get_card import *
from create_card import *

ser = serial.Serial(
	port = 'COM4',
	baudrate=9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 2
)


dataString = ""
card_uid2 = ""
check_code = 0
uid_exists = 0
cof_count = 10

while 1:

	if(ser.in_waiting > 0):

		dataString = ser.readline()
		decodeData = dataString.decode('Ascii')

		decodeData = decodeData[:len(decodeData) - 2] + decodeData[len(decodeData) - 1]
		decodeData = decodeData[:len(decodeData) - 1]
		decodeData = decodeData.strip()
		decodeData = decodeData.lower()
		decodeData = decodeData.replace(" ", "")

		print('data = ' + decodeData + ' len = ' + str(len(decodeData)))


		if(check_code == 1):

			print("Count = " + decodeData)

			if(uid_exists == 0):

				before_count = get_card_by_uid(card_uid)['scores']
				name = get_card_by_uid(card_uid)['phone']
				print("Before2 = " + str(before_count))

				record = {
					'card_id' : card_uid,
					'phone' : name,
					'scores' : before_count + (int(decodeData) * cof_count),
					'uid' : card_uid
				}

				update_card_by_uid(card_uid, record)

			else:

				before_count = get_card_by_uid(card_uid)['scores']
				name = get_card_by_uid(card_uid)['phone']
				print("Before = " + str(before_count))

				record = {
					'card_id' : card_uid,
					'phone' : name,
					'scores' : before_count + (int(decodeData) * cof_count),
					'uid' : card_uid
				}

				update_card_by_uid(card_uid, record)

			check_code = 0

		else:

			#set_new_card('666666', 0)

			uid_list = get_all_card()

			card_uid = decodeData
			regex_res = re.match(r'[a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9]', card_uid)

			if(regex_res != None and card_uid.find("firmwareversion") == -1 and card_uid not in uid_list):

				print("SET NEW CARD")
				print(uid_list)
				set_new_card(card_uid, 0)
				check_code = 1
				uid_exists = 0

			else:

				for card_id in uid_list:

					if(card_id == decodeData):

						card_uid = card_id
						uid_exists = 1
						check_code = 1

						print(uid_list)

						print("UID is Valid")
						ser.write(b'status_ok')

						break
