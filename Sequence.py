n = int(input("Enter the length of the sequence: ")) # Do not change this line

t1 = 1
t2 = 2
t3 = 3
t4 = 0

print(1)
print(2)
print(3)

for i in range(n-3):
    t4 = t2 + t3 +t1
    print(t4)
    t1 = t2
    t2 = t3
    t3 = t4
    

    
    
    