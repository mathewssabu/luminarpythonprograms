class Books:
    def show(self):

        print("Book method")


class Sub(Books):
    def show(self):

        print("Sub method")


o = Sub()
o.show()