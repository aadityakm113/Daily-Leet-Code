# https://leetcode.com/problems/design-circular-deque/
class ListNode:
    def __init__(self,val,nxt=None,prev=None):
        self.val,self.next,self.prev=val,nxt,prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.size=0
        self.capacity=k
        self.left=None
        self.right=None
        

    def insertFront(self, value: int) -> bool:
        if self.isFull(): #If deque is full
            return False
        if self.left is None: #if there is no node in the queue, create new node
            self.left=ListNode(value,None,None)
            self.right=self.left
        else:
            newLeft=ListNode(value,self.left,None)
            self.left.prev=newLeft
            self.left=newLeft
        self.size+=1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.left is None:
            self.left=ListNode(value,None,None)
            self.right=self.left
        else:
            self.right.next=ListNode(value,None,self.right)
            self.right=self.right.next
        self.size+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size==1:#only one node in the deque
            self.left=None
            self.right=None
        else:
            self.left=self.left.next
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size==1:
            self.left=None
            self.right=None
        else:
            self.right=self.right.prev
        self.size-=1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.left.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.right.val

    def isEmpty(self) -> bool:
        return (self.size==0)

    def isFull(self) -> bool:
        return (self.size==self.capacity)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()