from base_classes import *
from constants import *

class StressModel():
    
    def __init__(self):
        
        self._execute = True
        self._mode = None
        self._portfolio = Portfolio(0)

    def set_mode(self, mode_input):
        
        self._mode = int(mode_input)

    def check_cb_input(self, input: str):

        if input == 'C':
             return self._portfolio.get_holdings()
        
        elif input == 'R': 
            self._portfolio.reset_holdings()

        elif input in ['H', 'D']: 
            return

        else:         
            self._portfolio.add_holding(input.split(HOLD_SEPERATOR))

    def read_sim_prompts(self, sim_specs: list):
        
        self._portfolio.set_value(sim_specs[0])

        if sim_specs[-1] == 'Y':
            sim_specs[-1] = True
        
        else:
            sim_specs[-1] = False

        self._sim_specs = tuple(sim_specs[1:])
    
        self._sim = Simulation(self._portfolio, *self._sim_specs)
    
    def generate_sim_summary(self):

        self._sim.gen_summary()

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
        
        return list(self._prompts.values())[2:-1]
    
    def reprompt(self):

        return self._prompts['REPEAT_PROMPT']
    
    def execute_mode_open(self, mode: int):
        
        print(self._messages['MODE_OPEN_MESSAGE'].replace('@', str(mode))
              .replace('mode_name', self._mode_desc[mode]))

        if mode == 1:
            print(self._messages['MODE1_CMDS'])
        
        elif mode == 2:
            print(self._messages['MODE2_CMDS'])
    
    def cb_prompt_response(self, input: str, model_ret): 

        if input == 'C':

            print('\nCurrent Portfolio: \n')

            for _ in model_ret.index:
                print(f'({_}): {model_ret['Symbol'].loc[_]}.{model_ret['Exchange'].loc[_]} ({model_ret['Weighting'].loc[_]}%)')            

        elif input == 'R':
            print(self._messages['PORT_RESET'])

        elif input == 'H':
            print(self._messages['MODE1_CMDS'])

        else:
            pass
    
    def generating_sim_msg(self):

        print(self._messages['SIM_GENERATING'])

    def show_gen_summary(self, conf: int, sum_stats: tuple):

        print(self._messages['SUMMARY_1'].replace('X', str(conf)))
        print(self._messages['SUMMARY_2'].replace(
            'V', str(sum_stats[0])).replace('E', str(sum_stats[1])))
    
    def execute_exit_msg(self):

        print(self._messages['EXIT_MSG'])
    
    def get_err_msg(self):
        
        return self._messages['ERROR_MSG']

class StressTester():
    
    def __init__(self):    
        
        self._model = StressModel()
        self._view = StressView()
        self._valid_cmds = VALID_COMMANDS

    def receive_input(self, prompt_text, prompt_id):
    
        self._pass = False
        self._count = 0

        while not self._pass:

            if self._count > 0:
                print(self._view.get_err_msg())

            self._count += 1

            self._input = input(prompt_text).upper()

            if (prompt_id == 'CB_PROMPT') and (HOLD_SEPERATOR in self._input): 

                try: 
                    self._dummy = Holding(
                        *tuple(self._input.upper().split(HOLD_SEPERATOR)))
                except:
                    pass

                self._pass = True

            elif prompt_id in ['PORT_VAL_PROMPT', 'NSTEP_PROMPT',
                               'NSIM_PROMPT', 'CONF_PROMPT']: 
                
                try:
                    self._input = int(self._input)
                except:
                    pass

                self._pass = (self._input >= self._valid_cmds[prompt_id][0])

            else: 

                self._pass = (self._input in self._valid_cmds[prompt_id])
        
        return self._input
    
    def build_sim_input(self, prompts):

        self._sim_list = []

        for i,_ in enumerate(prompts):
            self._sim_list.append(self.receive_input(_, 
                                                     list(self._valid_cmds.keys())[2+i]))

        return self._sim_list

    def execute(self):
 
        self._view.execute_welcome()

        while self._model.check_execute():

            self._model.set_mode(
                    self.receive_input(
                        self._view.mode_prompt(), 'MODE_PROMPT'))
            
            self._view.execute_mode_open(self._model.get_mode())

            if self._model.get_mode() == 1:

                self._curr_input = None

                while self._curr_input != 'D':

                    self._curr_input = self.receive_input(
                        self._view.hld_enter_prompt(self._model.get_hold_no()), 'CB_PROMPT')

                    self._view.cb_prompt_response(self._curr_input, 
                                                  self._model.check_cb_input(self._curr_input))
                                               
            elif self._model.get_mode() == 2: # not yet in development
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
