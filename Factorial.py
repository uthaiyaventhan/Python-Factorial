n = int(input("Enter a positive integer: "))
              
product = 1
count = 1

while count <= n:
    product = count * product 
    count += 1
print("The factorial of", str(n), "is %d" % product)