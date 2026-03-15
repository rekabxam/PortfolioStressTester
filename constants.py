HOLD_SEPERATOR = '.'

MODE_NAMES = {
    1: 'Custom Portfolio Builder',
    2: 'Portfolio CSV Importer'
}

PROMPT_MESSAGES = {
    'MODE_PROMPT': '\nPlease enter the method by which you wish to evaluate your portfolio (1/2): ',
    'CB_PROMPT' : 'Please enter Portfolio Holding @. Alternatively, enter a valid command: ',
    'PORT_VAL_PROMPT': 'Please enter the value of the entered portfolio: ',
    'NSTEP_PROMPT': 'Please enter how many steps you would like to simulate for your portfolio: ',
    'NSIM_PROMPT': 'Please enter how many simulations you would like to generate: ',
    'CONF_PROMPT': 'Please enter the confidence level (%) for which you are stress testing: ',
    'GRAPH_PROMPT' : 'Please enter whether you would like to generate a graph for the simulation (Y/N): ',
    'REPEAT_PROMPT': 'Would you like to evaluate another portfolio? (Y/N) '
}

VALID_COMMANDS = {
    'MODE_PROMPT': ['1','2'],
    'CB_PROMPT' : ['C','D','R','H'],
    'PORT_VAL_PROMPT': [0],
    'NSTEP_PROMPT': [0],
    'NSIM_PROMPT': [0],
    'CONF_PROMPT': [0],
    'GRAPH_PROMPT' : ['Y', 'N'],
    'REPEAT_PROMPT': ['Y', 'N']
}

VIEW_MESSAGES = {
    'TITLE': '** Portfolio Stress Tester | Developed by Max Baker **',
    'WELCOME_MESSAGE1': '\nWelcome to the Portfolio Stress Tester! \nThis program is currently undergoing development.',
    'WELCOME_MESSAGE2': '\nThis program currently supports 2 modes: \n (1) Custom Portfolio Builder: Build your own portfolio from scratch. \n (2) Portfolio CSV Importer: Import an existing portfolio with a formatted excel file.',
    'MODE_OPEN_MESSAGE': '\nYou have chosen: (@) mode_name\n\n** mode_name **\n\nThank you for choosing the mode_name! :D\n\nCommands:',
    'MODE1_CMDS': (f' TKR{HOLD_SEPERATOR}EXCH{HOLD_SEPERATOR}WGT: Add holding into portfolio \n C/c: See current holdings \n D/d: Finish custom portfolio building ') + 
    ('\n R/r: Reset current portfolio \n H/h: Help on commands and mode usage \n'),
    'MODE2_CMDS': 'NOTHING HERE YET',
    'PROMPT_ERROR': 'The input you entered could not be recognised. Please enter again.',
    'PORT_RESET': 'Portfolio holdings have been reset! \n',
    'SUMMARY_1': 'With a confidence level of X%, the simulation has generated the following statistics:\n',
    'SUMMARY_2': 'Value-at-Risk: V \nExpected Shortfall: E',
    'SIM_GENERATING': '\nGenerating simulation. Please wait a moment...',
    'EXIT_MSG': 'Thank you so much for using the Portfolio Stress Tester! :D \nSee you next time!',
    'ERROR_MSG': 'ERROR: The input you entered was invalid. Please enter again.'
}
