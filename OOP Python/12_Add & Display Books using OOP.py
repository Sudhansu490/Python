class Books:
    def __init__(self):
        self.name=input('Enter Book Name:')
        self.author=input('Enter Author Name:')
        self.price=float(input('Enter Book Price:'))
        self.isbn=input('Enter Book ISBN Number:')
        print(f'{self.name} Book added successfully.')
        print('-'*40)
    
    def displayBooks(self):
        print(f'Book Name: {self.name}')
        print(f'Book Author: {self.author}')
        print(f'Book Price: {self.price}')
        print(f'Book ISBN No: {self.isbn}')
        print('-'*20)

Book_List=[]
while True:
    choice=int(input('Enter Your Choice: \n1.Add Book \n2.DIsplay Book \n3.Stop\n'))
    if choice==1:
        b=Books()
        Book_List.append(b)
    elif choice==2:
        if len(Book_List)==0:
            print('No Book is Available.')
        else:
            for i in Book_List:
                i.displayBooks()
    elif choice==3:
        print('Thanks for using our Book Application.')
        break
    else:
        print('Invalid Choice,Plz choice again.')