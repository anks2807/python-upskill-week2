try:
    a, b= 10, 0
    result = a / b
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(f"Exception details: {e}")


try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Error: List index out of range.")
    print(f"Exception details: {e}")


def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Exception details: {e}")
    except TypeError as e:
        print(f"Exception details: {e}")
    finally:
        print("Execution completed.")


safe_divide(1, 0)
safe_divide(1,'a')
