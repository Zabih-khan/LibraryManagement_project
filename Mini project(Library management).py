class Library:
    def __init__(self,name,*bookList):
        self.library_name=name
        self.bookList=list(bookList)

        #This is a blink dictionary
        #in this we store  who take the book which book.
        self.lendDict={}
    def displayBooks(self):
        print(f"We have the following books in our library:{self.library_name} ")
        for book in self.bookList:
            print(book)  
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender -database has been updated.You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.bookList.append(book)
        print("Book is been added to the book list.")
    def returnBook(self,book):
        self.lendDict.pop(book)

harry=Library("Student","python","rich dady poor daddy","c++ basic","English")

##if __name__ == '__main__':
while(True):
        print(f" ====== Welcome to {harry.library_name} Library ======")
        print("Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend a Books")
        print("3.Add a Books")

        print("4.Return a Books")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue
        else:
            user_choice=int(user_choice)
            
        if user_choice==1:
            harry.displayBooks()
            

        elif user_choice==2:
            book=input("Enter the name of the book that you want to lend")
            user_name=input("enter your name")
            harry.lendBook(user_name,book)
             
        elif user_choice==3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice==4:
            book=input ("Enter the name of the book that you want to return:")
            harry.returnBook(book)
  
        else:
            print("Not a valid option")
        print("press q to quit and c to continue")

        user_choice2=()
        while (user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice=="c":
                continue

            
        


        









        
        

            








        

