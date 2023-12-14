import functools

def absSort(arr):
    def abs_sort(a, b):
      if abs(a) < abs(b): return -1
      if abs(a) > abs(b): return 1
      if a < b: return -1
      if a > b: return 1
      return 0
  
    # return sorted(arr, key=functools.cmp_to_key(abs_sort))
    arr.sort(key=functools.cmp_to_key(abs_sort))
    return arr