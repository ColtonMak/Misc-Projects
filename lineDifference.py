a = list(input("First line:"))
b = list(input("Second line:"))

if len(a) == len(b):
    for x in range(0, len(a)):
        if a[x] != b[x]:
            print ("At char " + str(x) + " " + a[x] + " doesn't match " + b[x])
else:
    print("Lines are at different lengths")