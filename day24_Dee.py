import statistics

values = [1, 2, 3, 4, 5]
print(statistics.mean(values))
print(statistics.median(values))
print(statistics.stdev(values))
print(statistics.variance(values))

pip install numpy

import numpy as np

print('numpy:', np.__version__)

python_list = [1, 2, 3, 4, 5]
array = np.array(python_list)
float_array = np.array(python_list, dtype=float)
boolean_array = np.array([0, 1, -1, 0], dtype=bool)
matrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(type(array))
print(array)
print(matrix.shape)
print(matrix.size)
print(matrix.dtype)

print(array.tolist())
print(np.array((1, 2, 3)))

numbers = np.array([1, 2, 3, 4, 5])
print(numbers + 10)
print(numbers - 10)
print(numbers * 10)
print(numbers / 10)
print(numbers % 3)
print(numbers // 2)
print(numbers ** 2)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(data[0])
print(data[:, 0])
print(data[0:2, 0:2])
print(data[::-1, ::-1])

reshaped = data.reshape(1, 9)
flattened = data.flatten()
print(reshaped)
print(flattened)

print(np.zeros((3, 3), dtype=int))
print(np.ones((3, 3), dtype=int))
print(np.arange(0, 20, 2))
print(np.linspace(1, 5, num=5))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a, b)))
print(np.vstack((a, b)))

random_float = np.random.random()
random_integers = np.random.randint(0, 10, size=(3, 3))
normal_values = np.random.normal(79, 15, 80)

values = np.random.normal(5, 0.5, 1000)
print('min:', np.min(values))
print('max:', np.max(values))
print('mean:', np.mean(values))
print('median:', np.median(values))
print('standard deviation:', np.std(values))
print('variance:', np.var(values))
print('percentile:', np.percentile(values, 50))

matrix = np.array([[1, 2, 3], [4, 55, 44], [7, 8, 9]])
print(np.amin(matrix, axis=0))
print(np.amax(matrix, axis=1))

f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(np.dot(f, g))

h = np.array([[1, 2], [3, 4]])
i = np.array([[5, 6], [7, 8]])
print(np.matmul(h, i))
print(np.linalg.det(i))