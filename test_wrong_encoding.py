# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:11:22 2021

@author: Darlington
"""

import unittest

from wrong_encoding import dict_case,remove_dots,base_case,list_case,read_json

tests_dict = {
 "\".H.E.I.Z.G.R.U.P.P.E\"": "HEIZGRUPPE", 
 "\".T.E.M.P.E.R.A.T.U.R.E...1.F...2.2.5\"": "TEMPERATURE.1F.225",
 ".H.E.I.Z.G.R.U.P.P.E": "HEIZGRUPPE", 
 "H.E.I.Z.G.R.U.P.P.E.": "HEIZGRUPPE", 
 "\"This text is using \"quotes\".\"": "This text is using \"quotes\".",
 "T.h.i.s. is a special test case": "T.h.i.s. is a special test case", 
 "................": "........",
 "": "",
 "\"\"": "",
 "...": "." # special case
}


class TestWrongEncodingMethods(unittest.TestCase):
    
    def test_remove_dots(self):
        for key, value in tests_dict.items():
            self.assertEqual(remove_dots(key), value)
    
    def test_base_case(self):
        self.assertEqual(base_case("\"Hello\""), "Hello")
        self.assertEqual(base_case(5), 5)

    def test_list_case(self):
        arr = ["\"Hello\"", 5]
        self.assertEqual(list_case(arr), ["Hello", 5])
    
    def test_output(self):
        input_file = read_json('2000.json')
        obj=dict_case(input_file['objects'])
        self.assertDictEqual(input_file['objects'], obj)
    
if __name__ == '__main__':
    unittest.main()