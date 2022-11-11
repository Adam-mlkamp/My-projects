from cmath import sqrt

data = []
data.append([22,66,9, -0.14319894940006364 ])
data.append([9,1,4, -0.05])

def compute_data(a, b, c):
    return (-b + sqrt(b**2 - 4*a*c))/(2*a)

for test in data:
    print(compute_data(test[0], test[1], test[2])==test[3])

print(compute_data(22, 66, 9))
print(f'{compute_data(9, 1 ,4):.6f}')



