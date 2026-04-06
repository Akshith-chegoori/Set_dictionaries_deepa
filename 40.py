library = {
    'Ravi':  ['Python Basics', 'DSA', 'DBMS'],
    'Priya': ['OS', 'Python Basics', 'Networks'],
    'Arjun': ['DSA', 'OS', 'Python Basics']
}
all=[]
book=set()
sa=set(library['Ravi']) & set(library['Priya']) & set(library['Arjun'])

for names,books in library.items():
    book.update(books)
    all.extend(books)
    if 'DSA' in books:
        print(names)
print(book) 

sa.intersection(library['Ravi'], library['Priya'], library['Arjun'])
print(sa)
