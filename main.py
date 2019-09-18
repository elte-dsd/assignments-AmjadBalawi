#method to test the code(simulate the example given in the lecture)
from hw import CountMinSketch
counts = CountMinSketch(5,3) 

stream=['A','B','C','A','A','C']
for i in stream:
    counts.add(i)

query=set(stream) # find the unique elements in the list
    
for j in query:
    print ("the frequency of ",j," is ",counts.min_freq(j))