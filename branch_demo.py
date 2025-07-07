print("hello_world")
import math
def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        middle1 = n // 2 - 1
        middle2 = n // 2
        return (data[middle1] + data[middle2]) / 2
    else:
        middle = n // 2
        return data[middle]