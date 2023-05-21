#!/usr/bin/python3

''' This is the main file'''
import sys, os
sys.path.insert(0,os.path.abspath('/home/pi/DocumentationTest/test_folder/'))
sys.path.insert(0,os.path.abspath('/home/pi/DocumentationTest/'))

from newfile import *
from newfile2 import *

def print_msg():
	''' Prints a message'''
	print ("This is a message")

def main():
	'''This is the main main function'''
	print_msg()
	new_func()
	newfile2()

if __name__ == '__main__':
	main()