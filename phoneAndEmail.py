#! python 3
# phoneAndEmail.py - finds phone number and email addresses from the clipboard
# 11/27/2017

import re
import pyperclip

phoneReg = re.compile(r'''(
	(\d{3}|\(\d{3}\))?   		# area Code
	(\s|-|\.)?           		# seperator
	(\d{3})              		# first 3 Digit
	(\s|-|\.)			# seperator
	(\d{4})				# last 4 Digit
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)


emailReg = re.compile(r'''(
	[a-zA-Z0-9._%+-]+  				# username
	@						# @ symbol
	[a-zA-Z0-9.-]+					# Domain name
	(\.[a-zA-Z]{2,4})				# dot-something
	)''',re.VERBOSE)

# TODO : find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneReg.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailReg.findall(text):
	matches.append(groups[0])


# TODO : copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(set(matches))) 	# set() removes duplication from list 
	print('Copied to clipboard:')
	print('\n'.join(set(matches)))
else:
	print('No Phone number and email')
