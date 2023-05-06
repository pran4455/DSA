# -*- coding: utf-8 -*-


"""

This module provides a series of functions that traverses through
given file path and opens all subfolders and writes all the contents
of any text file present in any of the subfolders present within the
file path into a different text file and then find the occurence of
all words in the said text file [final file containing all the words
from all the different files]. This is a part of the excercises given
under the course UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 11 2023

Revised on Wed Apr 17 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import os


#function for calculating count of all words in a file
def word_histogram(filename,filepath):

    """

    The given function takes in the filename or filepath
    for a text file and reads the contents and gives a
    count of all the words present in it and writes all the
    pairs of words and counts into a separate text file.

    The input file is not mutated in any way and there are
    no side effects.

    args:
        filename: the name/path of the file to find the count
        of words.
        filepath: the name/path of the histogram file.

    Returns:
        The counts of all words present in the file in a
        dictionary.

    """

    with open(filename,'r',encoding='utf-8',errors='replace') as file:
        lines = file.read().split()  #reading all lines in the file
        histogram = {}
        for word in lines:
            if word in histogram.keys():
                histogram[word] += 1  #increasing count of word
            else:
                histogram[word] = 1

    histogram_item_list = [[str(key),str(val)] for key,val in histogram.items()]

    with open(filepath,'a',encoding='utf-8',errors='replace') as write_file:
        for word in histogram_item_list:
            key,val = word
            to_write = str(key+':'+val+'\n')
            write_file.write(to_write)

    return histogram
#end of word_histogram function


#function to get all the text files within a folder
def text_write(file_path,main_textfile_path):

    """
    
    This is a function that takes in a file path as the input
    and finds all the text files and calls a function 
    mass_write(files,pathway) to write down all their contents
    into a specific text file.

    The input file path is not modified in any way and there
    are no side effects.

    args:
        file_path: the path of file where we have to find text
        files

    Returns:
        None

    """

    files_path_dict = {}
    
    for (dir_path, dir_names, file_names) in os.walk(file_path):
        files_path_dict[dir_path] = file_names

    files_to_write = []
    for path in files_path_dict.keys():
        pathway = path
        files_to_write=(files_path_dict.get(path))
        mass_write(files_to_write,pathway,main_textfile_path)
#end of function text_write


#function to write into text file
def mass_write(files,pathway,main_textfile_path):

    """
    
    This is a function that takes in a file paths of multiple text
    files in a list as the input and writes down all the contents 
    of all text files present in the list into a main text file.

    The input list with file names is not modified in any way and
    there are no side effects.

    args:
        file_path: the path of file where we have to find text
        files

    Returns:
        A list containing names of all text files.

    """

    with open(main_textfile_path,'a',encoding='utf-8',errors='replace') as main_file:
        for file in files:
            filename = f'{pathway}/{file}'
            with open(filename,'r',encoding='utf-8',errors='replace') as read_file:
                lines = read_file.readlines()
                main_file.writelines(lines)
#end of function mass_write


#function for displaying words starting with a certain prefix
def find_prefix(histogram_path,prefix):

    '''
    This is a function that takes in the path of words-histogram.txt
    and reads its contents and returns a list of words starting with
    a certain prefix, along with their counts. The words will be
    displayed in the decreasing order of their appearance count.

    The input is not modified in any way and there are no side
    effects.

    args:
        histogram_path: the path for the file words-histogram.txt
        prefix: the prefix that each word must start with

    Returns:
        A list containing words starting with prefix and their
        counts arranged in decreasing order of appearance count.
    
    '''

    with open(histogram_path,'r',encoding='utf-8',errors='replace') as histo_file:
        words = histo_file.readlines()
        word_and_count_list = []
        for word in words:
            word_list = word.split(':')
            word_list[-1] = int(word_list[-1])
            appending_list = [word_list[0],word_list[-1]]
            word_and_count_list.append(appending_list)

    prefix_words = {}

    for word_and_count in word_and_count_list:
        if word_and_count[0].startswith(prefix):
            prefix_words[word_and_count[0]] = word_and_count[1]
    
    items = [item for item in prefix_words.items()]
    count_val = [count[1] for count in items]
    
    count_val.sort(reverse=True)

    count_total = 0
    prefix_words_with_count = []
    while count_total < len(items):
        for word in items:
            if word[1] == count_val[count_total]:
                prefix_words_with_count.append(word)
        
        count_total+=1

    if len(prefix_words_with_count) == 0:
        return [(prefix,'Word does not exist')]
    else:
        return prefix_words_with_count
#end of function find_prefix


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    file_path = r'D:\computer science\DSA\python-3.11.3-docs-text'  #shows position of the file containing subfolders and textfiles
    path_for_text_file = r'D:\computer science\DSA\Pranaav-UIT2201-psp-ex-01\words.txt'  #signifies the position of the main text file
    path_for_histogram = r'D:\computer science\DSA\Pranaav-UIT2201-psp-ex-01\words-histogram.txt'

    print("Writing into main text file words.txt at path:",path_for_text_file)
    #text_write(file_path,path_for_text_file)
    print()  #for spacing

    print("Now finding the histogram count of all words in the main text file words.txt")
    #histogram_dict = word_histogram(path_for_text_file,path_for_histogram)
    print()
    
    prefix_word = input("Enter the prefix to display the words and their count:")
    for word,count in find_prefix(path_for_histogram,prefix_word):
        print(f"Word is: {word} and Count is: {count}")
    #end of code
