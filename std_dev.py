# Author: Erik Blackowicz
# Date: 7/22/20
# Description: Assignment 6c -Create a person class with private data members of name and age.
# Calculations include mean and standard deviation, as well as methods to get name and age.


class Person:
  ''' Creates a person object with private 'name' and 'age' parameters '''
  def __init__(self, name, age):
    """ creates new person with specified name and age """
    self._name = name # name & age parameters initialized as private data members
    self._age = age

  def get_name(self):
    """ Returns the name of the person"""
    return self._name

  def get_age(self):
    """ Returns the age of the person"""
    return self._age

def meen(age_list):
  ''' Returns the mean value of ages from the person class'''
  count=0
  for person in age_list:
    count += person.get_age()
  return count/len(age_list)

def std_dev(list1):
  ''' Returns (population) standard deviation for the list of ages in the person class '''
  list_mean = meen(list1)
  list_len = len(list1)
  diff_sqr = [(person.get_age() - list_mean) ** 2 for person in list1]  # use list compreh. to find each list value's absolute deviation from the mean-squared
  sum_of_dev = 0  # cant use sum()
  for num1 in diff_sqr:  # must use for loop to find the sum of all list deviations
    sum_of_dev = sum_of_dev + num1
  variance = sum_of_dev / list_len  # take sum of the deviations divided by length
  return (variance ** 0.5)  # returns standard deviation

