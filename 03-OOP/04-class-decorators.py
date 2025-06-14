import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " ms")
        return result
    
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for num in numbers:
        result.append(num * num * num)
    return result

array = range(1, 3)
out_square = calc_square(array)
out_cube = calc_cube(array)

print(out_square)
print(out_cube)
