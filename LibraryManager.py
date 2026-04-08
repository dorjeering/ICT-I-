print()
books_list = []
authors_set = set()
books_dict = {}

books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict['Python Programming'] = 'John Smith'

books_list.append("Python Fundamentals")
authors_set.add('John Smith')
books_dict['Python Fundamentals']='John Smith'

books_list.append("Data Structure and Algorithm")
authors_set.add('Jane Doe')
books_dict['Data Structure and Algorithm']='Jane Doe'

books_list.append("Machine Learning Basics")
authors_set.add('Alice Johnson')
books_dict['Machine Learning Basics']='Alice Johnson'

search_title = input("Enter the book title to search: ")
if search_title in books_list:
    print(f"Book found! The author of the book '{search_title}' is {books_dict[search_title]}.")
else:
    print("Book not found")

remove_title = input("Enter the book title to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    del books_dict[remove_title]

    if remove_author not in books_dict.values():
        authors_set.remove(remove_author)
    
    print("Book removed successfully!")
    print("Books available along with their authors: ", books_dict)
    print("Just available books: ", books_list)
    print("Just available authors: ", authors_set)

else:
    print("Book not found")
print()