#!/usr/bin/python3

''' This is the main file'''
import sys, os
sys.path.insert(0,os.path.abspath('/home/pi/DocumentationTest/test_folder/'))

from newfile import *
import newfile2
from newfile2 import *

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