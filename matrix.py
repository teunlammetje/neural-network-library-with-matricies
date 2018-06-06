class matrix:
    def __init__(self,rowcount,colcount,randomize = False,randommin = 0,randommax = 0,debugMode = False):
        self.rowcount = rowcount
        self.colcount = colcount
        self.data = []
        self.initData()
        self.initrandom = randomize
        self.debugMode = debugMode
        if self.initrandom:
            self.randomize(randommin,randommax)
    def initData(self):
        temp = []
        for i in range(self.rowcount):
            temp = []
            for j in range(self.colcount):
                temp.append(0)
            self.data.append(temp)
    def randomize(self, minval,maxval):
        for i in range(self.rowcount):
            for j in range(self.colcount):
                self.data[i][j] = random(minval,maxval)
    def printmatrix(self):
        for i in range(self.rowcount):
            print(self.data[i])
        
    def scalar_add(self,other):
        if !other + 1 :
            print("error: can't add elementwise without one single number" )
            print("matrix:")
            self.printmatrix()
            print("")
            print("scalar:")
            print(other)
            print("")
            exit()
        else:
            if self.debugMode or other.debugMode:
                print("debug message: matrecies before addition:")
                print("")
                print("matrix 1 before addition:")
                self.printmatrix()
                print("")
                print("matrix 2:")
                other.printmatrix()
                print("")
                print("")
            for i in range(self.rowcount):
                for j in range(self.colcount):
                    self.data[i][j] = self.data[i][j]+ other.data[i][j]
            if self.debugMode or other.debugMode:
                print("debug message: matrix 1:")
                print("")
                print("matrix 1:")
                self.printmatrix()
                print("")
    def elem_multiply(self,other):
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
