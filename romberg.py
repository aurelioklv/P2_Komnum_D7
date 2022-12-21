from prettytable import PrettyTable
import math

def func(x):
    return (1/(1+pow(x, 3)))

lowerBound = int(input("Lower Bound: "))
upperBound = int(input("Upper Bound: "))
iteration = int(input("Iteration: "))

header = []

for i in range(iteration+1):
    h = "O(h^{})".format(2*(i))
    header.append(h)

table = PrettyTable()
column = []
h = upperBound - lowerBound

for i in range(0, iteration+1):
    h = h/2
    h_res = 0

    j = lowerBound
    while(j <= upperBound):
        j += h
        if(j == lowerBound or j == upperBound):
            h_res += func(j)
        else:
            h_res += 2*func(j)

    h_res *= h/2
    column.append(h_res)

table.add_column(header[0], column)

for i in range(1, iteration+1):
    column = []
    j = 0

    while j <= iteration - i:
        low = table[j]
        high = table[j+1]

        low.border = False
        low.header = False
        high.border = False
        high.header = False

        low_res = (float)(low.get_string(fields=[header[i-1]]).strip())
        high_res = (float)(high.get_string(fields=[header[i-1]]).strip())

        diff = (pow(4,i)*high_res - low_res)/(pow(4, i)-1)
        column.append(diff)
        j += 1
    
    for k in range(i):
        column.append("-")
        
    table.add_column(header[i], column)

print(table)

result_row = table[0]
result_row.border = False
result_row.header = False

result = result_row.get_string(fields = [header[iteration]]).strip()
print("Result: {}".format(result))
