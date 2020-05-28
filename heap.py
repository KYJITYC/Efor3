class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def show(self):
        return self.size, self.values

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)
        print(self.values)
        return self.values

    def extract_min(self):
        if self.size == 0:
            return None
        temp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        print(temp,self.values)
        return temp

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j


def heapify(arr):
    heap = Heap()
    for i in arr:
        heap.insert(i)
    return heap


def heapify_fast(arr):
    heap = Heap()
    heap.values=arr[:]
    heap.size=len(arr)
    for i in reversed(range(n//2)):
        heap.sift_down(i)
    return heap

def sort(heap):
    arr = []
    while heap.size:
        arr.append(heap.extract_min())
    return arr



if __name__ == "__main__":
    a = [1, 3, 6, 1, 2, 5]
    h = heapify(a)
    print(sort(h))



