# Add One to the Number
# You are given a linked list representing a number such that each individual node acts as a digit of the number. The list
# HEAD->1->2->3->NULL
# corresponds to the number 123. Your task is to add 1 to this number.

# Input Format
#
# The first line contains an integer T, number of test cases. Then follows
# T test cases. Each test case consists of two lines.The first line contains an integer N
# representing length of the linked list The second line contains
# N space separated integers representing nodes of a linked list.
#
# Output Format
#
# The output contains T lines, each line containing the modified number as a linked list.
# Note - You only need to implement addOneToList() function, and return the head of the linked list.
#
# Example
# Input
# 2
# 3
# 1 2 3
# 4
# 9 9 9 9
#
# Output
# 1 2 4
# 1 0 0 0 0

"""
Complete the addOneToList() function below
For your reference
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head=None
		self.tail = None


 	def insertAtEnd(self,data): # returns head of the linked list
 	def printSinglyLinkedList(self):

"""
# Function Arguments: head (refers to the head of the linked list)
def addWithCarry(head):
	if head is None:
		return 1
	res = head.data + addWithCarry(head.next)
	head.data =  res%10
	return res//10


def addOneToList(head):
	carry = addWithCarry(head)
	if(carry>0):
		newNode = Node(carry)
		newNode.next = head
		return newNode
	return head

