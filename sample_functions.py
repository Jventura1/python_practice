'''this will be a collection of our first set of functions '''

# Our First function!!
def max_of_three(arg1,arg2,arg3):
    '''this function takes in three arguments and returns the largest value'''
    if arg1>arg2 and arg1>arg3:
        return arg1
    elif arg2>arg3 and arg2>arg1:
            return arg2
    else:
        return arg3

#our second function!!
def list_ends(L):
    '''This function takes in a list and returns a new list with the first and last entries'''
    final_list = []
    list_size = len(L)
    final_list.append(L[0])
    final_list.append(L[list_size-1]) 
    return final_list
