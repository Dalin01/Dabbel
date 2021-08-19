# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:29:36 2021

@author: Darlington
"""
import datetime as dt
import random

def get_sec(value):
    dt_obj = dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return dt_obj.timestamp()

def get_sensor():
    sensors = []
    for num in range(1,501):
        if num == 1:
            sensors.append('')
        sensors.append('sensor'+str(num))
    return sensors

def takefirst(elem):
    return elem[0]

def get_reading():
    start = get_sec('2020-12-01 00:00:00')
    end = get_sec('2020-12-01 00:08:00')
    reading = []
    for num in range(3000):
        time = random.randint(start, end)
        row = [time]
        for num in range(500):
            row.append(round(random.uniform(18, 22), 1))
        reading.append(row)
    reading.sort(key=takefirst)
    for value in reading:
        time = dt.datetime.fromtimestamp(value[0]).strftime('%Y-%m-%d %H:%M:%S')
        value[0] = time
    reading.insert(0, get_sensor())
    return reading

def get_prediction():
    start = get_sec('2020-12-01 00:00:00')
    end = get_sec('2020-12-01 00:08:00')
    prediction = []
    for num in range(15000):
        time = random.randint(start, end)
        row = [time]
        for num in range(500):
            if random.randint(1, 10) > 4:
                row.append(round(random.uniform(18, 22), 1))
            else:
                row.append('Null')
        prediction.append(row)
    prediction.sort(key=takefirst)
    for value in prediction:
        time = dt.datetime.fromtimestamp(value[0]).strftime('%Y-%m-%d %H:%M:%S')
        value[0] = time
    prediction.insert(0, get_sensor())
    return prediction


