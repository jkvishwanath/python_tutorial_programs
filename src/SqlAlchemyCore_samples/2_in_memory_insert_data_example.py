from sqlalchemy import insert


from src.SqlAlchemyCore_samples.in_memory_db_ful_exqample import cookies,engine

insert_one_entry = cookies.insert().values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)
# too see natural db query
print(str(insert_one_entry))
# print(str(ins))
# INSERT INTO cookies
#   (cookie_name, cookie_recipe_url, cookie_sku, quantity, unit_cost)
# VALUES
#   (:cookie_name, :cookie_recipe_url, :cookie_sku, :quantity, :unit_cost)

# pprint(ins.compile().params)
# {'cookie_name': 'chocolate chip',
#  'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
#  'cookie_sku': 'CC01',
#  'quantity': '12',
#  'unit_cost': '0.50'}

connection = engine.connect()
result = connection.execute(insert_one_entry)
print(result.inserted_primary_key)

# Insert can also be called as a top-level function
ins2 = insert(cookies).values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)

# Provide values for insertion separately
ins3 = cookies.insert()
result3 = connection.execute(
    ins3,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
)
print(result3.inserted_primary_key)


# Insert multiple values
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]

connection.execute(cookies.insert(),inventory_list)
