def operation(a,b,c):
    c = c.rstrip()
    #print(a,b,c+'u', 'gggggggggggg', str(int(a)+int(b)), dir(c))
    if c == '+': return str(int(a)+int(b))
    elif c == '-':
        result = int(a)-int(b)
        if result<0: return str(int(a)-int(b))
        else: return str(int(a)-int(b))
    elif c== '*': return str(int(a)*int(b))
    else: return str(int(a)/int(b))
def arithmetic_arranger(problems, bool=False):
    arr=[]
    maxLen = 0
    if len(problems) > 5 :
        return 'Error: Too many problems.'
    for problem in problems:
        a = problem.split()
        b = problem.find(a[1])
        c=''
        item1 = problem[:b]
        try:
            num1 = int(a[0])
            num2 = int(a[2])
        except:
            return 'Error: Numbers must only contain digits.'
        if a[1] == '*' or a[1] =='/':
            return "Error: Operator must be '+' or '-'."
        if len(str(num1)) > 4 or len(str(num2)) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(a[2]) > len(a[0]):
            maxLen = len(a[2])
            #print('ppppppppp', maxLen)
            for i in range(maxLen- len(a[0])):
                a[0]= ' '+a[0]
        elif (len(a[2])) < len(a[0]):
            maxLen = len(a[0])
            minLen =len(a[2])
            for i in range(maxLen - minLen):
                #print(i)
                a[1]= a[1]+' '
        #print(b, problem, len(item1))
        elif len(a[2]) == len(a[0]):
            maxLen = len(a[2])
            #a[0]=' '+a[0]
        for i in range(maxLen):
            c = c + '-'
        if len(arr)==0:
            arr.append('  '+a[0])
            arr.append(a[1]+' '+a[2])
            arr.append('--'+c)
            if bool is True:
                s = operation(a[0], a[2], a[1])
                #print(maxLen,len(s), 'nnnnnn', len(c))
                for i in range(len(c)-len(s)+2):
                    s = ' '+s
                arr.append(s)
        else:
            a[0] = '  '+a[0]
            c = '--'+c
            arr[0] = arr[0] + '    '+a[0]
            arr[1] = arr[1] + '    '+a[1]+' '+a[2]
            arr[2] = arr[2] + '    '+c
            if bool is True:
                s = operation(a[0], a[2], a[1])
                for i in range(len(c)-len(s)):
                    s = ' '+s
                arr[3] = arr[3] + '    '+s
        #arr[0] = arr[0] + '   '+a[0]
    count = 0
    string=''
    while count < len(arr):
        if(count == len(arr)-1):
            break
        arr[count] = arr[count] + '\n'
        string = string + arr[count]
        count = count + 1
    string = string + arr[len(arr)-1]
    #print(arr, 'uuuu')
    #print(len(string))
    return string