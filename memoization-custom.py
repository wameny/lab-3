from functools import wraps
import time

def memoization(cache_size = None, time_live = None, type='LRU'):
    def decor(func):
        cache = {}
        cache_order = []
        cache_used = {}
        time_created = {}

        @wraps(func)
        def wrapper(*args):
            key = args
            now = time.time()

            if key in cache:
                if type == 'Time':
                    if time_live is None or now - time_created[key] < time_live:
                        return cache[key]
                    else:
                        del cache[key]
                        del time_created[key]
                elif type == 'LRU':
                    cache_order.remove(key)
                    cache_order.append(key)
                    return cache[key]
                elif type == 'LFU':
                    cache_used[key] += 1
                    return cache[key]
            
            result = func(*args)
            if cache_size is not None and len(cache) >= cache_size:
                if type == 'LRU':
                    old = cache_order.pop(0)
                    del cache[old]
                if type == 'LFU':
                    least_used = min(cache_used, key = cache_used.get)
                    del cache[least_used]
                    del cache_used[least_used]

            cache[key] = result        
            cache_order.append(key)
            cache_used[key] = 1
            time_created[key] = now
            return result

        return wrapper
    return decor

@memoization(cache_size = 75, time_live = 1, type = 'Time')
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))