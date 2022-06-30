#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quotientProblem(x,y):
    goo = x+y
    return goo
def quotientProblems(x,y):
    ga = x-y
    return ga
def quotientProblemss(x,y):
    ge = x/y
    return ge
def test_return():
   str1 = 'nice'
   return str1


print(test_return())

def ola(name):
    return 'Hello ' + name + ". How are you doing today?"

print(ola('Stephen'))
print(ola('Ralu'))
def main():
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    
    print (quotientProblem(x,y))
    print (quotientProblems(x,y))
    print (quotientProblemss(x,y))
    
if __name__ == '__main__':
    main()


# In[ ]:




