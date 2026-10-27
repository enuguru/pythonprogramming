# write a python program to remove duplicate elements from a list
def remove_duplicates(input_list):
    # Using a set to remove duplicates
    return list(set(input_list))

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3, 2, 4, 5, 1, 6]
    print("Original list:", sample_list)
    unique_list = remove_duplicates(sample_list)
    print("List after removing duplicates:", unique_list)


