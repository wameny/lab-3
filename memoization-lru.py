from functools import wraps

def memoization(cache_size = None):
    def decor(func):
        cache = {}
        cache_order = []

        @wraps(func)
        def wrapper(*args):
            key = args
            if key in cache:
                cache_order.remove(key)
                cache_order.append(key)
                return cache[key]
            
            result = func(*args)
            
            if len(cache) >= cache_size:
                old = cache_order.pop(0)
                del cache[old]

            cache[key] = result
            cache_order.append(key)

            return result
        return wrapper
    return decor

@memoization(70)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))