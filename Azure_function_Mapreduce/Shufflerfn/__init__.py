# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from collections import defaultdict
import logging

def main(pairs: tuple[str, int]) -> tuple[str, int]:
  out = defaultdict(list)
  items = []
  shufflerkey = []
  for pair in pairs:
    keys = pair.keys()
    values = pair.values()
    for pat,pat1 in zip(keys,values):
      items.append((pat, pat1))
  return items