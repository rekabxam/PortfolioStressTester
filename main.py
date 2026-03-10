from base_classes import *
from constants import *

class StressModel():
    
    def __init__(self):
        
        self._execute = True
        self._mode = None
        self._portfolio = Portfolio(0)
        self._cmd = None

    def set_mode(self, mode_input):
        
        self._mode = int(mode_input)

    def check_cmd(self, input): # method of checking correct holding needs work

        self._cmd = input

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

    def execute_welcome(self):
        
        for message in list(self._messages.values())[:3]:
            print(message)

    def mode_prompt(self):
        
        return self._prompts['MODE_PROMPT']
    
    def hld_enter_prompt(self, hold_no: int):

        return self._prompts['CB_PROMPT'].replace('@', hold_no)
    
    def sim_prompts(self):
        
        return list(self._prompts.keys())[2:-1] # add generating sim message somewhere
    
    def reprompt(self):

        return self._prompts['REPEAT_PROMPT']
    
    def execute_mode_open(self, mode: int):
        
        print(self._messages['MODE_OPEN_MESSAGE'].replace('@', str(mode))
              .replace('mode_name', self._mode_desc[mode]))

        if mode == 1:
            print(self._messages['MODE1_CMDS'])
        
        elif mode == 2:
            print(self._messages['MODE2_CMDS'])
    
    def mode_1_receive(self, model_msg, cmd: str):

        if cmd == 'C':
            print(model_msg)
        
        elif cmd == 'R':
            print(self._messages['PORT_RESET'])

        elif cmd == 'H':
            print(self._messages['MODE1_CMDS'])

        else:
            pass
    
    def generating_sim_msg(self):

        return self._messages['SIM_GENERATING']

    def show_gen_summary(self, conf: int, sum_stats: tuple):

        print(self._messages['SUMMARY_1'].replace('X', str(conf)))
        print(self._messages['SUMMARY_2'].replace(
            'V', str(sum_stats[0])).replace('E', str(sum_stats[1])))
    
    def execute_exit_msg(self):

        print(self._messages['EXIT_PROMPT'])
    
    def get_err_msg(self):
        
        return self._messages['ERROR_MSG']

class StressTester():
    
    def __init__(self):    
        
        self._model = StressModel()
        self._view = StressView()
        self._valid_cmds = VALID_COMMANDS

    def receive_input(self, prompt_text, prompt_id):
        
        self._input = input(prompt_text)

        while self._input not in self._valid_cmds[prompt_id]:
        
            print(self._view.get_err_msg())
            self._input = input(prompt_text)
        
        return self._input
    
    def build_sim_input(self, prompts):

        self._sim_list = []

        for i,_ in enumerate(prompts):
            self._sim_list.append(self.receive_input(_, 
                                                     self._valid_cmds.keys()[3+i]))

        return tuple(self._sim_list)

    def execute(self):
 
        self._view.execute_welcome()

        while self._model.check_execute():

            self._model.set_mode(
                    self.receive_input(
                        self._view.mode_prompt(), 'MODE_PROMPT'))
            
            self._view.execute_mode_open(self._model.get_mode())

            if self._model.get_mode() == 1:

                while self._model.get_cmd() != 'D':
                    
                    self._view.mode_1_receive(
                            self._model.check_cmd(
                                self.receive_input(
                                    self._view.hld_enter_prompt(
                                        self._model.get_hold_no()), 'CB_PROMPT')))
            
            elif self._model.get_mode() == 2:
                pass

            self._model.read_sim_prompts(
                self.build_sim_input(
                    self._view.sim_prompts()))
            
            self._view.generating_sim_msg()

            self._view.show_gen_summary(self._model.get_sim().get_conf(),
                                        self._model.generate_sim_summary())
            
            self._model.set_execute(
                self.receive_input(
                    self._view.reprompt()))
        
        self._view.execute_exit_msg()
    
def main():   
    controller = StressTester()
    controller.execute()

if __name__=="__main__":
    main()
