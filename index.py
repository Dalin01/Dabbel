# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:56:42 2021

@author: Darlington
"""

import csv
import math
import datetime as dt

def read_files(file_path):
    data = []
    with open(file_path, encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            data.append(row)
    return data

reading = read_files('reading.csv')
prediction = read_files('prediction.csv')

def get_sec(value):
    dt_obj = dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return dt_obj.timestamp()

res = []

pointer = 1
result = []

res = {}

heading = reading[0:1][0]

def check(diff1, reading_time, value):
    global pointer
    if pointer + 1 <= len(prediction) - 1:
        
        next_time = get_sec(prediction[pointer + 1][0])
        diff2 = abs(reading_time - next_time)
    
        if diff1 <= diff2:
            diff3 = math.inf
            if pointer - 1 > 0:
                prev_time = get_sec(prediction[pointer - 1][0])
                diff3 = abs(reading_time - prev_time)
            
            for col in range(1, len(prediction) - 1):
            
                if prediction[pointer][col] == 'Null':
                    if diff2 < diff3 and prediction[pointer + 1][col] != 'Null':
                        
                        key = prediction[pointer + 1][0]+str(col)
                        if key in res:
                            t1 = get_sec(res[key][-1])
                            t2 = get_sec(prediction[pointer][0])
                            time = get_sec(res[key][-2])
                            
                            if abs(time - t1) > abs(time - t2):                                                
                                res[prediction[pointer + 1][0]+str(col)] = [value[0].replace(u'\xa0', u' '), heading[col], 
                                                                    value[col], 
                                                                    prediction[pointer + 1][col],
                                                                    prediction[pointer + 1][0],
                                                                    prediction[pointer][0]]
                        else:
                            res[prediction[pointer + 1][0]+str(col)] = [value[0].replace(u'\xa0', u' '), heading[col], 
                                                                    value[col], 
                                                                    prediction[pointer + 1][col],
                                                                    prediction[pointer + 1][0],                                                                   
                                                                    prediction[pointer][0]]
                        
                        
                        # result.append([prediction[pointer + 1][0]+str(col), value[0].replace(u'\xa0', u' '), heading[col], 
                        #                                             value[col], 
                        #                                             prediction[pointer + 1][col],
                        #                                             prediction[pointer][0]])
                    elif prediction[pointer - 1][col] != 'Null':

                        key = prediction[pointer - 1][0]+str(col)
                        if key in res:
                            t1 = get_sec(res[key][-1])
                            t2 = get_sec(prediction[pointer][0])
                            time = get_sec(res[key][-2])
                            if abs(time - t1) > abs(time - t2):
                                res[prediction[pointer - 1][0]+str(col)] = [value[0].replace(u'\xa0', u' '), heading[col], 
                                                                    value[col], 
                                                                    prediction[pointer - 1][col],
                                                                    prediction[pointer - 1][0],
                                                                    prediction[pointer][0]]
                        else:
                            res[prediction[pointer - 1][0]+str(col)] = [value[0].replace(u'\xa0', u' '), heading[col], 
                                                                    value[col], 
                                                                    prediction[pointer - 1][col],
                                                                    prediction[pointer - 1][0],
                                                                    prediction[pointer][0]]
                        # result.append([prediction[pointer - 1][0]+str(col),value[0].replace(u'\xa0', u' '), heading[col], 
                        #                                             value[col], 
                        #                                             prediction[pointer - 1][col],
                        #                                             prediction[pointer][0]])
                else:
                    key = prediction[pointer][0]+str(col)
                    # if key in res:
                    #     t1 = get_sec(res[key][-1])
                    #     t2 = get_sec(prediction[pointer][0])                       
                     
                    #     if abs(reading_time - t1) > abs(reading_time - t2):
                    #        res[key] = [value[0].replace(u'\xa0', u' '), heading[col], value[col], 
                    #                                         prediction[pointer][col], 
                    #                                         prediction[pointer][0]]
                    # else:
                    res[key] = [value[0].replace(u'\xa0', u' '), heading[col], value[col], 
                                                            prediction[pointer][col], 
                                                            prediction[pointer][0],
                                                            prediction[pointer][0]]
                    # result.append([key,value[0].replace(u'\xa0', u' '), heading[col], value[col], 
                    #                                         prediction[pointer][col], 
                    #                                         prediction[pointer][0]])

            pointer += 1
        else:
            pointer += 1
            pred_time = get_sec(prediction[pointer][0])
            diff1 = abs(reading_time - pred_time)
            check(diff1, reading_time, value)        

for row in range(1, len(reading)):
    reading_time = get_sec(reading[row][0])
    pred_time = get_sec(prediction[pointer][0])
    diff1 = abs(reading_time - pred_time)
    check(diff1, reading_time, reading[row])
print(res)
# print(result)
