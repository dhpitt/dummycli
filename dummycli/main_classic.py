import sys

from InquirerPy import prompt
from InquirerPy.exceptions import InvalidArgument
from InquirerPy.validator import PathValidator

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('dummyCLI'))

def is_upload(result):
    return result[0] == "Upload"

model_type = ['BERT_mini', 'BERT_regular', 'BERT_large', 'BagOfWords']

questions = [
    {
        "message": "Select an action:",
        "type": "list",
        "choices": ["Train a model", "Attack a model", "Adversarial training"],
        "name": 'action',
    },
    {
        "message": "Select a model:",
        "type": "fuzzy",
        "choices": model_type,
        "name": "model",
    },
    {"message": "Confirm?", "type": "confirm", "default": False, 'name':'confirmation'},
]

try:
    result = prompt(questions, vi_mode=True)
    #print(result)
    if result['action'] == 'Attack a model': 
        model = result['model']
        print(f'Attacking {model}...')
    elif result['action'] == 'Train a model': 
        print(f'Training {model}...')
    elif result['action'] == 'Adversarial training': 
        print(f'Training {model} on attacked data...')
except InvalidArgument:
    print("No available choices")

# Download or Upload the file based on result ...