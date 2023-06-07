#!/usr/bin/python3
'''
This is the main page, Execution begins here.
'''

import sys, os
from global_functions import *
sys.path.append(os.path.abspath('sensor_pages'))
sys.path.append(os.path.abspath('assets'))
sys.path.append(os.path.abspath('resources'))
sys.path.append(os.path.abspath('general_pages'))
sys.path.append(os.path.abspath('freqshow_code'))

from sensor_pages import *
from general_pages import *
from assets import *
from resources import *
from freqshow_code import *

#: A global variable
glob_var=0

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

	print_vis_ir()
	print_fonts()
	mappings_print()
	print_dev()
	print_freq()


if __name__ == '__main__':
	main()