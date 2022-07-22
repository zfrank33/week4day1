def decorator(func):
    def inner():
        print("before the funciotn is callled")
        func()
        print("after the function is called")
    return inner

@decorator
@decorator
def my_function():
    print("This is inside the function")


    # Function to be decorated should give me the first name of a person
# Its decorator should return the name as a string with is awesome attached if the name starts with a [k ,s ,a d]
# if not not it should says that the name smells like teen spirit
# There needs to be also some driver code

names=['Jody S', 'Jacoby Y', 'Alex C', 'Dylan K', 'Kevin B', 'Andre L', 'Dmitry U', 'Francisco G', 'Sarah S', 'Gio M', 'Shayne H']