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
    for x in a:
        c=c+x
    return (c)

def listdot (a,b):
    c=0
    for x in range(0,len(a)):
        c=c+a[x]*b[x]
    return c

def listmean (a):
    c=0
    for x in a:
        c=c+x
    c=c/len(a)
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

def listel(a,ind_list):
    c=[a[x] for x in ind_list]
    return c

def listindfind(a,cndn):
    c=[]
    for i in range(0,len(a)):
        if eval('a[i]'+str(cndn)):
            c.append(i)
    return c

def listelfind(a,cndn):
    c=[]
    for x in a:
        if eval('x'+str(cndn)):
            c.append(x)
    return c
        
def doc():
    print('''List of functions:
         listadd (a,b):          Returns list of Elementwise addition of lists "a" and "b"
         listsub (a,b):          Returns list of Elementwise difference of lists "a" and "b"
         listelemwisemult (a,b): Returns list of elementwise products of lists "a" and "b"
         listelemwisemdiv (a,b): Returns list of elementwise division of lists "a" and "b" as a[...]/b[...]
         listsum (a):            Returns the sum of numbers in the list "a"
         listdot (a,b):          Returns the scalar or dot product of elements in lists "a" and "b"
         listmean (a):           Returns the arithmetic mean of the elements in list "a" 
         listscal(a,b):          Returns a list of the product of scalar "a" with list "b" if "a" is scalar, or other way around.
         listel(a,ind_list):     Returns a list of elements in "a" referenced by index list "ind_list"
         listindfind(a,cndn):    Returns a list of indices in "a" satisfying condition "cndn" entered as string, e.g. cndn='>3'
         listelfind(a,cndn):     Returns a list of elements in "a" satisfying condition "cndn" entered as string, e.g. cndn='>3'
         ''')
