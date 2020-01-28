"""
31a_if __name__ == '__main__'.py and 31b_if __name__ == '__main__'.py demonstrate why is the following statement used:
    if __name__ == '__main__':

What does the if __name__ == "__main__": do?
    - When Python runs a program, before it goes and executes the code in the program, it sets some special variables,
    and __name__ is one of those special variables.
    - And when Python runs a program 'directly' it sets the __name__ variable equal to '__main__'. Otherwise, it sets
    the __name__ variable to the name you import the module by.
    - That is, the global variable, __name__, in the module that is the entry point to your program, is '__main__'.
    Otherwise, it's the name you import the module by.
    - So, the code under the if block will only run if the module is the entry point to your program.
    - It allows the code in the module to be importable by other modules, without executing the code block beneath the
    if block on import.
    - In short, use if __name__ == "main" block to prevent (certain) code from being run when the module is imported.

Note: Whenever a module is imported, all the code in the imported module is executed, except the code that is in
uncalled functions/methods, and the code that is inside the if __name__ == "main" block.
"""

# The next line of code will always be executed when this module is imported
print('This will always run.')


def my_func():
    print("31a_if __name__ == '__main__' module's my_func() method executed.")


# The following code will not run when this module is imported
if __name__ == '__main__':
    my_func()
