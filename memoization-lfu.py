from functools import wraps

def memoization(cache_size = None):
    def decor(func):
        cache = {}
        cache_used = {}

        @wraps(func)
        def wrapper(*args):
            key = args
            if key in cache:
                cache_used[key] += 1
                return cache[key]
            
            result = func(*args)
            
            if len(cache) >= cache_size:
                least_used = min(cache_used, key = cache_used.get)
                del cache[least_used]
                del cache_used[least_used]

            cache[key] = result
            cache_used[key] = 1

            return result
        return wrapper
    return decor

@memoization(75)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))