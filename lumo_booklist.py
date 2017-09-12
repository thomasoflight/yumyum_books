import os
import argparse
import lumo_filehandler as l_files

suitcase = argparse.ArgumentParser()


suitcase.add_argument(
		'book_category', 
		 metavar='book_category',
		 help="Which category is this? E.G. 'erth', 'lght', 'soft'")

suitcase.add_argument(
		'book_title', 
		 metavar='book_title',
		 nargs="+",
		 help="So, what is the name of the book(s) you are adding?")

suitcase.add_argument(
		'BOOK CATEGORIES --->',
		nargs='?',
		help="ARTE; SOFT; LGHT; FIC; NONFIC; RECOVERY")


options = suitcase.parse_args()


def main(folder):
    books_group_file = os.path.join(folder, l_files.bookstr_to_filename[(options.book_category).lower()])
    books = [book.title() for book in options.book_title]
    l_files.Wrtrs().basic_wrtr_list(books, books_group_file)

if __name__ == '__main__':
	# print(options.book_category, options.book_title)
	main(l_files.booklist_folder)
