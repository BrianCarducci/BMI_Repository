from pylab import *
import matplotlib.pyplot as plt
from math import sqrt

# Author: Brian Carducci
# Date: 10/10/16
# CSC325, RUBY

"""This program reads in a text file which is composed of numerical data. Rows represent individuals and columns
   represent variables. This program acquires the desired data from this text file (age, weight, height). It then
   calculates the BMIs of all of the individuals and plots the BMIs against the ages of the individuals. It then
   calculates the formula contained in the function named calc_formula, and plots this data against the weight of
   the individuals. The regression lines for both graphs are calculated and plotted as well."""




"""Computes formula"""


def calc_formula(chest_diameter, chest_depth, bitrochanteric_diameter, wrist_girth, ankle_girth, height):
    return -110 + 1.34 * chest_diameter + 1.54 * chest_depth + 1.20 * bitrochanteric_diameter + 1.11 * \
        wrist_girth + 1.15 * ankle_girth + 0.177 * height


"""reads in a text file and stores each line in a list of lists"""


def read_data_in_array(path):
    with open(path) as file:
        array = []
        array = [[float(digit) for digit in line.split()] for line in file]
        print "Raw Data: " + str(array)
    return array


"""retrieves the ages of each person and stores them into an array"""


def get_age_array(x):
    age_array = []
    for i in range(507):
            age = x[i][21]
            age_array.append(age)
    print "Ages: " + str(age_array)
    return age_array


"""retrieves the weight of each person and stores them into an array"""


def get_weight_array(x):
    weight_array = []
    for i in range(507):
            weight = x[i][22]
            weight_array.append(weight)
    print "Weights: " + str(weight_array) + "\n"
    return weight_array


"""Returns an array of all of the formula results"""


def get_formula_array(form_array):
    new_array = []
    for i in range(507):
            form_result = calc_formula(form_array[i][4], form_array[i][3], form_array[i][2], form_array[i][20], form_array[i][19], form_array[i][23])
            new_array.append(form_result)
    print "Formula Data: " + str(new_array)
    return new_array


"""Returns the sum of of the products of x,y pairs"""


def sum_of_prods(x, y):
    sum_of_prods = 0
    for i in range(len(x)):
        sum_of_prods += x[i] * y[i]
    return sum_of_prods


"""Returns the sum of every item squared in an array"""


def sum_squared_array(x):
    squared_array = [i**2 for i in x]
    return np.sum(squared_array)


""""Calculates the regression slope"""


def regression_slope(n, sum_prod_xy, sum_x, sum_y, sum_Xs):
    slope = (n * sum_prod_xy - (sum_x * sum_y)) / (n * sum_Xs - (sum_x) ** 2)
    return slope


"""Calculates the intercept"""


def intercept(sum_y, sum_x, slope, n):
    inter = (sum_y - (slope * sum_x)) / n
    return inter


"""Calculates the correlation coefficient"""


def correlation(n, sumXY, sum_x, sum_y, sum_x_squared, sum_y_squared,):
    corr = (n * sumXY - (sum_x * sum_y))/sqrt((n*sum_x_squared - sum_x**2) * (n*sum_y_squared - sum_y**2))
    return corr


"""Calculates the bmi of an individual"""


def bmi_calc(x, y):
    bmi = x / ((y ** 2)/100)
    return bmi


"""Returns array of BMIs"""


def get_bmi_array(x):
    new_array = []
    for i in range(507):
        bmi = bmi_calc(x[i][22], x[i][23])
        new_array.append(bmi)
    return new_array


"""Returns an array of Y-values given a slope and intercept of a line"""


def get_line(slope, intercept):
    y_array = [intercept]
    for i in range(1, 120):
        y = slope*i + intercept
        y_array.append(y)
    return y_array


"""Data is read into a list of lists. Each individual list within the parent list is a row from the data text file"""
"""Note: You may need to supply your own path, or just put the file in your project folder in your IDE"""
data_array = read_data_in_array("bmi_data.txt")

"""Stores needed pieces of the data into individual"""
formula_array = get_formula_array(data_array)
age_array = get_age_array(data_array)
weight_array = get_weight_array(data_array)
bmi_array = get_bmi_array(data_array)


"""Calculates the slope of the regression line, correlation coefficient, and the intercept of the Weight,Formula data"""
regression_slope_weight = regression_slope(len(weight_array), sum_of_prods(weight_array, formula_array,), np.sum(weight_array), np.sum(formula_array), sum_squared_array(weight_array))
print "Slope of the weight,formula regression line: " + str(regression_slope_weight)
corr_weight = correlation(len(weight_array), sum_of_prods(weight_array, formula_array), np.sum(weight_array), np.sum(formula_array), sum_squared_array(weight_array), sum_squared_array(formula_array))
print "Correlation coefficient of Weight/Formula data: " + str(corr_weight)
intercept_weight = intercept(np.sum(formula_array), np.sum(weight_array), regression_slope_weight, len(weight_array))
print "Intercept of Weight/Formula data: " + str(intercept_weight) + "\n"


"""Calculates the slope of the regression line, correlation coefficient, and the intercept of the Age,BMI data"""
regression_slope_bmi = regression_slope(len(bmi_array), sum_of_prods(age_array, bmi_array), np.sum(age_array), np.sum(bmi_array), sum_squared_array(age_array))
print "Slope of the Age,BMI regression line: " + str(regression_slope_bmi)
corr_bmi = correlation(len(bmi_array), sum_of_prods(age_array, bmi_array), np.sum(age_array), np.sum(bmi_array), sum_squared_array(age_array), sum_squared_array(bmi_array))
print "Correlation coefficient of Age,BMI data: " + str(corr_bmi)
intercept_bmi = intercept(np.sum(bmi_array), np.sum(age_array), regression_slope_bmi, len(bmi_array))
print "Intercept of Weight/Formula data: " + str(intercept_bmi) + "\n"


"""Code below plots graphs"""


"""Graph for weight,formula"""
plt.figure(1)
plt.plot(get_line(regression_slope_weight, intercept_weight), color="red")
plt.scatter(weight_array, formula_array)
plt.title("Weight VS. Formula results")
plt.xlabel("Weight")
plt.ylabel("Formula")

"""Graph for age,bmi"""
plt.figure(2)
plt.scatter(age_array, bmi_array)
plt.plot(get_line(regression_slope_bmi, intercept_bmi), color="red")
plt.title("Age VS. BMI")
plt.xlabel("Age")
plt.ylabel("BMI")

"""Displays both graphs"""
plt.show()
