records = ["Learn Python - 13", "Learn Java - 22",
           "Learn Python - 5", "Learn HTMl - 20", "Learn Java - 5"]

books = {}

for record in records:
    # ["Learn Python", "13"]
    book = record.split(" - ")
    title = book[0]
    days = int(book[1])
    if title in books:
        books[title] += days
    else:
        books[title] = days


books_unique = set(books.keys())

max_borrowed = max(books.items(), key = lambda x: x[1])#("Learn Java", 27)
min_borrowed = min(books.items(), key = lambda x : x[1])

sorted_books = sorted(books.items(), key = lambda x: x[1], reverse=True)

sum_days =  sum(books.values())
total_books = len(books)
average = sum_days/total_books

print("=================")
print(f"the books unique titles : {books_unique}")
print(f"the most book borrowed : {max_borrowed[0]}, with {max_borrowed[1] } days")
print(f"the least book borrowed : {min_borrowed[0]}, with {min_borrowed[1] } days")
print(f"The average of days is : {average}")
print(f"sorted list : {sorted_books}")


