# BASIC SYNTAX

'''
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only,
the indentation in Python is very important.
Python uses indentation to indicate a block of code.
'''
#Example 01:
'''
    x = 11
    if x < 10:
        print("the number")
        print("is bigger then 10")
    print("here we are out the code block")
'''

'''
Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object.
An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more
letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers.
Python is a case sensitive programming language. Thus, Manpower and manpower are two 
different identifiers in Python.

Here are naming conventions for Python identifiers −
    * Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
    * Starting an identifier with a single leading underscore indicates that the identifier is private.
    * Starting an identifier with two leading underscores indicates a strongly private identifier.
    * If the identifier also ends with two trailing underscores, the identifier is a language-defined 
    special name.
'''

'''
Reserved Words

The following list shows the Python keywords. These are reserved words and you cannot use them as
constant or variable or any other identifier names. All the Python keywords contain lowercase letters only.

        and	        exec	        not
        assert	    finally         or
        break	    for	            pass
        class	    from	        print
        continue	global	        raise
        def	        if	            return
        del	        import	        try
        elif	    in	            while
        else	    is	            with
        except	    lambda          yield
'''

'''
Multi-Line Statements
Statements in Python typically end with a new line. Python does, however, allow the use of the line 
continuation character (\) to denote that the line should continue.

#Example 03:
    total = item_one + \
            item_two + \
            item_three
'''