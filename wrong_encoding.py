# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:38:04 2021

@author: Darlington
"""

import json
import re

def read_json(path):
    data = {}
    with open(path) as file:
        try:
            data = json.load(file)
        except (IOError, OSError) as e:
            data['error'] = str(e)
        finally:
            return data 

def remove_dots(string):
    substring = re.sub(r"\.(?=\.?[A-Z0-9])",'' , string)
    if substring != '' and substring[-1] == '.':
        substring = substring[:-1]
        if substring[-1] == '.' and substring[-2] == '.':
            end = round(len(substring) / 2)
            substring = substring[:end]
    return substring

def base_case(string):
    if isinstance(string, str):
        string = remove_dots(string)
        return string.strip('"')
    else:
        return string

def dict_case(dic):    
    if 'out-of-service' in dic:
        del dic['out-of-service']

    new_dic = {}
    for key, value in dic.items():
        if isinstance(value, list):
            new_dic[key] = list_case(value)
        elif isinstance(value, dict):
            new_dic[key] = dict_case(value)
        else:
            new_dic[key] = base_case(value)
    return new_dic

def list_case(arr):
    new_arr = []
    for item, value in enumerate(arr):
        if isinstance(value, list):
            new_arr.append(list_case(value))
        elif isinstance(value, dict):
            new_arr.append(dict_case(value))
        else:
            new_arr.append(base_case(value))
    return new_arr

def save_data(data):
    with open('2000_cleaned.json', 'w') as file:
        try:
            json.dump(data, file, indent=4)
        except (IOError, OSError) as e:
            print(e)

data = read_json('2000.json') # read
obj = dict_case(data['objects'])
data['objects'] = obj
save_data(data) # save





