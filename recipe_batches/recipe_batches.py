#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

# for each key in recipe, ingredient.key // ingredient.key, 
  # if all results > 0, return highest common result

def recipe_batches(recipe, ingredients):
  current_qty = 0
  batches = 0
  for val1 in recipe.values():
    for val2 in ingredients.values():
      if (val2 // val1) > 0:
        current_qty = val2 // val1
      if current_qty < batches: 
        batches = current_qty

recipe_batches(recipe, ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))