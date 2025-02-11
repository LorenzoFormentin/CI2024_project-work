# s328373 - Lorenzo Formentin

import numpy as np

# MSE: 7.12594e-32
def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

# MSE: 1.14294e+15
def f2(x: np.ndarray) -> np.ndarray:
    return  np.multiply(np.exp(np.negative(np.add(np.add(-5.3764146574248635, -4.692474291917981), -3.874839711447872))), np.add(np.multiply(np.sin(np.sin(np.sin(np.power(np.abs(x[0]), 0.9800281466887241)))), np.subtract(x[1], np.negative(x[2]))), x[0]))

# MSE: 4.952668771268292e-05
def f3(x: np.ndarray) -> np.ndarray:
    return np.subtract(np.subtract(np.multiply(2.0009349859153516, np.square(x[0])), np.divide(np.square(x[1]), np.reciprocal(x[1]))), np.divide(np.subtract(np.tan(1.1819816421246245), np.add(np.square(-1.1403504786040495), x[2])), np.reciprocal(-3.50044292533818)))

# MSE: 1.8806700432910917e-10
def f4(x: np.ndarray) -> np.ndarray:
    return np.add(np.add(np.add(np.add(np.cbrt(-1.709959363771984), 4.475216042264263), np.add(np.cos(x[1]), np.multiply(x[0], -0.05361298843153227))), np.log(np.abs(np.exp(np.cos(x[1]))))), np.add(np.add(np.add(np.add(np.cos(x[1]), np.cos(x[1])), np.cos(x[1])), np.multiply(x[0], -0.03729943517914346)), np.add(np.cos(x[1]), np.cos(x[1]))))

# MSE: 3.9469809772573434e-18
def f5(x: np.ndarray) -> np.ndarray:
    return np.divide(np.reciprocal(np.exp(np.square(4.5448881647015495))), np.tan(np.power(np.abs(np.cbrt(6.131535248870913)), np.divide(x[1], 2.783335244410499))))

# MSE: 1.268152358619465e-09
def f6(x: np.ndarray) -> np.ndarray:
    return np.add(x[1], np.multiply(0.694511799447451, np.add(x[1], np.negative(x[0]))))

# MSE: 35.29871832548343
def f7(x: np.ndarray) -> np.ndarray:
    return np.add(np.sqrt(np.abs(np.divide(np.subtract(np.divide(np.divide(np.multiply(np.log(np.abs(np.add(x[1], 1.7793682206964412))), np.multiply(np.add(x[0], x[0]), np.add(x[0], 1.0887296717744281))), np.add(x[1], np.negative(x[0]))), np.divide(np.cbrt(np.power(np.abs(np.add(x[0], x[1])), -4.676801676642564)), np.multiply(x[1], np.multiply(x[1], np.add(x[0], x[0]))))), np.divide(np.divide(np.multiply(np.log(np.abs(np.add(x[0], 1.4499540712525796))), np.multiply(np.add(x[1], x[1]), np.add(x[0], 1.0801601216336572))), np.add(x[1], np.negative(x[0]))), np.divide(np.cbrt(np.power(np.abs(np.add(x[0], x[1])), -4.676801676642564)), np.subtract(2.855935054418408, np.cos(np.add(x[0], x[1])))))), np.tan(-3.562675474663839)))), np.power(np.abs(np.negative(np.power(np.abs(-1.8033503570886023), np.cos(np.cos(np.square(x[1])))))), np.multiply(np.add(np.negative(np.power(np.abs(np.power(np.abs(2.3268716907637144), 3.2447479901915877)), np.cos(np.add(x[1], np.negative(x[0]))))), np.exp(np.divide(np.subtract(-3.1273704799300104, 0.37456462027018234), np.cbrt(-3.2904512978709057)))), -1.3265643340480757)))

# MSE: 19197.584545242124
def f8(x: np.ndarray) -> np.ndarray:
    return np.subtract(np.subtract(np.exp(np.add(x[5], np.absolute(-4.715694544662557))), np.add(np.absolute(np.power(np.abs(-5.632182938136989), 4.034970230441637)), np.add(np.multiply(x[3], -45.16886310612786), np.power(np.abs(x[4]), 4.888932543187845)))), np.subtract(np.exp(np.add(np.absolute(4.81713262209737), np.negative(x[5]))), np.square(np.add(np.subtract(4.999795905012371, -25.390378174225116), np.multiply(-5.507721530077821, x[5])))))
