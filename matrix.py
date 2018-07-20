from random import randint

class Matrix:

    def __init__(self, nrows, ncols):
        
        self.n = nrows #橫列
        self.m = ncols #直行
        self.table = []
        for i in range(self.n):
            self.table.append([0] * (self.m))

        for j in range(self.n):
            for k in range(self.m):
                self.table[j][k] = randint(0,9)

    def add(self, m):
        if len(self.table) != len(m.table):
            return None
        elif len(self.table[0]) != len(m.table[0]):
            return None
        else:
            self.addt=[]
            for i in range(self.n):
                self.addt.append([0] * (self.m))
            for p in range(len(self.table)):
                for q in range(len(self.table[0])):
                    self.addt[p][q]=self.table[p][q]+m.table[p][q]

            return self.new(self.addt)


    def sub(self, m):
        if len(self.table) != len(m.table):
            return None
        elif len(self.table[0]) != len(m.table[0]):
            return None
        else:        
            a=self.table
            self.subt=[]
            for i in range(self.n):
                self.subt.append([0] * (self.m))
            for p in range(len(a)):
                for q in range(len(a[0])):
                    self.subt[p][q]=a[p][q]-m.table[p][q]

            return self.new(self.subt)

    def mul(self, m):
        
        if len(self.table[0]) != len(m.table):
            return None
        
        else:
            self.result = []
            for i in range(self.n):
                self.result.append([0] * m.m)

            for i in range(len(self.table)):

                for j in range(len(m.table[0])):

                    for k in range(len(m.table)):
                        self.result[i][j] += self.table[i][k] * m.table[k][j]

            return self.new(self.result)

    def transpose(self):
        self.tran=[]
        a=self.table
        t2=a[:]
        
        for i in range(self.m):
            self.tran.append([0] * self.n)

        for s in range(self.m):
            for t in range(self.n):
                self.tran[s][t]=t2[t][s]

        return self.new(self.tran)  

    def new(self,res):
        newma = Matrix(len(res),len(res[0]))
        for s in range(len(res)):
            for t in range(len(res[0])):
                newma.table[s][t]=res[s][t]
        return newma
        
        
    def display(self):
        for i in self.table:
            for j in i:
                print(j, end="\t")
            print()

            
a = Matrix(int(input("Enter the rows of A matrix:")),int(input("Enter the columns of A matrix:")))
a.display()
b = Matrix(int(input("Enter the rows of B matrix:")),int(input("Enter the columns of B matrix:")))
b.display()

print('----------A+B-----------')
try:
    c = a.add(b)
    c.display()
except:
    print("Matrices are not addable")
    
print('----------A-B-----------')
try:
    e = a.sub(b)
    e.display()
except:
    print("Matrices are not minusable")
    
print('----------A*B-----------')

try:
    d = a.mul(b)
    d.display()
except:
    print("Matrices are not multable")
print('--The transpose of A*B--')

try:
    f=d.transpose()
    f.display()
except:
    print("A*B Matrix doesn't exit")

