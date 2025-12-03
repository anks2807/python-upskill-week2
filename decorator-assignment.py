import functools
from datetime import datetime

#calculate and print the time taken by a function to execute
def audit_time(func):
    def wrapper():
        start_time = datetime.now()
        print(f"start time: {start_time}")
        result = func()
        end_time = datetime.now()
        print(f"end time: {end_time}")
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in: {duration.total_seconds()} seconds")
        return result
    return wrapper

@audit_time
def make_list():
    list = [];
    for i in range(1, 1001):
        list.append(i)
    return list

print(make_list())


# retry decorator to retry a function a specified number of times
def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                func(*args, **kwargs)
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Alice")


# validate_positive decorator to ensure input is positive
def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Input must be a positive number.")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(10))


# cache decorator to cache results of a function
def cache(func):
    cached_results = {}
    def wrapper(x):
        if x not in cached_results:
            cached_results[x] = func(x)
        return cached_results[x]
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))


# require_permission decorator to check user permissions
def require_permission(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if 'admin' in user.get('permissions', []):
            return func(*args, **kwargs)
        else:
            print("Permission denied.")
    return wrapper


@require_permission
def delete_user(actor, target):
    print(f"User {target['name']} deleted by {actor['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}
delete_user(user1, user3)