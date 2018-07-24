import os

from boto3 import resource
from lambdarest import lambda_handler
from slugify import slugify


BOOKS_TABLE_NAME = os.getenv('BOOKS_TABLE_NAME')
dynamodb = resource('dynamodb')

books_table = dynamodb.Table(BOOKS_TABLE_NAME)


@lambda_handler.handle('post', path='/books')
def add_book(event):
    book_data = event['json']['body']
    book_data['id'] = slugify(book_data['title'])
    books_table.put_item(Item=book_data)
    return book_data


@lambda_handler.handle('get', path='/books/<book_id>')
def get_book(event, book_id):
    print('book id: ', book_id)
    book_details = books_table.get_item(
        Key={'id': book_id}
    )
    return book_details['Item']


@lambda_handler.handle('get', path='/books')
def get_books(event):
    books = books_table.scan()
    return books['Items']
