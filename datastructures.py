# Q1
n=list(map(int, input("enter elements of array seperated by space: ").strip().split()))
print('array is ',n)
target=int(input('enter sum target: '))
for i in n:
  for j in n:
    if i+j== target and i>j:
      print (i,j)

# Q2
n=list(map(int, input("enter elements of array seperated by space: ").strip().split()))
print('array:', n)
for i in range(len(n)):
    a=i
    b=len(n)-1-i
    if a==b or a>b:
      break
    c=n[a]
    n[a]=n[b]
    n[b]=c

print('Reversed array: ', n)

#Q3
a=input('string 1: ')
b=input('string 2: ')
if a[::-1]==b:
  print('strings are reverse of each other')
else:
  print('strings are not reverse of each other.')

#q4
a=input('string: ')
for i in a:
  if a.count(i)>1:
    continue
  else:
    print(i)
    break

#Q5
def hanoi(n, start, aux, dest):
    if n == 0:
        return
        
    hanoi(n-1, start, dest, aux)

    if start:
        dest.append(start.pop())
        print(Pole_1, Pole_2, Pole_3)

    hanoi(n-1, aux, start, dest)

n = int(input("NO of disks: "))
Pole_1 = list(range(n,0,-1))
Pole_2, Pole_3 = [], []
print(Pole_1, Pole_2, Pole_3)
hanoi(n, Pole_1, Pole_2, Pole_3)

# Q6
class Stack:
  def _init_(self):
    self.stack=[]
  def push(self,element):
    self.stack.append(element)
  def pop(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack.pop()
  def peek(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack[-1]
posttopre=Stack()
operators='+-*/^'
def posttopreconv(exp):
  for i in exp:
    result=''
    if i not in operators:
      posttopre.push(i)
    else:
      a=posttopre.pop()
      b=posttopre.pop()
      result += i+b+a
      posttopre.push(result)

  return result
a=input('Enter the postfix expression: ')
posttopreconv(a)

#Q7
class Stack:
  def _init_(self):
    self.stack=[]
  def push(self,element):
    self.stack.append(element)
  def pop(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack.pop()
  def peek(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack[-1]
pretoin=Stack()
operators='+-*/^'
def pretoinconv(exp):
  exp1=exp[::-1]
  for i in exp1:
    result=''
    if i not in operators:
      pretoin.push(i)
    else:
      a=pretoin.pop()
      b=pretoin.pop()
      result += a+i+b
      pretoin.push(result)

  return result
a=input('Enter the prefix expression: ')
pretoinconv(a)

#Q8
a=input()
b=('[','{','(')
stack=[]
for i in a:
  if i in b:
    stack.append(i) 
  if i not in b:
    if i=='}' and stack[-1]=='{':
      stack.pop()
    elif i==']' and stack[-1]=='[':
      stack.pop()
    elif i==')' and stack[-1]=='(':
      stack.pop()
    else:
      break
if len(stack)==0:
  print('the brackets are closed')
else:
  print('the brackets are not closed')

# Q9
class Stack:
  def _init_(self):
    self.stack=[]
  def push(self,element):
    self.stack.append(element)
  def pop(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack.pop()
  def peek(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack[-1]
def reverse(stack):
  print('stack before;', stack.stack)
  rev=stack.stack[::-1]
  return 'reversed stack:',rev

  # OR
def reverse2(stack):
  print('stack before;', stack.stack)
  x=Stack()
  while len(stack.stack)!=0:
    x.push(stack.pop())
  return 'reversed stack:',x.stack


s=Stack()
s.push(10)
s.push(20)
s.push(30)

reverse2(s)

#Q10
class Stack:
  def _init_(self):
    self.stack=[]
  def push(self,element):
    self.stack.append(element)
  def pop(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack.pop()
  def peek(self):
    if len(self.stack)==0:
      print('stack is empty')
      return
    return self.stack[-1]


def minimum(stack):
  a=min(stack.stack)
  return a
  
  #or
def minimum2(stack):
  x=stack
  y=[]
  while len(x.stack)!=0:
    y.append(x.pop())
  return min(y)

s=Stack()
s.push(10)
s.push(20)
s.push(30)
