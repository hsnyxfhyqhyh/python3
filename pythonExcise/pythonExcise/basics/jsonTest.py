import json

import sys

from pprint import pprint       # remember, this is different from the print, so the structure of the json data will be kept.

input_filename= "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\basics\\data_input.json"
output_filename= "C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\basics\\data_output.json"

#load the data from a json file. 

with open(input_filename) as data_file:
    data_item = json.load(data_file)

pprint(data_item)
print(data_item['parameters'][0]['id'])

data_item['parameters'][0]['id'] = "ying"
print (type(data_item))

outputFile = open(output_filename, 'w', encoding='utf-8')
json.dump(data_item, outputFile, ensure_ascii = False)


