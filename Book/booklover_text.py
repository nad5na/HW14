import unittest

class BookLoverTestSuite(unittest.TestCase): 
        
    def test_1_add_book(self):
        # Add a book and test if it is in book_list
        noah = BookLover('Noah','nad5na','fiction')
        noah.add_book('Hunger Games',4)
        self.assertEqual(noah.has_read('Hunger Games'), True)
  
    def test_2_add_book(self):
        # Add the same book twice. Test if it's in book_list only once
        grace = BookLover('Grace','grace.gmail','nonfiction')
        grace.add_book('Catan',3)
        grace.add_book('Catan',3)
        self.assertTrue(grace.num_books_read() == 1)

    def test_3_has_read(self):
        # Pass a book in the list and test the answer is True
        shannon = BookLover('shannon','shannon.gmail','fiction')
        shannon.add_book('Dune',5)
        self.assertEqual(shannon.has_read('Dune'), True)
        
    def test_4_has_read(self):
        # Pass a book NOT in the list and use assert False to test if the 
answer is True
        barry = BookLover('Barry','barry.gmail','fiction')
        barry.add_book('Foundation',5)
        self.assertFalse(barry.has_read('Dune'), False)
        
    def test_5_num_books_read(self):
        # Add some books to the list, and test num_books matches expected
        sean = BookLover('Sean','sean.gmail','nonfiction')
        sean.add_book('Caves of Steel',3)
        sean.add_book('Divergent',4)
        sean.add_book('Naked Sun',2)
        sean.add_book('Pebble in the Sky',5)
        self.assertEqual(sean.num_books_read(), 4)
        
    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of 
them have rating > 3
        # Your test should check that the returned books have rating > 3
        summer = BookLover('Summer','summer.gmail','nonfiction')
        summer.add_book('HP 1',1)
        summer.add_book('HP 2',4)
        summer.add_book('HP 3',2)
        summer.add_book('HP 4',5)
        
        faves = []
        for i, val in summer.fav_books().book_name.items():
            faves.append(summer.fav_books().book_name[i])
        self.assertTrue('HP 2' in faves)
        self.assertTrue('HP 4' in faves)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
