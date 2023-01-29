#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruit = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruit)
fruits = {"orange", "apple", "pear", "banana", "kiwi", "apple", "banana"}
print(fruits)
newfruits = ("orange", "apple", "pear", "banana", "kiwi", "apple", "banana")
print(newfruits)