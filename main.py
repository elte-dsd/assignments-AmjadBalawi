#method to test the code(simulate the example given in the lecture)
from hw import CountMinSketch
counts = CountMinSketch(5,3) 

counts.add('A')
counts.add('B')
counts.add('C')
counts.add('A')
counts.add('A')
counts.add('C')
a= counts.min_freq('A')
b= counts.min_freq('B')
c= counts.min_freq('C')

print ("the frequency of A in the given stream =",a ,"and for B=",b," and for C =",c)
    
