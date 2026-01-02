#Tuples

tuple2 = (1, 4, 2, 7, 8)  # Use round braces to define a tuple

def find_min_max(tup):
    # Sort the tuple by converting it to a list
    sorted_tuple = sorted(tup)
    
    # Maximum value (last element in the sorted list)
    max_val = sorted_tuple[-1]
    
    # Second smallest value (second element in the sorted list)
    second_smallest = sorted_tuple[1]
    
    # Return both values as a tuple
    return (max_val, second_smallest)

#Function call
print(find_min_max(tuple2))
