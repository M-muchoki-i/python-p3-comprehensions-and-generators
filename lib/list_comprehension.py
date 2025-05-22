#!/usr/bin/env python3

def return_evens(num_list):
    return_evens =[] #define the empty list of even numbers
    for number in num_list:
        if number %2 ==0: # checks if number is even
            return_evens.append(number) # if even stores it
    return return_evens # retums a list of even numbers

   


        




def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
    
    