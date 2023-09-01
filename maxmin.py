
def max_min(dataset):
  for i in dataset:
    if type(i) is int:
      continue
    else:
      return "Input not compatible: " + i
      break
  sorted_list = sorted(dataset)
  return [sorted_list[0], sorted_list[-1]]

print(max_min([2, 4, 1, 0, 2, -1]))