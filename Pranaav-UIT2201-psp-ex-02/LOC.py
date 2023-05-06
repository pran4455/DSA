# -*- coding: utf-8 -*-


'''
This module contains python functions use a series of functions
to find the total lines of code by excluding all comments, blank
lines as well as documentation in all files in a given folder
as well as its subdirectories.

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 18 2023

Revised on Wed Apr 30 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import ast
import os


# Define a function to extract function names from the AST
def extract_functions(file_path):

    '''
    Given function retrieves all the file names in a
    given file path.

    args:
        file_path: file in which we need to find functions.

    returns:
        list of function names.
    
    '''

    function_list = []
    with open(file_path,'r',encoding='utf-8',errors='replace') as file:
        node = ast.parse(file.read())
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            function_list.append(item.name)
    return function_list



def get_function_lengths(filepath):

    '''
    
    Counts the number of lines in a given function
    at the given file path.

    args:
        filepath: the path to the file in which function
        lines need to be counted.
    
    returns:
        Total number of lines in a function.
    
    '''

    with open(filepath, 'r') as file:
        lines = file.readlines()
        functions = {}
        start_line = None
        
        for i, line in enumerate(lines):
            if line.startswith('def'):
                if start_line is not None:
                    functions[name] = i - start_line - 1
                name = line.split()[1].split('(')[0]
                start_line = i
        if start_line is not None:
            functions[name] = len(lines) - start_line - 1

    return functions


def count_ignore_doc(f_path,fnames):

    '''
    
    It takes in file path and a file name and finds
    whether a given line of code within each file
    is a docstring, comment or a blank line and also
    counts the number of lines in each function inside
    a class as well as normal functions.

    args:
        f_path: the file path.
        fnames: the list containing names of
        functions.
    
    returns:
        Total number of lines and number of lines in a
        file of only functions in a tuple.
    
    '''

    counts = []
    mains_list = []
    for fname in fnames:
        file_path = os.path.join(f_path,fname)
        functions = get_function_lengths(file_path)

        with open(file_path,'r',encoding='utf-8',errors='replace') as main_file:

            main_file.seek(0)

            is_docstring = False
            count = 0
            comment_count = 0
            space_count = 0
            lines = main_file.readlines()

            for line_ind in range(len(lines)):

                lines[line_ind]=lines[line_ind].lstrip()

                if len(lines[line_ind]) == 0:
                    if not is_docstring:
                        space_count += 1
                        continue

                if lines[line_ind].startswith('#'):
                    comment_count += 1
                    continue

                if lines[line_ind].count("'''") == 1 or lines[line_ind].count('"""') == 1:
                    is_docstring = ~(is_docstring)

                if not is_docstring:
                    if lines[line_ind].count('"""') == 2 or lines[line_ind].count("'''") == 2:
                        continue
                    else:
                        count += 1

            counts.append(count)
            mains_list.append(functions)
        
    return (counts,mains_count(mains_list))


def mains_count(main_list):

    '''
    Counts the number of lines in a given mains_list
    containing dictionary of function lengths.

    args:
        main_list: the list containing dictionary of
        lengths of functions.
    
    returns:
        Total number of lines.
    
    '''

    count = 0
    for i in main_list:
        for j in i.values():
            count += j

    return count


def py_LOC_count(file_path):

    '''
        This function takes in a file path as input and returns
        the count of number of lines of code and lines of
        functions.

        The input is not modified and there are no side effects.

        args:
            file_path: the file path

        Returns:
            The counts of number of lines of code and number of
            lines of function in class as well as normal functions.
        
    '''  

    global Total_vals

    files_path_dict = {}
    for dir_path, dir_names, file_names in os.walk(file_path):
        files_path_dict[dir_path] = file_names

    Total_lines = 0
    for path in files_path_dict.keys():
        pathway = path
        files_to_count = files_path_dict.get(path)
        val = count_ignore_doc(pathway,files_to_count)
        for i in val[0]:
            Total_lines += i
        Total_vals.append(val)
        

    return (Total_lines,Total_vals)


#driver code 
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #writing the file path
    py_path = r'D:\computer science\xml'

    # Open the Python file and read the contents

    Total_vals = []
    total_count, lines_in_each_file = py_LOC_count(py_path)

    print("Total number of lines is:",total_count)
    print()

    print("Number of lines in each file in each directory is:\n")
    print()

    for val in lines_in_each_file:
        print(val[0])
    print()

    print("Number of lines of functions in each directory is:\n")
    for val in lines_in_each_file:
        print(val[1])
    print()
    #end of code