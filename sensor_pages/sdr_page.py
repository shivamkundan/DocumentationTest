'''
For visualizing data from RTL2832 SDR dongle.
Two modes of visualizing: line plot and waterfall.
Reverse-engineered from Adafruit's FreqShow project.
'''


#: Starting frequency
INIT_FREQ=433.0

#: Leave some top & bottom border for text and buttons
WIN_SIZE=(680,720)

class SoftwareDefinedRadioPage():
	''' For visualizing data from RTL2832 SDR dongle'''
	def __init__(self,name):
		super().__init__(name)
		pass

	def init_sdr(self):
		''' Initialize the RTL2832 SDR lib'''
		# return fscontroller, fsmodel
		pass

	def set_freq_manual(self,new_freq):
		''' Manually set a specific frequency'''
		pass

	def blit_title(self,screen):
		''' Display page title'''
		pass
	def next_frame(self,screen,curr_events,**kwargs):
		pass