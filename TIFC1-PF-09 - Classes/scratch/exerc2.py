class Book():
    def __init__(self, title, author, genre ):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"My book title is: {self.title}")
        print(f"My book author is: {self.author}")
        print(f"My book genre is: {self.genre}")

    def update_page(self, page):
      self.page = page
      

    
Book1 = ('Harry Potter', 'J. K. Rowling', 'fantasy literature')
Book2 = ('Ramayana', 'Valmiki',' Itihasa')

#Book1.display_info()
#Book2.display_info()

#Book1.update_page(4)
#Book1.display_info

