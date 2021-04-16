class Book:
    def set(self,Library_name,book_name,author,pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def get(self):
       print(self.Library_name,self.book_name,self.author,self.pages)


ob = Book()
ob.set("central librarry","seven seas","mark",300)
ob.get()