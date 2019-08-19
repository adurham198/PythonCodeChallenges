#Anton Durham
#Date: 8/2/2019
#Desc: This program evaluates test arrays of boolean values
#and returns the final state of them. 

def boolean_and(lst)
	return all(lst)

def boolean_or(lst):
	if True in lst:
		return True
	else:
		return False

def boolean_xor(lst):
	if lst.count(True) == lst.count(False):
		return False
	elif lst.count(True) == len(lst) or lst.count(False) == len(lst):
		return False
	elif lst.count(True) == 1 or lst.count(True) > lst.count(False):
		return True
#Test cases:
    # AND tests
#Test.assert_equals(boolean_and([True, True, False, True]), False)
#Test.assert_equals(boolean_and([True, True, True, True]), True)
#Test.assert_equals(boolean_and([False, True, True, True]), False)
#Test.assert_equals(boolean_and([False, False, False, False]), False)
#Test.assert_equals(boolean_and([False, False, True, True]), False)

# OR tests
#Test.assert_equals(boolean_or([True, True, False, False]), True)
#Test.assert_equals(boolean_or([True, False, False, False]), True)
#Test.assert_equals(boolean_or([False, False, False, True, False]), True)
#Test.assert_equals(boolean_or([False, True, False, True, False, True]), True)
#Test.assert_equals(boolean_or([False, False, False, False, False]), False)

# XOR tests
#Test.assert_equals(boolean_xor([True, True, False, True]), True)
#Test.assert_equals(boolean_xor([True, True, False, False]), False)
#Test.assert_equals(boolean_xor([True, False, False, False]), True)
#Test.assert_equals(boolean_xor([True, False, True, False]), False)
#Test.assert_equals(boolean_xor([True, True, True, True]), False)
#Test.assert_equals(boolean_xor([False, False, False, False]), False)
#Test.assert_equals(boolean_xor([False, False, False, True]), True)
#Test.assert_equals(boolean_xor([True, False, False, True]), False)
