import logging
import math
from flask import Flask
from flask import request
import azure.functions as func
def BlackBoxFunction(x):
    f = math.sin(x)
    return f
def main(req: func.HttpRequest) -> func.HttpResponse:
    #logging.info('Python HTTP trigger function processed a request.')
    start = float(0.0)
    end = float(0.0)
    start = req.params.get('start')
    end = req.params.get('end')
    name = req.params.get('name')
    LENGTH = 0
    WIDTH = 3.14
    print(start)
    print(end)
    print({name})
    strr =" "
    strrr = " "
    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    l = len(N)
    for i in range(0, l):
        integral = 0.0
        dx = WIDTH-LENGTH/N[i]
        for j in range(1, N[i]):
            xp = dx*(j+0.5)
            di = BlackBoxFunction(xp)*dx
            integral += di
        strr += str(integral)+","
        strrr = strr
    return func.HttpResponse(strrr)