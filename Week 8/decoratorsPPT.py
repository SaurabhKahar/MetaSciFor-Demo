# Step 1: Define the decorator function
def my_decorator(func):
    
    # Step 2: Create a wrapper function
    def wrapper():
        print("Something before the function.")
        func()  # Call the original function
        print("Something after the function.")
        
    # Step 3: Return the wrapper function
    return wrapper

# Step 4: Apply the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Step 5: Call the decorated function
say_hello()
