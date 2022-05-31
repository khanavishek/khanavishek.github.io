# Our users love our Random number class!
# However, they get frustrated when the same number comes up too frequently.
# Please design a class that generates random integers with a specified range,
# but never repeats the same number until all other numbers have been seen.
 
# Phase 1
# Your class must support the following operations:
#  - Construct a random number generator with a given minimum and maximum
#  - Generate a new random number without any unnecessary repetition
 
 
# Always Test
#  - Write unit tests for your code! Code the test cases rather than reading from stdin.


import random

class Random: 

    def __init__(self,start, end):
        self.HashMap = {}
        self.HashMapItems= []
        self.start = start
        self.end = end
        self.createHashMap()
        
    def createHashMap(self):
        #start and end are both integers, and assuming end > start
        
        for i in range(self.start, self.end + 1):
            #for each number in the range: 
            
            #add it to the hashMap 
            # while( random.randint(self.start,self.end+2) not in self.HashMap.keys()):
            
            self.HashMap[random.random()] = i
            # key = random.random() #returns a float between 0 and 1
        self.HashMapItems = sorted(self.HashMap.items())
        
        # print("hash_map.items()", self.HashMapItems)
    
    def randomNum(self):
        if (len(self.HashMapItems) > 0):
            num = self.HashMapItems.pop()[1]
            return num
        else: #you have seen all the numbers
            self.createHashMap()
            return self.randomNum()
        


#Driver code to test method

test_method = Random(1,5)
for i in range(10):
    print(test_method.randomNum())

        
        
        
    
    
