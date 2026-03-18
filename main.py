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

        return self._sim.gen_summary()
    
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
    
    def reset_portfolio_holdings(self):

        self._portfolio.reset_holdings()

class StressView():

    def __init__(self):
        
        self._messages = VIEW_MESSAGES
        self._prompts = PROMPT_MESSAGES
        self._mode_desc = MODE_NAMES

    def get_text(self, type_id: str, msg_id: str): 

        if type_id == 'msg':
            return self._messages[msg_id]
        
        elif type_id == 'prompt':
            return self._prompts[msg_id]
    
    def output_text(self, text: str, pholder: str, new: str, output: bool):

        if output:
            print(text.replace(pholder, new))

        return text.replace(pholder, new)

    def output_mode_open(self, mode: int):
        
        self.output_text(
            self.get_text('msg', 'MODE_OPEN_MESSAGE'), 'mode_name', self._mode_desc[mode], True)

        if mode == 1:
            self.output_text(
                self.get_text('msg', 'MODE1_CMDS'), *('','',True))
        
        elif mode == 2:
            self.output_text(
                self.get_text('msg', 'MODE2_CMDS'), *('','',True))
    
    def cb_prompt_response(self, input: str, model_ret): 

        if input == 'C':

            if not model_ret.empty: 
                
                self.output_text(
                    self.get_text('msg', 'CURRENT_PORTFOLIO'), *('','',True))
        
                for _ in model_ret.index:
                    
                    self._entry = ((self.output_text(
                        self.get_text('msg', 'MODEL_SYMBOL'), *('@',model_ret['Symbol'].loc[_],False))) 
                    + (self.output_text(
                        self.get_text('msg', 'MODEL_EXCH'), *('@',model_ret['Exchange'].loc[_],False)))
                    + (self.output_text(
                        self.get_text('msg', 'MODEL_WGT'), *('@',model_ret['Weighting'].loc[_],False))))

                    self.output_text((f'({_+1}) '+ self._entry), *('','', True))
    
            else:
                self.output_text(
                    self.get_text('msg', 'EMPTY_PORT'), *('','',True))
        
        elif input == 'R':
            self.output_text(
                    self.get_text('msg', 'PORT_RESET'), *('','',True))
        
        elif input == 'H':
            self.output_text(
                    self.get_text('msg', 'MODE1_CMDS'), *('','',True))
        
        else:
            pass
    
    def sim_prompts(self): 

        return [self.get_text('prompt', _) 
                for _ in list(self._prompts.keys())[2:-1]]
    
    def show_gen_summary(self, conf: int, sum_stats: tuple):

        self._entries = (conf, *(sum_stats))

        for i, _ in enumerate(['SUMMARY_1', 'SUMMARY_2', 'SUMMARY_3']):
            self.output_text(self.get_text('msg', _),'@', str(self._entries[i]), True)

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
                self._view.output_text(
                    self._view.get_text('msg', 'ERROR_MSG'), *('', '', True))

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
 
        self._view.output_text(self._view.get_text('msg', 'PROGRAM_OPEN_MSG'), *('', '', True))

        while self._model.check_execute():

            self._mode_choice = self.receive_input(
                        self._view.output_text(self._view.get_text('prompt', 'MODE_PROMPT'), *('', '', False)), 'MODE_PROMPT')

            self._model.set_mode(self._mode_choice)

            self._view.output_mode_open(self._model.get_mode())

            if self._model.get_mode() == 1:

                self._curr_input = None

                while self._curr_input != 'D':

                    self._curr_input = self.receive_input(
                        self._view.output_text(self._view.get_text('prompt', 'CB_PROMPT'), *('@', self._model.get_hold_no(), False)),
                        'CB_PROMPT')

                    self._view.cb_prompt_response(self._curr_input, 
                                                  self._model.check_cb_input(self._curr_input))
                                               
            elif self._model.get_mode() == 2: 
                pass

            self._model.read_sim_prompts(
                self.build_sim_input(
                    self._view.sim_prompts()))
            
            self._view.output_text(self._view.get_text('msg', 'SIM_GENERATING'), *('', '', True))

            self._view.show_gen_summary(self._model.get_sim().get_conf()*100,
                                        self._model.generate_sim_summary())

            self._model.set_execute(
                self.receive_input(
                    self._view.output_text(self._view.get_text('prompt', 'REPEAT_PROMPT'), *('', '', False)), 'REPEAT_PROMPT'))
            
            self._model.reset_portfolio_holdings()
        
        self._view.output_text(self._view.get_text('msg', 'EXIT_MSG'), *('', '', True))
    
def main():   
    controller = StressTester()
    controller.execute()

if __name__=="__main__":
    main()
