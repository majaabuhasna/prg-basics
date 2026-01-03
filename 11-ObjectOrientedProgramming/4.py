class Ebook:
    def __init__(self,title,author,number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_open = False
        self.page = 1

    def open(self):
        self.is_open = True
        print("You just opened the e-book!")

    def close(self):
        self.is_open = False
        print("You just closed the e-book!")

    def next_page(self):
        if self.is_open:
            if self.page >= 1 and self.page < self.number_of_pages:
                self.page += 1
                print(f"You are now on page {self.page}!")
            else:
                print("No more pages left.")
        else:
            print(f"You cannot turn pages. The e-book is closed.")

    def previous_page(self):
        if self.is_open:
            if self.page > 1 and self.page <= self.number_of_pages:
                self.page -= 1
                print(f"You are now back to page {self.page}!")
        else:
            print(f"You cannot turn pages. The e-book is closed.")

    def status(self):
        print(f"The title of the E-book is {self.title}.")
        print(f"The author is {self.author}.")
        print(f"It has {self.number_of_pages} pages.")
        if self.open:
            print(f"Currently, page number {self.page} is open.")
        else:
            print(f"The e-book is currently closed.")

def main():
    my_ebook = Ebook('Misery','Stephen King',368)
    my_ebook.open()
    my_ebook.status()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.previous_page()
    my_ebook.status()
    my_ebook.close()
    my_ebook.next_page()

if __name__ == '__main__':
    main()