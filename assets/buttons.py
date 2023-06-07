'''
 This file contains:\n
-> A generic class for buttons\n
-> Button definitions for all pages
'''

class ButtonClass():
	''' Generic class for all buttons'''
	# def __init__(self,butt_id,button_img,alt_img,pos_x,pos_y,selected_img=None,selected_alt_img=None,cooldown_val=5,icon=None,text='',font=FONT_FEDERATION,style=0,font_size=16,name='',font_color=FONT_BLUE,selected=False,selected_color=GREEN,required_cooldown=10,align_left=False):
	# 	'''Constructor'''

	def blit_button(self,screen):
		pass

	def update_position(self,pos_x):
		pass

	def update_y_pos(self,pos_y):
		pass

	def reset_position(self):
		pass

	def press(self):
		pass

	def release(self):
		self.pressed=False
		pass
