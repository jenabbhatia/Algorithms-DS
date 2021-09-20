
def stack_push(var):
    stack.append(var)

def output_push_NGR(item):
    output_NGR.append(item)

def find_NGR(arr):
    # size = len(arr)
    for i in reversed(arr):
        if len(stack)==0:
            output_push_NGR(-1)
        elif len(stack) > 0 and stack[-1] > i:
            output_push_NGR(stack[-1])
        elif len(stack) > 0 and stack[-1] < i:
            while(len(stack) > 0 and stack[-1] < i):
                stack.pop()
            if len(stack)==0:
                output_push_NGR(-1)
            else:
                output_push_NGR(stack[-1])
        stack_push(i)


#creating input array
arr=[3,0,2,4,5,1,6]
stack = []
output_NGR = []

find_NGR(arr)
output_NGR.reverse()
print("Nearest greatest right elements are:",output_NGR)

