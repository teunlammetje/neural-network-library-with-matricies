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
        #TODO: find a way for checking scalar is int

#        if  other + 1:
#            print("error: can't add elementwise without one single number" )
#            print("matrix:")
#            self.printmatrix()
#            print("")
#            print("scalar:")
#            print(other)
#            print("")
#            exit()
#        else:
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
        #TODO: find a way for checking scalar is int

#        if  other + 1:
#            print("error: can't add elementwise without one single number" )
#            print("matrix:")
#            self.printmatrix()
#            print("")
#            print("scalar:")
#            print(other)
#            print("")
#            exit()
#        else:
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
    def matrix_multi(self,other):
            if self.rowcount != other.colcount:
                print("error: can't matrix multiply matricies of wich rows of matrix 1 don't match up with cols of matrix 2:")
                print("matrix 1:")
                self.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                exit()
            else:
                out = matrix(self.rowcount,other.colcount)
                if self.debugMode or other.debugMode:
                    print("debug message: matrecies before matrix multiplication:")
                    print("")
                    print("matrix 1:")
                    self.printmatrix()
                    print("")
                    print("matrix 2:")
                    other.printmatrix()
                    print("")
                    print("")
                for i in range(self.rowcount):
                    for j in range(other.colcount):
                        out.data[i][j] = 0
                        for k in range(other.rowcount):
                            out.data[i][j] += self.data[i][k] * other.data[k][j]
                if self.debugMode or other.debugMode:
                    print("debug message: output matix after matrix multiplication:")
                    print("")
                    print("matrix out:")
                    out.printmatrix()
                    print("")
                return out
                    
                        
