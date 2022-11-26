# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df
from collections import Counter

def orchestrator_function(context: df.DurableOrchestrationContext):
    appe = []
    input = yield context.call_activity('Getinputdatafn', None)
    Mapper = []
    for file in input:
        Mapper.append(context.call_activity('Mapperfn', file))
    results = yield context.task_all(Mapper)
    result1 = yield context.call_activity('Shufflerfn', results)
    reducer = []
    for file2 in result1:
        reducer.append(context.call_activity('reduerfn', file2))
    results2 = yield context.task_all(reducer)
    counter = Counter(results2)
    print(counter)
    return counter
main = df.Orchestrator.create(orchestrator_function)