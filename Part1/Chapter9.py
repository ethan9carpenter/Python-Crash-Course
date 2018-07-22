
class Dog(object):#object in parentheses when not extending class
    name=""
    
    def __init__(self, name, age):#constuctor, __ to differentiante from user-named methods
        super(Dog, self).__init__()#required for calling superclass in Python 2.7
        self.name=name
        self.age=age
    def getName(self):
        return self.name

dog=Dog(name="Boston", age=12)
print dog.getName()

#super class must be in same file and come before subclass

class PrimeCounter(object):
    def getPrimeCount(self, upperBound):
        primes=[]
        if upperBound>=2:
            primes.append(2)
        for i in range(2, upperBound):
            isPrime=True
            for prime in primes:
                if i%prime==0:
                    isPrime=False
                    break
            if isPrime:
                primes.append(i)                
        return len(primes)

counter=PrimeCounter()
print str(counter.getPrimeCount(10000))