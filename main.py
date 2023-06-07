#!/usr/bin/python3
"""
This is the main page, Execution begins here.

:note:: this is a note
"""

from batt_page import *

def print_msg(msg):
	"""
	Prints a message

	:param msg: message to be printed
	:param other: Another param.
	:return: None
	"""
	print (msg)

def main():
	'''This is the main main function'''
	print_msg(my_msg)

	print_battery()

if __name__ == '__main__':
	main()