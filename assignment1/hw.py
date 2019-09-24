import numpy as np
import mmh3

class CountMinSketch(object):
   
    def __init__(self, width, length):
    
        self.width = width # the number of columns (possible values for the hash function)
        self.length = length # the number of rows (number of hash functions)
        self.table = np.zeros([length, width])  # Create empty table (initialize with zeros)
        self.seed = np.random.randint(self.width, size = self.length) #Random seed

    def add(self, key): 
        #method to add the key to the table (in this case a string will be added)
     
        for i in range(0, self.length):
            index = mmh3.hash (key, self.seed[i]) % self.width
            self.table[i, index] = self.table[i, index] + 1

    def min_freq(self, key):
       #to find the frequency of a given element
        min_freq = self.width
        for i in range(0, self.length): #loop over the rows to find the corresponding count
            index = mmh3.hash( key, self.seed[i] ) % self.width
            if self.table[i, index] < min_freq:
                min_freq = self.table[i, index] 
        return min_freq
