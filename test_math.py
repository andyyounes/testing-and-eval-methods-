import pytest
import time
from operations import sum, mul, sub

def test_sum():
    assert sum(1,2)==3
    assert sum(-1, 1)==0
    assert sum(0,0)==0
def test_mul():
    assert mul(2,3)==6
    assert mul(-2,3)==-6
    assert mul(0,3)==0

def test_sub():
    assert sub(5, 3)==2
    assert sub(-5, 3)==-8
    assert sub(5,5)==0
def measure_time(func, a, b):
    start = time.time()
    result = func(a, b)
    elapsed = time.time() - start
    return result, elapsed
def time_sum():
    start = time.time()
    sum(1000, 2000)
    elapsed = time.time() - start
    print(f"Time taken for sum: {elapsed:.2f} seconds")

def time_mul():
    start = time.time()
    mul(1000, 2000)
    elapsed = time.time() - start
    print(f"Time taken for mul: {elapsed:.2f} seconds")

def time_sub():
    start = time.time()
    sub(1000, 2000)
    elapsed = time.time() - start
    print(f"Time taken for sub: {elapsed:.2f} seconds")
def pytest_time():
    
@pytest.mark.time
def test_execution_time():
    start_time = time.time()
    sum(1000, 2000)
    sum_time = time.time() - start_time

    mul(1000, 2000)
    mul_time = time.time() - start_time

    sub(1000, 2000)
    sub_time = time.time() - start_time
    print(f"Execution Time for sum: {sum_time} seconds")
    print(f"Execution Time for mul: {mul_time} seconds")
    print(f"Execution Time for sub: {sub_time} seconds")

    assert sum_time < 1
    assert mul_time < 1
    assert sub_time < 1

def main():
    i = int(input("Enter a number a= "))
    j = int(input("Enter a number b= "))
    s, time_sum = measure_time(sum, i, j)
    m, time_mul = measure_time(mul, i, j)
    subr, time_sub = measure_time(sub, i, j)

    print(f'sum of {i}+{j} = {s}, took {time_sum:.2f} seconds')
    print(f'Mul of {i}*{j} = {m}, took {time_mul:.2f} seconds')
    print(f'sub of {i}-{j} = {subr}, took {time_sub:.2f} seconds')
    print(f'pytest: {test_execution_time()}')

if __name__ == '__main__':
    main()