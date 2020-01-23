#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 60, 'flour': 51 }


# for each key in recipe, ingredient.key // ingredient.key, 
  # if all results > 0, return highest common result

def recipe_batches(r, i):
  current_qty = 0 # first pass makes this 1.
  batches = i["milk"] // r["milk"]
  for k1 in r.keys():
    for k2 in i.keys():
      if k1 not in i.keys():
        return 0
      if k1 == k2:
        if (i[k2] // r[k1]) > 0:
          current_qty = i[k2] // r[k1]
        if current_qty < batches: 
          batches = current_qty
  return batches


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 60, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))