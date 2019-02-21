from math import sqrt

a = (2321.4, -4747.62, 750.5)
b = (2321.4, -4747.62, 737.3)
c = (2321.4, -4747.62, 732.9)

distance1 = (sqrt(sum( (a-b)**2 for a, b in zip(a, b))))
distance2 = (sqrt(sum( (b-c)**2 for b, c in zip(b, c))))

print(distance1)
print(distance2)
    
