# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:03:32 2021

@author: Darlington
"""

import unittest
from index import get_sec, read_files, match_prediction

expected_result = [['', 'Sensor', 'Temperature', 'Prediction'], 
                   ['2020-12-01 00:11:34', 'Sensor1', '20.1', '20.2'], 
                   ['2020-12-01 00:00:00', 'Sensor2', '19.4', '19.5'], 
                   ['2020-12-01 00:00:00', 'Sensor3', '21.3', '21.1'], 
                   ['2020-12-01 00:00:00', 'Sensor4', '20.5', '20.3'], 
                   ['2020-12-01 00:20:00', 'Sensor2', '19.4', '19.6'], 
                   ['2020-12-01 00:11:34', 'Sensor4', '20.4', '20.2'], 
                   ['2020-12-01 00:20:00', 'Sensor1', '20', '20'], 
                   ['2020-12-01 00:20:00', 'Sensor4', '20.6', '20.5']]

class TestWrongEncodingMethods(unittest.TestCase):

    def test_sec(self):
        self.assertEqual(get_sec("2020-12-01 00:00:00"), 1606777200.0)

    def test_algorithm(self):
        reading=read_files('reading.csv')
        prediction=read_files('prediction.csv')
        self.assertEqual(match_prediction(reading, prediction), expected_result)

if __name__ == '__main__':
    unittest.main()



