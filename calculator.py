#calculator
+a=float(input(quot;enter a number\n&quot;))
b=float(input(quot;enter a number\n&quot;))
c=int(input(&quot;enter a number:add-1,sub-2,division-3,multiply-4\n&quot;))
print(&quot;the solution is&quot;)
if c==1:
print(a+b)
if c==2:
print(a-b)
if c==3:
if b==0:
print(&quot; infinity i.e. divisor is zero&quot;)
else:
print(a/b)
if c==4:
print(a*b)
s
