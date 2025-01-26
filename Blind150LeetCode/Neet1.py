## LeetCode#217 - Contains Duplicates

# step 1: Sort the list -> O(nLogn)

# Optimizing the above can be achieved by :
# Keep track of things and access them quickly -> Hash Set

# Time: O(n)
# Space: O(n)


def containsDuplicate(elems_array):

  elems = set()
  for item in elems_array:
    
