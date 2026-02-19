
MODE_NAMES = {
    1: 'Custom Portfolio Builder',
    2: 'Portfolio CSV Importer'
}

PROMPT_MESSAGES = {
    'MODE_PROMPT': 'Please enter the method by which you wish to evaluate your portfolio (1/2): ',
    'CB_PROMPT' : 'Please enter holding number @ (Format: ticker-weighting) or enter a valid command: '
}

VIEW_MESSAGES = {
    'TITLE': '** Portfolio Stress Tester | Developed by Max Baker **',
    'WELCOME_MESSAGE1': 'Welcome to the Portfolio Stress Tester! \nThis program is currently undergoing development.',
    'WELCOME_MESSAGE2': f'This program currently supports 2 modes: \n (1) Custom Portfolio Builder: Build your own portfolio from scratch. \n (2) Portfolio CSV Importer: Import an existing portfolio with a formatted excel file.',
    'MODE1_CMDS': ('\nC: See current holdings \nD: Finish custom portfolio building ') + 
    ('\nR: Reset current portfolio \nH: Help on commands and mode usage'),
}
