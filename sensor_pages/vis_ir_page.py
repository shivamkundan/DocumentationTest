'''
For visualizing data from TSL2591 vis/ir sensor.
'''

def print_vis_ir():
	''' Print vis/ir readings'''
	print ("vis/ir")

class LightSensorPage():
    '''
    For visualizing data from TSL2591 vis/ir sensor.

    :warning: Requires mosfet on/off control.
    '''

    def on_enter(self):
        ''' Turns on tsl_scl mosfet.'''
        pass


    def on_exit(self):
        ''' Turns off tsl_scl mosfet.'''
        pass


    def init_gauges(self):
        ''' Init gauges for this page.'''
        pass

    def blit_current_settings(self,screen):
        ''' Display current settings for this page/sensor.'''
        pass

    def flip_gain_buttons(self):
        ''' Flip button selections.'''
        pass


    def next_frame(self,screen,curr_events,**kwargs):
    	pass

    def init_buttons(self):
        ''' Init buttons for this page.

		:return: List of buttons
        '''
        pass