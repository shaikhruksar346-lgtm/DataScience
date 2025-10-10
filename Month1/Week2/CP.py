Data Cleaning Script (Remove Duplicates)
def remove_duplicates(data_list):
    return list(set(data_list))

data_with_duplicates = ['apple', 'banana', 'apple', 'orange', 'banana']
cleaned_data = remove_duplicates(data_with_duplicates)
print("Cleaned data:", cleaned_data)
