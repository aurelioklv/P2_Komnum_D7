from prettytable import PrettyTable
import math

#WOLFANS = Hasil integrasi fungsi untuk LOWBOUND dan UPBOUND dihitung menggunakan wolfram
WOLFANS = 0.835648848264721053337103459700110766786522127

# Define function to integrate
def f(x):
    return (1/(1+pow(x, 3)))

# Define trapezoidal method
def trapezoidal(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    
# Define romberg method
def romberg(lower, upper, iteration):
    lowerBound = lower
    upperBound = upper
    iteration = iteration
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
                h_res += f(j)
            else:
                h_res += 2*f(j)

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

    print("Table for Romberg's Integration method")
    print(table)

    result_row = table[0]
    result_row.border = False
    result_row.header = False

    result = result_row.get_string(fields = [header[iteration]]).strip()
    return result

# Main
lower_limit = int(input("Lower limit: "))
upper_limit = int(input("Upper limit: "))
iteration = int(input("Iteration: "))

result_trapezoid = trapezoidal(lower_limit, upper_limit, iteration)
result_romberg = romberg(lower_limit, upper_limit, iteration)

error_trapezoid = (WOLFANS - (float)(result_trapezoid)) / 100
error_trapezoid = "{:.12f}".format(error_trapezoid)
error_romberg = (WOLFANS - (float)(result_romberg)) / 100
error_romberg= "{:.12f}".format(error_romberg)

print("Actual result: " + str(WOLFANS))
print("Result using trapezoid method: " + str(result_trapezoid))
print("Result using romberg method: " + str(result_romberg))
print("Error using trapezoidal method: " + error_trapezoid + "%")
print("Error using romberg method: " + error_romberg + "%")
