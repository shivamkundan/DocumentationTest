#!/usr/bin/python3
'''
This is the main page, Execution begins here.
'''

import sys, os
from global_functions import *
sys.path.append(os.path.abspath('sensor_pages'))
from vis_ir_page import *

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
	# print_msg(my_msg)

	print_battery()
	print_vis_ir()

if __name__ == '__main__':
	main()