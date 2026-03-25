from functools import wraps
import time

def memoization(time_live = None):
    def decor(func):
        cache = {}
        time_created = {}

        @wraps(func)
        def wrapper(*args):
            key = args
            now = time.time()

            if key in cache:
                if now - time_created[key] < time_live:
                    return cache[key]
                else:
                    del cache[key]
                    del time_created[key]
            
            result = func(*args)
            cache[key] = result
            time_created[key] = now

            return result
        return wrapper
    return decor

@memoization(3)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))