fruit = {"apple", "banana", "avocado", "orange", "tomato", "watermelon"}
vegetable = {"celery", "kale", "turnip", "carrot", "spinach", "avocado", "tomato"}

print ("FRUIT: " + ', '.join(fruit))
print ("VEGETABLES: " + ', '.join(vegetable))

print ("The UNION of fruit and vegetables is: {0}".format(fruit.union(vegetable)))
print ("The INTERSECTION of fruit and vegetables is: {0}".format(fruit.intersection(vegetable)))
print ("The DIFFERENCE of fruit and vegetables is: {0}".format(fruit.difference(vegetable)))
print ("The SYMMETRIC DIFFERENCE of fruit and vegetables is: {0}".format(fruit.symmetric_difference(vegetable)))

'''
NOTE:
[] = empty list
() = empty tuple
{} = empty dictionary
set() = empty set
'''
