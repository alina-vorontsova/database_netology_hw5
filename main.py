import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from database_connection import get_DSN


engine = sq.create_engine(get_DSN())

Session = sessionmaker(bind=engine)
session = Session()

def insert_data():
    with open('test_data.json', 'r') as file_to_read:
        data = json.load(file_to_read)

    for d in data: 
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale
        }[d.get('model')]
        session.add(model(id=d.get('pk'), **d.get('fields')))
    session.commit()

def get_shops():
    while True: 
        command = int(input('Введите 1, чтобы выполнить поиск через имя издателя. Введите 0, чтобы выполнить поиск через идентификатор издателя. '))
        if command == 0:
            for shop in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == int(input('Идентификатор целевого издателя: '))).all():
                print(shop)
            break 
        if command == 1:
            for shop in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == input('Название целевого издателя: ')).all():
                print(shop)
            break


if __name__ == '__main__':
    create_tables(engine)
    insert_data()
    get_shops()


session.close()