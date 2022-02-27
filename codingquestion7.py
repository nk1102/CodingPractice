s = int(input())
e = int(input())
w = int(input())
count = s
d =int((5/9)*(count-32))
print(count,d)
if count<e:
    while count<e:
        count = count+w
        c =int((5.0/9)*(count-32))
        if count<e:
            print(count,c)


# perfect solution
# well done nikunj
