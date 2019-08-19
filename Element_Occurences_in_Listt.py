#Anton Durham
#7/16/2019
#Desc: Function that returns indices of all occurences of an item in a given list


def get_indices(lst, el):
  lst2 = []
  for i in range(len(lst)):
      if(el == lst[i]):
          lst2.append(i)
  return lst2


#Test Cases
#Test.assert_equals(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'), [0, 1, 3, 5])
#Test.assert_equals(get_indices([1, 5, 5, 2, 7], 7), [4])
#Test.assert_equals(get_indices([1, 5, 5, 2, 7], 5),[1, 2])
