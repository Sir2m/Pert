The code uses mainly numpy and pandas in python for handling needed calculation in PERT/CPM problems

Data points are given as inputs
a matrix of the input data is printed in a familiar shape for revising the data

a DataFrame contains the calculated Estimate Time and Variance for every activity is printed to be used

after making CPM the critical path can be determined, at this point it's given to the program the needed data of the critical path activites for further calculations
variance, and so the standard deviation, are calculated then using Scipy statistics and exactly standard norml distribion the program calculates the probability of occurence of the project after giving the final estimated time of the whole project
