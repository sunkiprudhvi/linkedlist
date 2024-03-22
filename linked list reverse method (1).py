#remove linkedlist elements
#input: head=[1,2,6,3,4,5,6]
#val=6
#output:[1,2,3,4,5]
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            val=int(input("enter data :"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new_node
            i=i+1
    def show(self,head):
        t=head
        print("list of nodes: ")
        s=0
        while t:
            print(t.val,end=" ")
            s=s+t.val
            t=t.next
        print("\nTotal",s)
    def removeElement(self,head,val):
        temp=Node(0) #dumy node
        temp.next=head
        prev, curr=temp,head
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return temp.next    
        
obj=linkedlist()
n=int(input("value of n: "))
obj.createLL(n)
obj.show(obj.head)
val=int(input("Enter the value to delete: "))
obj.head=obj.removeElement(obj.head,val)
print("\n After deletion")
obj.show(obj.head)
