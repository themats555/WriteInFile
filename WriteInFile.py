#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:53:16 2023

@author: mattei
"""

class WriteInFile:
    '''Class to write in a file.
    Attributes
    ----------
        text : str
            the text to search
        new_text : list
            the list with the text to insert
        sound : str
            the sound that the animal makes
        row_number : int
            the row number after the row of the text (default 1)
    Example:
        w = WriteInFile('infile', 'OPS ', 'class_1_ops_',row_number = 3, output_file='outfile')
        w.write_in_file()
    '''
    def __init__(self,input_file, text, new_text, row_number=1, output_file='output_file'):
        self.input_file = input_file
        self.text = text
        self.new_text = new_text
        self.row_number = row_number
        self.output_file = output_file
        
    def write_in_file(self):
        fla = 0
        new_text_index = 0
        if len(self.new_text) == 0:
            print('new_text is empty, nothing to do. Bye')
            return
            
        with open(self.input_file, 'r') as f:
            with open(self.output_file,'w') as o:
                for i, line in enumerate(f):
                    if fla == self.row_number :
                        if len(self.text) >= new_text_index:
                            o.write(self.new_text[new_text_index]+'\n')
                            new_text_index += 1
                            fla = 0
                        else:
                            print(len(self.text) >= new_text_index)
                            return
                    elif fla > 0:
                        fla += 1

                    o.write(line)
                    if (self.text in line):
                        fla = 1
                
        f.close()
        o.close()
        

