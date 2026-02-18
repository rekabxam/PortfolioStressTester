from base_classes import *

VIEW_MESSAGES = {
    'TITLE': '** Portfolio Stress Tester | Developed by Max Baker **',
    'WELCOME_MESSAGE1': 'Welcome to the Portfolio Stress Tester! This program is currently undergoing development. ',
    'WELCOME_MESSAGE2': 'This program currently supports 2 modes: \n (1) Custom Builder: Build your own portfolio from scratch. \n (2) Import: Import an existing portfolio with a formatted excel file.',
    'MODE_PROMPT': 'Please enter the method by which you wish to evaluate your portfolio (1/2): '    
}

class StressView():

    def __init__(self):
        self._messages = VIEW_MESSAGES

    def welcome(self):
        
        for message in list(self._messages.values())[:3]:
            print(message)

        self._prompt = input(VIEW_MESSAGES['MODE_PROMPT'])
        
        return self._prompt
          
class StressModel():
    
    def __init__(self):
        pass #could save some time by initialising portfolio and sim objects initially

    def check_mode_prompt(self, mode_input):

        self._mode = mode_input
        print(f'{self._mode}? A great choice!')
        print('Thats all for now :)')
        
class StressTester():
    
    def __init__(self):    
        self._model = StressModel()
        self._view = StressView()

    def execute(self):
        # 1) section of code printing program execute message/design w/ input prompt from model that checks to determine what version to use (imnport/build)

        self._model.check_mode_prompt(self._view.welcome())

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
