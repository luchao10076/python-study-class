# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:08:06 2018

@author: Joey Lu
"""

def PowerSetsRecursive(items):
  """Use recursive call to return all subsets of items, include empty set"""
   
  if len(items) == 0:
    #if the lsit is empty, return the empty list
    return [[]]
   
  subsets = []
  first_elt = items[0] #first element
  rest_list = items[1:]
   
  #Strategy:Get all subsets of rest_list; for each of those subsets, a full subset list
  #will contain both the original subset as well as a version of the sebset that contains the first_elt
   
  for partial_sebset in PowerSetsRecursive(rest_list):
    subsets.append(partial_sebset)
    next_subset = partial_sebset[:] +[first_elt]
    subsets.append(next_subset)
  return subsets
def PowerSetsRecursive2(items):
  # the power set of the empty set has one element, the empty set
  result = [[]]
  for x in items:
    result.extend([subset + [x] for subset in result])
  return result

print(PowerSetsRecursive2([1,2,3]))