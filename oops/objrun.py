from run import run
r1=run()

r2=run()

if r1.get() > r2.get():
   r1.show()
else:
   r2.show()