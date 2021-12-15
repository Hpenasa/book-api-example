from logging import fatal
from os import truncate
import sqlite3
from sqlite3 import Error


from .connection import create_connection



def insert_book(data):
    conn = create_connection()

    sql = """ INSERT INTO books (ISBN, title, author, price)
             VALUES (?, ?, ?, ?)   
    """

    try: 
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error at Insert_book() : {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id(_id):
    conn = create_connection()

    sql = f"SELECT * FROM books WHERE id = {_id}"

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        books = dict(cur.fetchone())
        return books
    except Error as e:
        print(f"Error at select_book_by_id : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



    
def select_all_books():
    conn = create_connection()

    sql = "SELECT * FROM books"
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        book_rows = cur.fetchall()
        books = [ dict(row) for row in book_rows ]
        return books
    except Error as e:
        print(f"Error at Select_all_Query() : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book(bookupdated):
    conn = create_connection()
    print (bookupdated)

    sql = """  UPDATE books SET isbn = %(isbn)s, title = '%(title)s', author = '%(author)s', price = %(price)s
                WHERE id = %(id)s;
            """ % bookupdated
    

    
    try: 
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at PUT() : {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()


def patch_books(updated_book):
    actualbook = select_book_by_id(updated_book.get('id'))
    
    conn = create_connection()
    
    if (updated_book.get('isbn')):
        actualbook['isbn'] = updated_book.get('isbn')
        
    if(updated_book.get('title')):
        actualbook['title'] = updated_book.get('title')
    
    if(updated_book.get('author')):
        actualbook['author'] = updated_book.get('author')

    if(updated_book.get('price')):
        actualbook['price'] = updated_book.get('price')
    
    try: 
        update_book(actualbook)
        return True
    except Error as e:
        print(f"Error at patch() : {str(e)}")
    


def delete_book(_id):
    conn = create_connection()

    sql = f"DELETE FROM books WHERE id = {_id}"

    try: 
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at delete() : {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()



    
