def stack_push(var):
    stack.append(var)

def output_push_NGL(item):
    output_NGL.append(item)

def find_NGL(arr):
    # size = len(arr)
    for i in arr:
        if len(stack)==0:
            output_push_NGL(-1)
        elif len(stack) > 0 and stack[-1] > i:
            output_push_NGL(stack[-1])
        elif len(stack) > 0 and stack[-1] < i:
            while(len(stack) > 0 and stack[-1] < i):
                stack.pop()
            if len(stack)==0:
                output_push_NGL(-1)
            else:
                output_push_NGL(stack[-1])
        stack_push(i)

arr = [3,0,2,4,5,1,6]
stack = []
output_NGL = []
find_NGL(arr)
print("Nearest greatest left elements are:",output_NGL)