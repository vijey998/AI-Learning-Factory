"""A tiny scalar reverse-mode autodiff engine for Chapter 8."""
from math import isclose
class Value:
    def __init__(self,data,parents=(),op=''):
        self.data=float(data);self.grad=0.0;self.parents=tuple(parents);self.op=op;self._backward=lambda:None
    def __add__(self,other):
        other=other if isinstance(other,Value) else Value(other);out=Value(self.data+other.data,(self,other),'+')
        def backward():self.grad+=out.grad;other.grad+=out.grad
        out._backward=backward;return out
    __radd__=__add__
    def __mul__(self,other):
        other=other if isinstance(other,Value) else Value(other);out=Value(self.data*other.data,(self,other),'*')
        def backward():self.grad+=other.data*out.grad;other.grad+=self.data*out.grad
        out._backward=backward;return out
    __rmul__=__mul__
    def __pow__(self,power):
        if not isinstance(power,(int,float)):raise TypeError('scalar power required')
        out=Value(self.data**power,(self,),f'**{power}')
        def backward():self.grad+=power*(self.data**(power-1))*out.grad
        out._backward=backward;return out
    def backward(self):
        topo=[];seen=set()
        def visit(v):
            if id(v) in seen:return
            seen.add(id(v))
            for p in v.parents:visit(p)
            topo.append(v)
        visit(self);self.grad=1.0
        for v in reversed(topo):v._backward()
def expression(a,b,c):return (a*b+c)**2
def finite_difference(values,index,h=1e-6):
    x=list(values);x[index]+=h;hi=expression(*map(Value,x)).data
    x=list(values);x[index]-=h;lo=expression(*map(Value,x)).data
    return (hi-lo)/(2*h)
if __name__=='__main__':
    nodes=[Value(2),Value(-3),Value(10)];loss=expression(*nodes);loss.backward()
    expected=[-24,16,8]
    for i,(v,e) in enumerate(zip(nodes,expected)):
        numeric=finite_difference([2,-3,10],i)
        assert isclose(v.grad,e,rel_tol=1e-12) and isclose(v.grad,numeric,rel_tol=1e-7,abs_tol=1e-7)
    print({'loss':loss.data,'gradients':[v.grad for v in nodes],'finite_differences':[finite_difference([2,-3,10],i) for i in range(3)]})
