#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_list = list(recipe.values())
  ing_list = list(ingredients.values())
  ans = []

  # check if arrays of the same length
  if len(recipe_list) != len(ing_list):
    return 0

  # check if items not enough
  for idx, val in enumerate(recipe_list):
    if val > ing_list[idx]:
      return 0
  for j in range(len(ing_list)):
    ans.append(ing_list[j] // recipe_list[j])
  return min(ans)

  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 78, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))