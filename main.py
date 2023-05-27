#!/usr/bin/python3

import sys, os
sys.path.append('/home/pi/DocumentationTest/test_folder/')

''' This is the main file'''
from newfile import *
from newfile2 import *

print (sys.path)

def print_msg():
	''' Prints a message'''
	print ("This is a message")

def main():
	'''This is the main main function'''
	print_msg()
	new_func()
	new_func2()

if __name__ == '__main__':
	main()