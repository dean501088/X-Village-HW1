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
        self.addt=[]
        for i in range(self.n):
            self.addt.append([0] * (self.m))
        for p in range(len(self.table)):
            for q in range(len(self.table[0])):
                self.addt[p][q]=self.table[p][q]+m.table[p][q]

        return self.new(self.addt)


    def sub(self, m):
        
        a=self.table
        self.subt=[]
        for i in range(self.n):
            self.subt.append([0] * (self.m))
        for p in range(len(a)):
            for q in range(len(a[0])):
                self.subt[p][q]=a[p][q]-m.table[p][q]

        return self.new(self.subt)

    def mul(self, m):
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
        
        for i in range(self.n):
            self.tran.append([0] * self.m)

        for s in range(self.n):
            for t in range(self.m):
                self.tran[s][t]=t2[t][s]

        return self.new(self.tran)  

    def new(self,res):
        newma = Matrix(self.n,self.m)
        for s in range(self.n):
            for t in range(self.m):
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
c = a.add(b)
d = a.mul(b)
e = a.sub(b)
c.display()
print('----------A-B-----------')
e.display()
print('----------A*B-----------')
d.display()
print('--The transpose of A*B--')
f=d.transpose()
f.display()

