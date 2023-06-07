#!/usr/bin/python3
"""
This is the main page, Execution begins here.
"""


import sys, os
sys.path.append('/home/pi/DocumentationTest/sensor_pages/')
from newfile import *
from newfile2 import *
from newfile3 import *



print (sys.path)

def print_msg():
	"""
	Prints a message

	:param user_data: The Gtk.LinkButton that should be opened when the Gtk.EventBox is clicked.
	:param other: Another param.
	:return: None
	"""
	print ("This is a message")

def main():
	'''This is the main main function'''
	print_msg()
	new_func()
	new_func2()

if __name__ == '__main__':
	main()