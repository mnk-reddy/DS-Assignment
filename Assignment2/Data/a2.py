import random
f=open('BMI.csv','w')
f.write('Height,Weight\n')
for i in range(300):
    x=random.randint(120,200)
    y=random.randint(50,100)
    f.write(str(x)+','+str(y)+'\n')
f.close()