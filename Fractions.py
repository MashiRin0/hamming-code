#Samengewerking tussen Robert de Haas en Jan Huls
import math

class Fraction:
    def sm_fr(self):
        p=self.a
        q=self.b
        while p%q!=0:
            p0=p
            q0=q
            p=q0
            q=p0%q0
        return Fraction(self.a/q,self.b/q)
    def __init__(self, teller, noemer):
        self.a = teller
        self.b = noemer
        if self.b==0:
            raise ValueError("noemer is gelijk aan 0")
    def __str__(self):
        self=Fraction.sm_fr(self)
        if self.b==1:
            return str(int(self.a))
        else:
            return str(int(self.a)) + '/' + str(int(self.b))
    def __add__(self,other):
        if type(self)!=type(other):
            other=Fraction(other,1)
        add = Fraction(self.a*other.b+self.b*other.a,self.b*other.b)
        return add
    def __radd__(self,other):    
        return self+other
    def __sub__(self,other):
        if type(self)!=type(other):
            other=Fraction(other,1)
        sub = Fraction(self.a*other.b-self.b*other.a,self.b*other.b)
        return sub
    def __rsub__(self,other):
        return (-self)+other
    def __mul__(self, other):
        if type(self)!=type(other):
            other=Fraction(other,1)
        mul = Fraction(self.a*other.a,self.b*other.b)
        return mul
    def __rmul__(self,other):
        return self*other
    def __truediv__(self, other):
        if type(self)!=type(other):
            other=Fraction(other,1)
        div = Fraction(self.a*other.b,self.b*other.a)
        return div
    def __rtruediv__(self, other):
        if type(self)!=type(other):
            other=Fraction(other,1)
        rdiv = Fraction(self.b*other.a,self.a*other.b)
        return rdiv
    def __gt__(self, other):
        if float(self)>float(other):
            return True
        else: return False
    def __ge__(self, other):
        if float(self)>=float(other):
            return True
        else: return False
    def __lt__(self, other):
        if float(self)<float(other):
            return True
        else: return False
    def __le__(self, other):
        if float(self)<=float(other):
            return True
        else: return False
    def __eq__(self, other):
        if float(self)==float(other):
            return True
        else: return False
    def __ne__(self, other):
        if float(self)==float(other):
            return False
        else: return True
    def __neg__(self):
        neg=Fraction(-self.a,self.b)
        return neg
    def __pos__(self):
        return self
    def __abs__(self):
        abs_self = Fraction(abs(self.a),abs(self.b))
        return abs_self
    def __float__(self):
        return self.a/self.b
    def __int__(self):
        return self.a//self.b