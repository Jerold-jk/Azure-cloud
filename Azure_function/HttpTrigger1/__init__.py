import logging
import math
from flask import Flask
from flask import request
import azure.functions as func
def BlackBoxFunction(x):
    f = math.sin(x)
    return f
def main(req: func.HttpRequest) -> func.HttpResponse:
    start = req.params.get('start')
    end = req.params.get('end')
    strr =" "
    strrr = " "
    a = float(end)
    b = float(start)
    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    l = len(N)
    for i in range(0, l):
        integral = 0.0
        dx = a-b/N[i]
        for j in range(1, N[i]):
            xp12 = dx*(j+0.5)
            di = BlackBoxFunction(xp12)*dx
            integral += di
        strr += str(integral)+","
        strrr = strr
    return func.HttpResponse(strrr)