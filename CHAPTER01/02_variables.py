'''
Assigning Values to Variables

Python variables do not need explicit declaration to reserve memory space. 
The declaration happens automatically when you assign a value to a variable. T
he equal sign (=) is used to assign values to variables.
'''
#Example 01:
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = 'John'       # A string

print('------------ Example 01 --------------')
print (counter)
print (miles)
print (name)
print('--------------------------------------')



'''
Standard Data Types

The data stored in memory can be of many types. For example, a person's age is stored as a numeric value
and his or her address is stored as alphanumeric characters. Python has various standard data types that
are used to define the operations possible on them and the storage method for each of them.

Python has five standard data types −

    * Numbers
    * String
    * List
    * Tuple
    * Dictionary
'''
'''
Python Numbers

Number data types store numeric values. Number objects are created when you assign a value to them.
For example −
'''
#Example 02:
print ('------------ Example 02 --------------')
var1 = 1
var2 = 10
print(var1)
print(var2)
del var1
print(var2)
# print(var1) # throw an error
print ('--------------------------------------')

'''
Python Strings

Strings in Python are identified as a contiguous set of characters represented in the quotation marks.
Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the
slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working
their way from -1 at the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.
For example −
'''
#Example 03:
print ('------------ Example 03 --------------')
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
print ('--------------------------------------')

'''
Python Lists

Lists are the most versatile of Python's compound data types. A list contains items separated by commas
 and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference
  between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at
 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation
  operator, and the asterisk (*) is the repetition operator. For example −
'''
#Exmple 04:
print ('------------ Example 04 --------------')
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
print ('--------------------------------------')

'''
Python Tuples

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values
 separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements
 and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can
  be thought of as read-only lists. For example −
'''
# Example 05:
print ('------------ Example 05 --------------')
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples
print ('--------------------------------------')

'''
Python Dictionary
Python's dictionaries are kind of hash table type. They work like associative arrays or
hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any
Python type, but are usually numbers or strings. Values, on the other hand, can be any
arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed
using square braces ([]). For example −
'''
#Example 06:
print ('------------ Example 06 --------------')
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print ('--------------------------------------')