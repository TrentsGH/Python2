class vect:
    def __init__(self,v=[0,0,0]):
        self.v = v
        self.n = len(v)

    def __add__(self,v):
        temp = []
        if type(v) == int or type(v)==float:
            for i in range(self.n):
                temp.append(self[i]+v)
        else:
            for i in range(self.n):
                temp.append(self[i]+v[i])
        return vect(temp)
    
    def __radd__(self,v):
        temp = []
        if type(v) == int or type(v)==float:
            for i in range(self.n):
                temp.append(self[i]+v)
        else:
            for i in range(self.n):
                temp.append(self[i]+v[i])        
        return vect(temp)

    def __sub__(self,v):
        temp = []
        if type(v) == int or type(v)==float:
            for i in range(self.n):
                temp.append(self[i]-v)
        else:
            for i in range(self.n):
                temp.append(self[i]-v[i])
        return vect(temp)
    
    def __rsub__(self,v):
        temp = []
        if type(v) == int or type(v)==float:
            for i in range(self.n):
                temp.append(-self[i]+v)
        else:
            for i in range(self.n):
                temp.append(-self[i]+v[i])        
        return vect(temp)
    
    def __mul__(self,v):
        temp = []
        if type(v) == int or type(v)==float:
            for i in range(self.n):
                temp.append(self[i]*v)
        else:
            for i in range(self.n):
                temp.append(self[i]*v[i])        
        return vect(temp)

    def __rmul__(self,v):
        return self.__mul__(v)
    
    def __write__(self,x=None):
        return str(self.v)
    def __repr__(self):
        return self.__write__()
    def __getitem__(self,i):
        return self.v[i]
    def __call__(self,x):
        print(x)


