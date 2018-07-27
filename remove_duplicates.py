# Define the remove_duplicates function
def remove_duplicates(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result
