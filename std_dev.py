class Person:
  ''' doc string '''
  def __init__(self, name, age):
    """ creates new person with specified name and age """
    self._name = name # _private
    self._age = age    # _private
  def get_name(self):
    """ doc string"""
    return self._name
  def get_age(self):
    """ doc string"""
    return self._age

def meen(age_list):
  ''' returns the mean for a list of values'''
  count=0
  for person in age_list:
    count += person.get_age()
  return count/len(age_list)

def std_dev(list1):
  ''' doc string'''
  mean = meen(list1)
  list_len = len(list1)
  diff_sqr = [(person.get_age() - mean) ** 2 for person in list1]  # use list compreh. to find each list values absolute deviation from the mean-squared
  sum_of_dev = 0  # cant use sum()
  for num1 in diff_sqr:  # must use for loop to find the sum of all list deviations
    sum_of_dev = sum_of_dev + num1
  variance = sum_of_dev / list_len  # take sum of the deviations divided by length
  return (variance ** 0.5)  # returns standard deviation


p1 = Person("Kyounmin", 99)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1,p2,p3]
answer = std_dev(person_list)
print(answer)