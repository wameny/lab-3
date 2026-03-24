from functools import wraps

def memoization(cache_size = None):
    def decor(func):
        cache = {}

        @wraps(func)
        def wrapper(*args):
            key = args
            if key in cache:
                return cache[key]
            
            result = func(*args)
            if cache_size is not None and len(cache) <= cache_size:
                cache[key] = result

            return result
        return wrapper
    return decor

@memoization(70)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))