from base_classes import *
from constants import *

class StressModel():
    
    def __init__(self):
        
        self._execute = True
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

    def read_sim_prompts(self, sim_specs: list):
        
        self._portfolio.set_value(sim_specs[0])

        if sim_specs[-1] == 'Y':
            sim_specs[-1] = True
        
        else:
            sim_specs[-1] = False

        self._sim_specs = tuple(sim_specs[1:])
        
        print(self._sim_specs)
        self._sim = Simulation(self._portfolio, *self._sim_specs)
    
    def generate_sim_summary(self):

        self._sim.gen_sim()

        return self._sim.get_summary()
    
    def set_execute(self, exec_input: str):

        if exec_input == 'N':
            self._execute = False
    
    def check_execute(self):
        return self._execute
    
    def get_sim(self):
        return self._sim
    
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
        print(f'** {self._mode_desc[self._viewmode]} ** \n') #perhaps put these into constants strings collection
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
    
    def execute_sim_prompts(self):

        self._spec_inputs = []
        
        for _ in list(self._prompts.keys())[2:]:
            self._spec_inputs.append(input(self._prompts[_]))

        print('\nGenerating simulation. Please wait a moment...')
        
        return self._spec_inputs
    
    def show_gen_summary(self, conf: int, sum_stats: tuple):

        print(self._messages['SUMMARY_1'].replace('X', str(conf)))
        print(self._messages['SUMMARY_2'].replace(
            'V', str(sum_stats[0])).replace('E', str(sum_stats[1])))

    def check_reprompt(self):

        return input(self._prompts['REPEAT_PROMPT'])
    
    def execute_exit_msg(self):

        print(self._messages['EXIT_PROMPT'])

class StressTester():
    
    def __init__(self):    
        self._model = StressModel()
        self._view = StressView()

    def execute(self):
 
        while self._model.check_execute():

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

            self._model.read_sim_prompts(self._view.execute_sim_prompts())

            self._view.show_gen_summary(self._model.get_sim().get_conf(),
                                        self._model.generate_sim_summary())
            
            self._model.set_execute(self, self._view.check_reprompt())
        
        self._view.execute_exit_msg()
    
def main():   
    controller = StressTester()
    controller.execute()

if __name__=="__main__":
    main()
