class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, value):
        self.items += [value]
    
    def pop(self):
        if self.is_empty():
            return None
        top_value = self.items[len(self.items) - 1]
        self.items = self.items[:len(self.items) - 1]
        return top_value
    
    def top(self):
        if self.is_empty():
            return None
        return self.items[len(self.items) - 1]
    
def is_balanced(expression):
    stack = Stack()
    matching_pair = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.top() != matching_pair.get(char, None):
                return 'N'
            stack.pop()
    
    return 'S' if stack.is_empty() else 'N'

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        expression = data[i]
        results.append(is_balanced(expression))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
