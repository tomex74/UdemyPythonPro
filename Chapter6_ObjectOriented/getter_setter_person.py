class Person(object):
    def __init__(self):
        self._firstName = 'empty'
        self._lastName = 'empty'
        self._age = 0

    @property
    def firstName(self): 
        return self._firstName

    @firstName.setter
    def firstName(self, val): 
        self._firstName = val

    @firstName.deleter
    def firstName(self): 
        del self._firstName

    @property
    def lastName(self): 
        return self._lastName
    
    @lastName.setter
    def lastName(self, val): 
        self._lastName = val
    
    @lastName.deleter
    def lastName(self): 
        del self._lastName

    @property
    def age(self): 
        return self._age
    
    @age.setter
    def age(self, val): 
        self._age = val
    
    @age.deleter
    def age(self): 
        del self._age

if __name__ == '__main__':
    a = Person()
    print(a.firstName)
    a.firstName = 'Dave'
    print(a.firstName)
    a.firstName = 'Peter'
    print(a.firstName)
