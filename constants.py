
MODE_NAMES = {
    1: 'Custom Portfolio Builder',
    2: 'Portfolio CSV Importer'
}

PROMPT_MESSAGES = {
    'MODE_PROMPT': '\nPlease enter the method by which you wish to evaluate your portfolio (1/2): ',
    'CB_PROMPT' : 'Please enter holding number @ (Format: ticker-type-weighting) or enter a valid command: ',
    'NSTEP_PROMPT': 'Please enter how many steps you would like to simulate for your portfolio: ',
    'NSIM_PROMPT': 'Please enter how many simulations you would like to generate: ',
    'CONF_PROMPT': 'Please enter the confidence level (%) for which you are stress testing: ',
    'GRAPH_PROMPT' : 'Please enter whether you would like to generate a graph for the simulation (Y/N): '
}

VIEW_MESSAGES = {
    'TITLE': '** Portfolio Stress Tester | Developed by Max Baker **',
    'WELCOME_MESSAGE1': '\nWelcome to the Portfolio Stress Tester! \nThis program is currently undergoing development.',
    'WELCOME_MESSAGE2': f'\nThis program currently supports 2 modes: \n (1) Custom Portfolio Builder: Build your own portfolio from scratch. \n (2) Portfolio CSV Importer: Import an existing portfolio with a formatted excel file.',
    'MODE1_CMDS': (' C: See current holdings \n D: Finish custom portfolio building ') + 
    ('\n R: Reset current portfolio \n H: Help on commands and mode usage \n'),
    'MODE2_CMDS': 'NOTHING HERE YET',
    'ERR_ADDING': 'An error was encountered while adding this holding. Please check ticker is correct and try again. ',
    'PORT_RESET': '\n Portfolio holdings have been reset! \n'
}
