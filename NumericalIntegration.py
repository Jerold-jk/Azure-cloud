from flask import Flask
from flask import request
import math
app = Flask(__name__)
def BlackBoxFunction(x):
    f = math.sin(x)
    return f 
@app.route('/')
def numericalintegration():
    a = float(3.145)
    b = float(0)
    n = [10, 100, 1000, 10000, 100000, 1000000,10000000]
    length = len(n)
    for i in range(0,length):
        integral = 0.0
        dx = b-a/n[i]
        for j in range(1,n[i]):
            xip12 = dx*(j+0.5)
            di = BlackBoxFunction(xip12)*dx
            integral += di
        print(abs(integral))
    inte = str(integral)
    return  inte
if __name__=='main__':
    app.run()