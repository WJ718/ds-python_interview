"""
원형 큐 디자인하기

.enQueue(x) : x삽입
.Rear() : return rear
.isFull() : boolean
.deQueue(): front pop
.Front() : return front
"""

class CircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k 
        self.maxlen = k # 최대 노드 갯수
        self.p1 = 0 # front
        self.p2 = 0 # rear
    
    # push
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen # move rear
        else:
            return False

    # pop    
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        
    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self):
        return -1 if self.q[self.p2] is None else self.q[self.p2]
    
    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

    

