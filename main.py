from base_classes import *

MODE_NAMES = {
    1: 'Custom Builder',
    2: 'Import'
}

VIEW_MESSAGES = {
    'TITLE': '** Portfolio Stress Tester | Developed by Max Baker **',
    'WELCOME_MESSAGE1': 'Welcome to the Portfolio Stress Tester! This program is currently undergoing development. ',
    'WELCOME_MESSAGE2': f'This program currently supports 2 modes: \n (1) Custom Builder: Build your own portfolio from scratch. \n (2) Import: Import an existing portfolio with a formatted excel file.',
    'MODE_PROMPT': 'Please enter the method by which you wish to evaluate your portfolio (1/2): '    
}

class StressView():

    def __init__(self):
        self._messages = VIEW_MESSAGES
        self._mode_desc = MODE_NAMES

    def welcome(self):
        
        for message in list(self._messages.values())[:3]:
            print(message)

        self._mode = input(self._messages['MODE_PROMPT'])
        print(f'You have chosen: ({self._mode}) {self._mode_desc[int(self._mode)]}') #could perhaps write description and prompt for confirmation? (for later consideration)
        
        return self._mode
          
class StressModel():
    
    def __init__(self):
        
        self._mode = None
        #self._portfolio = Portfolio(0)
        #self._sim = Simulation(self._portfolio, 0, 0, 0, 0) # may need methods of these to change attributes later

    def confirm_mode(self, mode_input):

        self._mode = mode_input
        
class StressTester():
    
    def __init__(self):    
        self._model = StressModel()
        self._view = StressView()

    def execute(self):

        self._model.confirm_mode(self._view.welcome())

        # 2) section of code that executes method of model based on whether import/build was given
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
