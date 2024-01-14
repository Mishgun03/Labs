volume_floppy = 1.44
count_page = 100
count_row = 50
count_char = 25
BYTE_CHAR = 4

volume_book_in_byte = BYTE_CHAR * count_char * count_row * count_page
volume_floppy_in_byte = volume_floppy * (1024**2)

count_book = int(volume_floppy_in_byte // volume_book_in_byte)

print("Количество книг, помещающихся на дискету:", count_book)
