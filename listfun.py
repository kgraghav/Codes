{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def listadd (a,b):\n",
    "    c=[x+y for x,y in zip(a,b)]\n",
    "    return (c)\n",
    "\n",
    "def listsub (a,b):\n",
    "    c=[x-y for x,y in zip(a,b)]\n",
    "    return (c)\n",
    "\n",
    "def listelemwisemult (a,b):\n",
    "    c=[x*y for x,y in zip(a,b)]\n",
    "    return (c)\n",
    "\n",
    "def listelemwisemdiv (a,b):\n",
    "    c=[x/y for x,y in zip(a,b)]\n",
    "    return (c)\n",
    "\n",
    "def listsum (a):\n",
    "    c=0\n",
    "    for x in range(0,len(a)):\n",
    "        c=c+a[x]\n",
    "    return (c)\n",
    "\n",
    "def listdot (a,b):\n",
    "    c=0\n",
    "    for x in range(0,len(a)):\n",
    "        c=c+a[x]*b[x]\n",
    "    return c\n",
    "\n",
    "def listscal(a,b):\n",
    "    if type(a)==list and (type(b)==int or type(b)==float):\n",
    "        c=[b*x for x in a]\n",
    "        return c\n",
    "    elif type(b)==list and (type(a)==int or type(a)==float):\n",
    "        c=[a*x for x in b]\n",
    "        return c\n",
    "    else:\n",
    "        print('One input must be list and another scalar')\n",
    "        \n",
    "def doc():\n",
    "    print('''List of functions:\n",
    "         listadd (a,b):          Returns list of Elementwise addition of lists \"a\" and \"b\"\n",
    "         listsub (a,b):          Returns list of Elementwise difference of lists \"a\" and \"b\"\n",
    "         listelemwisemult (a,b): Returns list of elementwise products of lists \"a\" and \"b\"\n",
    "         listelemwisemdiv (a,b): Returns list of elementwise division of lists \"a\" and \"b\" as a[...]/b[...]\n",
    "         listsum (a):            Returns the sum of numbers in the list \"a\"\n",
    "         listdot (a,b):          Returns the scalar or dot product of elements in lists \"a\" and \"b\"\n",
    "         listscal(a,b):          Returns a list of the product of scalar \"a\" with list \"b\" if \"a\" is scalar, or other way around. \n",
    "                                 Atleast one input must be scalar and other a list\n",
    "         ''')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
