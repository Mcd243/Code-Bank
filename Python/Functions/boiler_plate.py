
"""This is called a "boiler-plate".
 This code makes the main() function run automatically if the code itself is run. 

If you run a script itself, its name, the value of the variable \_\_name\_\_, is " \_\_main\_\_", 
so the if statement in the boiler-plate is True and the main() function is called. 

If the code is saved as a script, and then this is imported, 
\_\_name\_\_ is the name of the file, e.g. 'passwd_checker'. 
So \_\_name\_\_ is not "\_\_main\_\_" and therefore main() is not called. 

The main reason for having this boiler-plate is that it allows the same 
module to be used in two different ways - it can be executed directly as a script, 
or be imported and used in another module or interactively. 
By doing the "main" check, you can have that code only executes when you want 
to run the module as a program and not have it execute when someone just wants 
to import your module and call your functions themselves.

The term "boiler-plate" is used for any standardised text that is often re-used 
without any changes - it actually comes from the field of law, where contracts 
often consist of boiler-plate text that is re-used again and again. """

if __name__ == "__main__":
    main()