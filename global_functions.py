'''
Contains functions invoked by several different parts of the code.
'''


def print_global():
	''' Prints the battery level'''
	print ("Printing global...")


def my_map(x,in_min,in_max,out_min,out_max):
	'''
	Standard mapping formula. Used in many places

	:note: Standard formula
	:custom: Custom
	:param x: Input value to be mapped
	:param in_min: Least possible value for input
	:param in_max: Max possible value for input
	:param out_min: Least possible value for output
	:param out_max: Max possible value for output
	:return: Scaled value
	'''
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def blitRotate2(surf, image, topleft, angle):
	'''
	Rotate an image around its center

	:return: surf,w,h
	'''
	pass

def get_text_dimensions(text='',font_style="FONT_DIN",font_color="WHITE",style=0,font_size=28):
	''' Return size of to-be-rendered text'''
	pass

def flip_buttons(pressed_button,button_list):
	''' Unselect all other buttons except the one just pressed'''
	pass

def update_cpu_stats(dt=None):
	''' Get rapsberry pi usage stats'''
	pass

def get_wifi_name():
	''' Check for connected wifi network. Return network name'''
	pass

def get_date_time():
	''' Get formatted time for top toolbar display'''
	pass

def blit_some_stats(screen,width,day,date,hour_sec,fps,cpu_pct,cpu_temp,wifi_name,wifi_symbol,bluetooth_img):
	''' These pieces of info are always displayed in the top bar or in the Okudagrams'''
	pass
	# return w,w2

def adjust_gauge_lims(curr_val,gauge):
	''' For circular gauges. Adjusts upper/lower limits to nearest round numbers'''
	pass

