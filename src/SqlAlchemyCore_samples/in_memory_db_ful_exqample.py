from sqlalchemy import Table, Column, MetaData, Integer, String, Numeric,DateTime,ForeignKey,Boolean,create_engine
from datetime import datetime

metadata = MetaData()
cookies = Table('cookies', metadata, 
                Column('cookies_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)), Column('cookie_sku', String(55)),
                Column('quantity', Integer()), Column('unit_cost', Numeric(12, 2)))


users = Table(
    'users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on',DateTime(),default=datetime.now()),
    Column('updated_on',DateTime(),default=datetime.now(),onupdate=datetime.now()))

orders = Table(
    'orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id',ForeignKey('users.user_id')),
    Column('shipped',Boolean(),default=False))


line_items = Table(
    'line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookies_id', ForeignKey('cookies.cookies_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)

engine = create_engine('sqlite:///C:\\app\\sqlite_3.db')
metadata.create_all(engine)
