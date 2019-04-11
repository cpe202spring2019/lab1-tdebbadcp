
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None 
   elif int_list == None:
      raise ValueError
   else:
      max = int_list[0]
      for i in int_list:
         if i > max:
            max = i
      return max


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   elif int_list == []:
      return []
   else:
      if len(int_list) == 1:
         return int_list
      else:
        #return reverse_rec(int_list[1:]) + [int_list[0]]
        return [int_list[len(int_list) - 1]] + reverse_rec(int_list[:-1])
 

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   elif int_list == []:
      return []
   else:
      mid = (high + low) // 2
      if int_list[mid] == target:
         return mid
      elif high == low or len(int_list) == mid:
         return None
      elif int_list[mid] > target:
         #return bin_search(target , low , mid - 1 , int_list)
         return bin_search(target, low, mid, int_list)
      else:
         return bin_search(target, mid + 1, high, int_list)

