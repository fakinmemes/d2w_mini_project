from org.transcrypt.stubs.browser import *
import random


def gen_random_int(number, seed):
    result = None
    mylist = []
    random.seed(seed)
    for x in range(number - 1):
        mylist.append(x)
    random.shuffle(mylist)
    result = mylist
    return result


def listtostring(s):
    string = ""
    count = 0
    for number in s:
        string += str(number)
        count += 1
        if count < (len(s)):
            string += ","
        else:
            string += "."
    return string


def generate():
    number = 10
    seed = 200
    array = gen_random_int(number, seed)
    array_str = listtostring(array)

    # This line is to placed the string into the HTML
    # under div section with the id called "generate"s
    document.getElementById("generate").innerHTML = array_str

def stringtolist(s):
    string = s
    new_array = string.split(",")
    for i in range(len(new_array)):
        new_array[i] = int(new_array[i])
    return new_array

def bubble_sort(list):
    array = list
    #create a variable for the length of the array
    n = len(array)
    #for loop to run for the outer index
    for outer_index in range(1, n-1):
        #for loop to run for the inner index
        for inner_index in range(1, n):
            #create hold variables to do the swap
            first_number = array[inner_index - 1]
            second_number = array[inner_index]
            #if loop to do the swap
            if first_number > second_number:
                array[inner_index] = first_number
                array[inner_index - 1] = second_number
    return array

def sortnumber1():

    array = stringtolist(document.getElementById("generate").innerHTML)
    new_array = bubble_sort(array)
    array_str = listtostring(new_array)
    document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
    value = document.getElementsByName("numbers")[0].value

    # Throw alert and stop if nothing in the text input
    if value == "":
        window.alert("Your textbox is empty")
        return
    array = stringtolist(value)
    new_array = bubble_sort(array)
    array_str = listtostring(new_array)
    document.getElementById("sorted").innerHTML = array_str
