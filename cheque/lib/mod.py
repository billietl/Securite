def invMOD(number,module):
    x=0; y=1;
    u=1; v=0;
    a=number; b=module;
    while (0 != a):
        q = int(b/a);
        r = b%a;
        m = x - u*q;
        n = y - v*q;
        b=a; a=r; x=u; y=v; u=m; v=n;
    return b == 1 and ((x+module)%module) or None 

