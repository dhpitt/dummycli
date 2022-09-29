# Basic command line interface

import sys

from InquirerPy import inquirer
from InquirerPy.exceptions import InvalidArgument
from InquirerPy.validator import PathValidator

from pyfiglet import Figlet

def main():

    f = Figlet(font='slant')
    print(f.renderText('dummyCLI'))

    # Eventually configurable
    available_models = ['BERT_mini', 'BERT_regular', 'BERT_large', 'BagOfWords'] 
    available_attacks = ['Homoglyph substitution', 'Misspellings', 'Less common synonym', 'Rubber ducky 3000']
    available_datasets = ['Yelp reviews', 'Broken GitHub code', 'RottenTomatoes']

    # .execute() stores responses as output vars
    action = inquirer.select(message='Select an action:', choices=["Train a model", "Attack a model", "Adversarial training"]).execute()
    model = inquirer.select(message='Select a model:', choices=available_models).execute()
    dataset = inquirer.select(message='Select a dataset:', choices=available_datasets).execute()

    if action in ['Train a model', "Adversarial training"]:
        epochs = inquirer.text(message='Number of training epochs:').execute()
    if action in ['Attack a model', 'Adversarial training']:
        attack_type = inquirer.select(message='Attack type:',choices=available_attacks).execute().lower()

    confirm = inquirer.confirm(message='Confirm?').execute()

    #  Required try/except in case something breaks
    try:
        if confirm:
            output = ''
            if action in ['Train a model', "Adversarial training"]:
                output += f'Training {model} for {epochs} epochs on {dataset}'
            if action == 'Adversarial training':
                output += f' in the presence of the {attack_type.lower()} attack'
            elif action == 'Attack a model':
                output += f'Attacking {model} on {dataset} using the {attack_type} attack'
            print(output + '...')
        else:
            print('OK, aborting.')
            
    except:
        print('Error: invalid option')
