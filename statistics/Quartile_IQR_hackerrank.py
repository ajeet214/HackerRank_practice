
# Enter your code here. Read input from STDIN. Print output to STDOUT

number = int(input())

sequence = sorted(list(map(lambda x:int(x), input().split(' ')))) 

if len(sequence)%2 != 0:
    Q2 = sequence[len(sequence)//2]
    lower = sorted(sequence[:len(sequence)//2])
    upper = sorted(sequence[(len(sequence)//2)+1:])
    if len(lower)%2 ==0:
        Q1 = (lower[len(lower)//2]+lower[(len(lower)//2)-1])/2
        Q3 = (upper[len(upper)//2]+upper[(len(upper)//2)-1])/2
    else: 
        Q1 = lower[len(lower)//2]
        Q3 = upper[len(upper)//2]

else:
    Q2 = (sequence[len(sequence)//2]+sequence[(len(sequence)//2)-1])/2
    lower = sequence[:int(len(sequence)//2)]
    upper = sequence[int(len(sequence)//2):]
    if len(lower)%2 == 0:
        Q1 = (lower[len(lower)//2]+lower[(len(lower)//2)-1])/2
        Q3 = (upper[len(upper)//2]+upper[(len(upper)//2)-1])/2
    else:
        Q1 = lower[len(lower)//2]
        Q3 = upper[len(upper)//2]


print('{:g}'.format(Q1))
print('{:g}'.format(Q2))
print('{:g}'.format(Q3))
#IQR
print('{:g}'.format(Q3-Q1))



