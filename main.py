from base_classes import *
from constants import *

class StressModel():
    
    def __init__(self):
        
        self._mode = None
        self._portfolio = Portfolio(0)

    def set_mode(self, mode_input):
        self._mode = mode_input
    
    def get_mode(self):
        return self._mode
    
    def get_hold_no(self):
        return self._portfolio.get_hold_no()

class StressView():

    def __init__(self):
        
        self._messages = VIEW_MESSAGES
        self._prompts = PROMPT_MESSAGES
        self._mode_desc = MODE_NAMES

    def welcome(self):
        
        for message in list(self._messages.values())[:3]:
            print(message)

        self._viewmode = int(input(self._prompts['MODE_PROMPT']))

        return self._viewmode
    
    def execute_mode_open(self):
        
        print(f'\nYou have chosen: ({self._viewmode}) {self._mode_desc[self._viewmode]} \n') #could perhaps write description and prompt for confirmation? (for later consideration)
        print(f'** {self._mode_desc[self._viewmode]} ** \n')
        print(f'Thank you for choosing the {self._mode_desc[self._viewmode]}! :D')

        print('\nCommands:')

        if self._viewmode == 1:
            print(self._messages['MODE1_CMDS'])
        
        else:
            pass
    
    def mode1_view(self, model: StressModel):
        
        print(self._messages['MODE1_CMDS'])

        input(f'\nPlease enter holding number {model.get_hold_no()+1}: ')

    def mode2_view(self):
        pass

class StressTester():
    
    def __init__(self):    
        self._model = StressModel()
        self._view = StressView()

    def execute(self):

        self._model.set_mode(self._view.welcome())

        if self._model.get_mode() == 1:
            
            self._view.execute_mode_open()

            #while not self._model.halt_construction(): #some type of method returning true or false based off whether command 'D' has been entered in view
            #    pass

        # 3) section of code that prompts user for other specifications
        # 4) section of code that generates simulation (instantiates object and runs gen_summary)
        # 5) section of code that prompts whether user wants to 
        # 6) section of code printing ending message from view class
        pass

def main():   
    controller = StressTester()
    controller.execute()

if __name__=="__main__":
    main()
