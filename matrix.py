class matrix:
    def __init__(self,rowcount,colcount, initnum = 0, randomize = False,randommin = 0,randommax = 1,debugMode = False):
        self.rowcount = rowcount
        self.colcount = colcount
        self.data = []
        self.initData(initnum)
        self.debugMode = debugMode
        if randomize and initnum == 0:
            self.randomize(randommin,randommax)
    def initData(self,num):
        temp = []
        for i in range(self.rowcount):
            temp = []
            for j in range(self.colcount):
                temp.append(num)
            self.data.append(temp)
    def randomize(self, minval,maxval):
        for i in range(self.rowcount):
            for j in range(self.colcount):
                self.data[i][j] = random(minval,maxval)
    def printmatrix(self):
        for i in range(self.rowcount):
            print(self.data[i])        
    def scalar_add(self,other):
        if  !other is int:
            print("error: can't add elementwise without one single number" )
            print("matrix:")
            self.printmatrix()
            print("")
            print("scalar:")
            print(other)
            print("")
            exit()
        else:
            if self.debugMode:
                print("debug message: matrix and scalar before addition:")
                print("")
                print("matrix 1 before addition:")
                self.printmatrix()
                print("")
                print("scalar:")
                print(other)
                print("")
                print("")
            for i in range(self.rowcount):
                for j in range(self.colcount):
                    self.data[i][j] = self.data[i][j]+other
            if self.debugMode:
                print("debug message: matrix 1:")
                print("")
                print("matrix 1:")
                self.printmatrix()
                print("")
    def scalar_multi(self,other):

        if  !other is int:
            print("error: can't multiply elementwise without one single number" )
            print("matrix:")
            self.printmatrix()
            print("")
            print("scalar:")
            print(other)
            print("")
            exit()
        else:
            if self.debugMode:
                print("debug message: matrix and scalar before multipication:")
                print("")
                print("matrix 1 before multipication:")
                self.printmatrix()
                print("")
                print("scalar:")
                print(other)
                print("")
                print("")
            for i in range(self.rowcount):
                for j in range(self.colcount):
                    self.data[i][j] = self.data[i][j]* other
            if self.debugMode:
                print("debug message: matrix 1:")
                print("")
                print("matrix 1:")
                self.printmatrix()
                print("")    
    def elem_multi(self,other):
            if self.rowcount != other.rowcount or self.colcount != other.colcount:
                print("error: can't multiply inequal matricies")
                print("matrix 1:")
                self.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                exit()
            else:
                if self.debugMode or other.debugMode:
                    print("debug message: matrecies before elementwise multiplication:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
                    print("matrix 2:")
                    other.printmatrix()
                    print("")
                    print("")
                for i in range(self.rowcount):
                    for j in range(self.colcount):
                        self.data[i][j] = self.data[i][j] * other.data[i][j]
                if self.debugMode or other.debugMode:
                    print("debug message: matrix 1 after elementwise multiplication:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
    def elem_add(self,other):
            if self.rowcount != other.rowcount or self.colcount != other.colcount:
                print("error: can't add inequal matricies")
                print("matrix 1:")
                self.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                exit()
            else:
                if self.debugMode or other.debugMode:
                    print("debug message: matrecies before elementwise addition:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
                    print("matrix 2:")
                    other.printmatrix()
                    print("")
                    print("")
                for i in range(self.rowcount):
                    for j in range(self.colcount):
                        self.data[i][j] = self.data[i][j] * other.data[i][j]
                if self.debugMode or other.debugMode:
                    print("debug message: matrix 1 after elementwise addition:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
    def elem_subtract(self,other):
            if self.rowcount != other.rowcount or self.colcount != other.colcount:
                print("error: can't add inequal matricies")
                print("matrix 1:")
                self.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                exit()
            else:
                if self.debugMode or other.debugMode:
                    print("debug message: matrecies before elementwise addition:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
                    print("matrix 2:")
                    other.printmatrix()
                    print("")
                    print("")
                for i in range(self.rowcount):
                    for j in range(self.colcount):
                        self.data[i][j] = self.data[i][j] * other.data[i][j]
                if self.debugMode or other.debugMode:
                    print("debug message: matrix 1 after elementwise addition:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
    def matrix_multi(a,other):
            if a.colcount != other.rowcount:
                print("error: can't matrix multiply matricies of wich cols of matrix 1 don't match up with rows of matrix 2:")
                print("matrix 1:")
                a.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                exit()
            else:
                out = matrix(a.rowcount,other.colcount)
                if a.debugMode or other.debugMode:
                    print("debug message: matrecies before matrix multiplication:")
                    print("")
                    print("matrix 1:")
                    a.printmatrix()
                    print("")
                    print("matrix 2:")
                    other.printmatrix()
                    print("")
                    print("")
                for i in range(a.rowcount):
                    for j in range(other.colcount):
                        out.data[i][j] = 0
                        for k in range(other.rowcount):
                            out.data[i][j] += a.data[i][k] * other.data[k][j]
                if a.debugMode or other.debugMode:
                    print("debug message: output matix after matrix multiplication:")
                    print("")
                    print("matrix out:")
                    out.printmatrix()
                    print("")
                return out        
    def transpose(self):
        if self.debugMode:
                    print("debug message: marix before being transposed:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
        temp = matrix(self.colcount,self.rowcount)
        
        for i in range(self.rowcount):
            for j in range(self.colcount):
                temp.data[j][i] = self.data[i][j]
        self.data = temp.data
        self.rowcount = temp.rowcount
        self.colcount = temp.colcount
        if self.debugMode:
            print("debug message: marix after being transposed:")
            print("")
            print("matrix 1:")
            self.printmatrix()
            print("")
    def aplyFunc(self,func):   
        if self.debugMode:
            print("debug message: marix before function being aplied:")
            print("")
            print("matrix 1:")
            self.printmatrix()
            print("")  
        for i in range(self.rowcount):
            for j in range(self.colcount):
                self.data[i][j] = func(self.data[i][j])
        if self.debugMode:
            print("debug message: marix after function being aplied:")
            print("")
            print("matrix 1:")
            self.printmatrix()
            print("")
    def copymatrix(self):
        m = Matrix(self.rowcount, self.colcount)
        for i in range(self.rowcount):
            for j in range(self.colcount):
                m.data[i][j] = self.data[i][j]
            return m;
    def toArray(m):
        out = []
        for i in range(m.rowcount):
            out.append(m.data[i][0])
        return out     
def fromArray(m):
    out = matrix(len(m),1)
    for i in range(out.rowcount):
        out.data[i][0] = m[i]
    return out
