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
	:type x: float/int

	:param in_min: Least possible value for input
	:type in_min: float/int

	:param in_max: Max possible value for input
	:type in_max: float/int

	:param out_min: Least possible value for output
	:type out_min: float/int

	:param out_max: Max possible value for output
	:type out_max: float/int

	:return: Scaled value
	:rtype: float
	'''
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def blitRotate2(surf, image, topleft, angle):
	'''
	Rotate an image around its center (instead of top corner)

	:param surf: pygame surface to blit to
	:type surf: pygame.Surface

	:param image: image to be rotated
	:type image: pygame.image

	:param topleft: top-left co-ord of image
	:type topleft: int

	:param angle: rotate by this angle
	:type angle: int

	:return:
		w (*int*):
			width
		w2 (*int*):
			width2

	'''
	pass

def get_text_dimensions(text='',font_style="FONT_DIN",font_color="WHITE",style=0,font_size=28):
	''' Return size of to-be-rendered text

	:param text: Find size of this text
	:type text: string

	:param font_style: Choice of font affects dimensions, default is ``FONT_DIN``.
	:type font_style: pygame.font

	:param font_color: Color defaults to ``WHITE``
	:type font_color: pygame.Color

	:param style: ``0`` for normal (default), ``1`` for bold
	:type style: int

	:param font_size: size of text
	:type font_size: int

	:returns:
		surf (*pygame.Surface)*:
			Surface of rendered text (not used)
		w (*int*):
			width (in px) of to-be-rendered tex
		h (*int*):
			height (in px) of to-be-rendered text

	'''
	pass

def flip_buttons(pressed_button,button_list):
	''' Unselect all other buttons except the one just pressed

	:param pressed_button: Pressed button that called this function
	:type pressed_button: button
	:param button_list: List of all buttons on this page
	:type button_list: list

	'''
	pass

def update_cpu_stats(dt=None):
	'''
	Get rapsberry pi usage stats

	:returns:
		cpu_pct (*float*):
				CPU % in use
		cpu_temp (*float*):
				CPU temperature in C
	'''
	pass

def get_wifi_name():
	'''
	Returns name of wifi network if connected.

	:return wifi_name: Name of network if connected, "No WiFi" otherwise
	:rtype: *string*
	'''
	pass

def get_date_time():
	'''
	Get formatted time for top toolbar display

	:return: day, date, hour_sec
	:rtype: *string, string, string*
	'''
	pass

def blit_some_stats(screen,width,day,date,hour_sec,fps,cpu_pct,cpu_temp,wifi_name,wifi_symbol,bluetooth_img):
	'''
	These pieces of info are always displayed in the top bar or in the Okudagrams.

	:param screen: Screen surface for blitting
	:type screen: pygame.Screen

	:param width:
	:type width: int

	:param day:
	:type day: string

	:param date:
	:type date: string

	:param hour_sec:
	:type hour_sec: string

	:param fps:
	:type fps: float

	:param cpu_pct:
	:type cpu_pct: float

	:param cpu_temp:
	:type cpu_temp: float

	:param wifi_name: Name of currently connected wifi (if any)
	:type wifi_name: string

	:param wifi_symbol: Wifi symbol
	:type wifi_symbol: pygame.image

	:param bluetooth_img: Bluetooth symbol
	:type bluetooth_img: pygame.image

	'''
	pass
	# return w,w2

def adjust_gauge_lims(curr_val,gauge):
	'''
	For circular gauges. Adjusts upper/lower limits to nearest round numbers

	:param curr_val: Value to be shown on gauge
	:type curr_val: float

	:param gauge: Which gauge to update
	:type gauge: ``AA_Gauge``


	'''
	pass

