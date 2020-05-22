# https://leetcode.com/problems/add-two-numbers/

# Linked Lists

class Node:
    def __init__(self, dataval=None):
        self.dataVal = dataval
        self.nextVal = None


class SinglyLinkedList:
    def __init__(self):
        self.headVal = None

    def traverse(self):
        nodeVal = self.headVal
        returnList = []
        returnList.append(nodeVal.dataVal)
        while nodeVal is not None:
            nodeVal = nodeVal.nextVal

        return returnList

    def reverseList(self):
        prev = None
        nodeVal = self.headVal
        while nodeVal is not None:
            next = nodeVal.nextVal
            nodeVal.NextVal = prev
            prev = nodeVal
            nodeVal = next

        self.headVal = prev

    def traverseAndAdd(self, reverse=False):
        if reverse:
            self.reverseList()

        val = 0
        nodeVal = self.headVal
        val = nodeVal.dataVal
        while nodeVal is not None:
            val += nodeVal.nextVal
            nodeVal = nodeVal.nextVal

        return val


def generateLinkedListAndAdd(*args):
    singlyLiskedLists = []
    for i in range(len(args)):
        singlyLiskedLists.append(SinglyLinkedList())

    for arg, index in enumerate(args):
        singlyLiskedLists[index].headVal = Node(arg[0])
        for i in range(1, len(arg)):
            singlyLiskedLists[index].headVal.nextVal = arg[i]

    sum = 0
    for list in singlyLiskedLists:
        sum += list.traverseAndAdd(reverse=True)

    return sum


def getSumOfDigits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number /= 10

    return sum
