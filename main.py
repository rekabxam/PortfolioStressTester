from base_classes import *
from constants import *

class StressModel():
    
    def __init__(self):
        
        self._mode = None
        self._portfolio = Portfolio(0)
        self._cmd = None

    def receive_input(self, input: str):

        self._cmd = input

    def check_input(self):

        if self._cmd == 'C':
             return self._portfolio.get_holdings()
        
        elif self._cmd == 'R': 
            self._portfolio.reset_holdings()

        elif self._cmd == 'H': 
            return

        else: 

            try:
                Holding(*tuple(self._cmd.split('-'))) 
            
            except:
                return 'Error Occurred'    
                
            self._portfolio.add_holding(tuple(self._cmd.split('-')))

    def set_mode(self, mode_input):
        self._mode = mode_input
    
    def get_mode(self):
        return self._mode
    
    def get_hold_no(self):
        return str(self._portfolio.get_hold_no() + 1)

    def get_cmd(self):
        return self._cmd

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
        
        print(f'\nYou have chosen: ({self._viewmode}) {self._mode_desc[self._viewmode]} \n') 
        print(f'** {self._mode_desc[self._viewmode]} ** \n')
        print(f'Thank you for choosing the {self._mode_desc[self._viewmode]}! :D')

        print('\nCommands:')

        if self._viewmode == 1:
            print(self._messages['MODE1_CMDS'])
        
        elif self._viewmode == 2:
            print(self._messages['MODE2_CMDS'])
    
    def mode_1_prompt(self, hold_no: int):

        return input(self._prompts['CB_PROMPT'].replace('@', hold_no))
    
    def mode_1_receive(self, model_msg, cmd: str):

        #if model_msg == 'Error Occurred': #need diff way of returning error
        #    print(self._messages['ERR_ADDING']) 

        if cmd == 'C':
            print(model_msg)
        
        elif cmd == 'R':
            print(self._messages['PORT_RESET'])

        elif cmd == 'H':
            print(self._messages['MODE1_CMDS'])

        else:
            pass

class StressTester():
    
    def __init__(self):    
        self._model = StressModel()
        self._view = StressView()

    def execute(self):

        self._model.set_mode(self._view.welcome())    
        self._view.execute_mode_open()

        if self._model.get_mode() == 1:

            while self._model.get_cmd() != 'D':
                
                self._model.receive_input(
                    self._view.mode_1_prompt(self._model.get_hold_no()))
                
                self._view.mode_1_receive(
                    self._model.check_input(), self._model.get_cmd())
        
        elif self._model.get_mode() == 2:
            pass

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
