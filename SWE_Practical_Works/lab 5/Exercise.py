class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


# 1. Function to evaluate postfix expressions using a stack
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():  # Operand
            stack.push(int(token))
        else:  # Operator
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)
    return stack.pop()


# 2. Queue implemented using two stacks
class QueueWithStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack.is_empty():
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()


# 3. Task Scheduler using a Queue
class TaskScheduler:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.enqueue(task)

    def run(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing task: {task}")


# 4. Convert infix expression to postfix using a stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    postfix = []
    tokens = expression.split()

    for token in tokens:
        if token.isalnum():  # Operand
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while not stack.is_empty() and precedence[stack.peek()] >= precedence[token]:
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)


# Testing the new functions

# Test Postfix Evaluation
print("Postfix Evaluation:")
print(evaluate_postfix("3 4 + 2 * 7 /"))  # Should print 2.0

# Test Queue with Two Stacks
print("\nQueue Using Two Stacks:")
queue_with_stacks = QueueWithStacks()
queue_with_stacks.enqueue(1)
queue_with_stacks.enqueue(2)
queue_with_stacks.enqueue(3)
print(queue_with_stacks.dequeue())  # Should print 1
print(queue_with_stacks.dequeue())  # Should print 2

# Test Task Scheduler
print("\nTask Scheduler:")
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.run()  # Should print each task in order

# Test Infix to Postfix Conversion
print("\nInfix to Postfix Conversion:")
print(infix_to_postfix("( 3 + 4 ) * 2 - 7"))  # Should print "3 4 + 2 * 7 -"
