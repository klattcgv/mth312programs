import numpy as np
import sympy as sy
import string
import random

#Code from Class

alpha,beta=-19,8
x,y=sy.var('x y',real=True)
x_1,x_2,x_3,y_1,y_2,y_3=sy.var('x_1 x_2 x_3 y_1 y_2 y_3')
ec = sy.Eq(y**2,x**3+alpha*x+beta)

def EX(xv,modulus:int=None):
    if modulus==None:
        return xv**3+alpha*xv+beta
    else:
        return (xv**3+alpha*xv+beta)%modulus
def EY(yv,modulus:int=None):
    if modulus==None:
        return yv**2
    else:
        return (yv**2)%modulus

p=127

ecm=sy.Eq(ec.lhs%p,ec.rhs%p)

def add(pt0,pt1):
    if pt0 == (sy.oo,sy.oo):
        return pt1
    elif pt1 == (sy.oo,sy.oo):
        return pt0
    else:
        x1,x2,y1,y2=pt0[0],pt1[0],pt0[1],pt1[1]
        if x1 == x2:
            if y1 == y2:
                if y1 == 0:
                    return (sy.oo,sy.oo)
                else:
                    mm = ((3*x1*x1+alpha)*sy.invert(2*y1,p))%p
            else:
                return (sy.oo,sy.oo)
        else:
            mm = ((y1-y2)*sy.invert(x1-x2,p))%p
        x3 = (mm*mm-x1-x2)%p
        y3 = (p-(mm*(x3 - x1) + y1))%p
        return (x3,y3)

def opp(pt):
    if pt==(sy.oo,sy.oo):
        return pt
    else:
        return pt[0], p - pt[1]

def subtract(pt0,pt1):
    return add(pt0,opp(pt1))

def ecmul(pt,exp: int):
    if exp == 0:
        return (sy.oo,sy.oo)
    elif exp < 0:
        sign = -1
        exp = -1*exp
    else:
        sign = 1
    r = (sy.oo,sy.oo)
    e = exp
    ppt = pt
    while e>0:
        if e%2 == 1:
            r = add(r,ppt)
        ppt = add(ppt,ppt)
        e = e//2
    if sign == -1:
        r = opp(r)
    return r

def isQuadRes(x:int,modulus:int=p):
    '''
    Checks whether a given number is a quadratic residue modulo p. That is, if it is the square of some number,
    modulo p, and thus if it has a square root modulo p.
    '''
    return (pow(x,(modulus-1)//2,modulus)==1) or (x%p==0)

def mSqrt(z:int,modulus:int=p):
    '''
    Uses properties of the integers modulo a prime p to find a square root modulo p if it exists.
    '''
    if isQuadRes(z,modulus):
        return pow(z,(modulus+1)//4,modulus)
    else:
        return None

mpts=[]

for xx in range(p):
    XX=EX(xx,p)
    if isQuadRes(XX):
        yy=mSqrt(XX)
        if yy==0:
            mpts+=[(xx,yy)]
        else:
            mpts+=[(xx,yy),(xx,p-yy)]
#mpts=[[(xx,mSqrt(EX(xx,p))),(xx,(p-mSqrt(EX(xx,p))%p))] for xx in range(p) if isQuadRes(EX(xx,p))]
#mpts=set(sy.flatten(mpts,1))
mpts = list(mpts)+[(sy.oo,sy.oo)]
len(mpts)

pfacts=set(sy.primefactors(len(mpts)))

checks = [(len(mpts))//j for j in pfacts]
print(checks)
g=mpts[0]
print(g)
all(ecmul(g,k)!=(sy.oo,sy.oo) for k in checks)

prods=[]
r = g
while not r in prods:
    prods += [r]
    r = add(r,g)

#Start of ECEC--------------------------------------------------------------------------

def string2num(instring: str, alphabet: str=string.printable):
  mynum=0
  for j in instring:
    mynum=len(alphabet)*mynum+alphabet.index(j)
  return mynum

def encode(message: str, modulus: int=p,alphabet: str=string.printable):
    n=string2num(message,alphabet)

    nlist=[]
    while n>0:
        nlist+=[n%modulus]
        n=n//modulus
    return nlist

def num2string(number: int, alphabet: str = string.printable):
    base = len(alphabet)
    plaintext = ''
    while number > 0:
        number, index = divmod(number, base)
        plaintext = alphabet[index] + plaintext
    return plaintext

def decode(nlist, modulus: int=p, alphabet: str=string.printable):
    decoded_message = ""
    n = 0

    for num in reversed(nlist):
        n = n * modulus + num

    decoded_message = num2string(n)

    return decoded_message

def find_point(msg: str):
    base_x = encode(msg)
    print(base_x)
    encrypted_message = []
    k = 50

    for num in base_x:
        x = 0
        for i in range(p):
            x += (num*k + i) % p
            rhs = (x ** 3 + alpha * x + beta) % p
            y = mSqrt(rhs, p)
            if y is not None:
                new_point = [x,y,k]
                encrypted_message += new_point
            else:
                k = random.randint(30,50)
                i = 0
                #raise ValueError("Couldn't find a valid point on the curve.")
    return encrypted_message

def decrypt_message(nlist):
    deciphered_list = [(nlist[i]//nlist[i+2]) for i in range(0,len(nlist),3)]
    print(deciphered_list)
    decoded_message = decode(deciphered_list)
    return decoded_message


msg = "This is a test."
points = find_point(msg)
print(msg, " Maps onto the points: ", points)
decrypted = decrypt_message(points)
print("Decrypted message: ",decrypted)