class Heap:
    def __init__(self,values):
        self.values=values
        self.size=len(self.values)

    def show(self):
        
        return self.size,self.values
        
    def insert(self,x):
        self.values.append(x)
        self.size+=1
        self.sift_up(self.size-1)
        return self.size,self.values
    
    def extract_min(self):
        if  self.size==0:
            return None
        temp=self.values[0]
        self.values[0]=self.values[-1]
        self.values.pop()
        self.size-=1
        self.sift_down(0)
        return temp,self.values
        
    def sift_up(self,i):
        while i!=0 and self.values[i]<self.values[(i-1)//2]:
            self.values[i],self.values[(i-1)//2]=self.values[(i-1)//2],self.values[i]
            i = (i - 1) // 2
            
   
        
    def sift_down(self,i):
        while  2*i+1<self.size:
            j=i
            if self.values[2*i+1]<self.values[i]:
                j=2*i+1
            if 2*i+2<self.size and  self.values[2*i+2]< self.values[j]:
                j=2*i+2
            if i==j:
                break
            self.values[i],self.values[j]=self.values[j],self.values[i]
            i=j

if __name__ == "__main__":
              
    a=Heap([1,2,4,6,1,2,5,7,8])
'''
print(a.insert(1))
    print(a.insert(2))
    print(a.insert(4))

    print(a.insert(3))
    print(a.insert(1))
    print(a.insert(5))
    print(a.insert(3))
    print(a.extract_min())

    print(a.show())
'''
print(a.show())
