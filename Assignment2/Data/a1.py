import random
f=open('grade.csv','w')
f.write('num,oddeven\n')
for i in range(1000):
    x=random.randint(0,100)
    if x<50:
        f.write(str(x)+',4\n')
    elif x<65:
        f.write(str(x)+',3\n')
    elif x<80:
        f.write(str(x)+',2\n')
    else:
        f.write(str(x)+',1\n')
f.close()