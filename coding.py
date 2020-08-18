class Node:
	def __init__(self,val):
		self.next = None
		self.data = val




class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self,val):
		if self.head == None:
			self.head = Node(val)
		else:
			p = self.head
			while p.next!=None:
				p = p.next
			p.next = Node(val)
	def display(self):
		p = self.head
		while p!=None:
			print(p.data,end=  "->")
			p = p.next
		print("\b\b  ")
def solve(L1,L2):
	L3 = LinkedList()
	l1 = L1.head
	l2 = L2.head
	l3 = L3.head
	carry = 0
	while l1 and l2:
		digit = l1.data  + l2.data +carry
		if digit>9:
			digit = digit%10
			carry = digit //10
		else:
			carry = 0
		L3.insert(digit)
		l1 = l1.next
		l2 = l2.next
	
	while l1:
		digit = l1.data + carry
		if digit>9:
			digit = digit%10
			carry = digit //10
		else:
			carry = 0
		L3.insert(digit)

		l1 = l1.next
	
	while l2:
		digit = l2.data + carry
		if digit>9:
			digit = digit%10
			carry = digit //10
		else:
			carry = 0
		L3.insert(digit)

		l2 = l2.next

	L3.display()



#Driver program
n1 = "243"
n2 = "564"
L1 = LinkedList()
L2 = LinkedList()
for x in n1:
	L1.insert(int(x))
for x in n2:
	L2.insert(int(x))

solve(L1,L2)