def listadd (a,b):
    c=[x+y for x,y in zip(a,b)]
    return (c)

def listsub (a,b):
    c=[x-y for x,y in zip(a,b)]
    return (c)

def listelemwisemult (a,b):
    c=[x*y for x,y in zip(a,b)]
    return (c)

def listelemwisemdiv (a,b):
    c=[x/y for x,y in zip(a,b)]
    return (c)

def listsum (a):
    c=0
    for x in range(0,len(a)):
        c=c+a[x]
    return (c)

def listdot (a,b):
    c=0
    for x in range(0,len(a)):
        c=c+a[x]*b[x]
    return c

def listscal(a,b):
    if type(a)==list and (type(b)==int or type(b)==float):
        c=[b*x for x in a]
        return c
    elif type(b)==list and (type(a)==int or type(a)==float):
        c=[a*x for x in b]
        return c
    else:
        print('One input must be list and another scalar')
        
def doc():
    print('''List of functions:
         listadd (a,b):          Returns list of Elementwise addition of lists "a" and "b"
         listsub (a,b):          Returns list of Elementwise difference of lists "a" and "b"
         listelemwisemult (a,b): Returns list of elementwise products of lists "a" and "b"
         listelemwisemdiv (a,b): Returns list of elementwise division of lists "a" and "b" as a[...]/b[...]
         listsum (a):            Returns the sum of numbers in the list "a"
         listdot (a,b):          Returns the scalar or dot product of elements in lists "a" and "b"
         listscal(a,b):          Returns a list of the product of scalar "a" with list "b" if "a" is scalar, or other way around. 
                                 Atleast one input must be scalar and other a list
         ''')
