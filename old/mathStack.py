

class Stack:
    def __init__(self):
        self.numList = []
        self.len = 0

    def populateList(self, userString):
        for char in userString:
            if char != ' ':
                self.numList.append(char)
                self.len += 1

    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

    def pop(self):

        tempVal = self.numList.pop()
        self.len -= 1
        return tempVal

    def peek(self):

        tempVal = self.numList[-1]
        return tempVal





def doMath(stack):
        tempVal = 0
        total = 0
        operator = ''

        while stack.isEmpty() != True:
            #print(stack.peek())
            print (total)
            if stack.peek().isdigit():
                tempVal = int(stack.pop())

            elif (stack.peek() == ' '):
                stack.pop()

            else:
                if stack.peek() == '+':
                    stack.pop()
                    #print ("temp:",tempVal)
                    total += (tempVal + int(stack.pop()))
                
                elif stack.peek() == '-':
                    stack.pop()
                    #print("here")
                    val = (int(stack.peek()) - tempVal)
                    print ("val:", val)
                    total += (int(stack.pop()) - tempVal)

                elif stack.peek() == '*':
                    stack.pop()
                    total += (tempVal * int(stack.pop()))
                
                elif stack.peek() == '/':
                    stack.pop()
                    total += (int(stack.pop() /tempVal))
                
                tempVal = 0

        print (total)
        return total



s1 = Stack()
s1.populateList("5 - 4 - 3")

val = s1.peek()
#print (val)

doMath(s1)


