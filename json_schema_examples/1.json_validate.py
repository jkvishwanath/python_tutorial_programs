import json
import jsonschema
from jsonschema import validate

# pip install jsonschema
# https://github.com/donofden/python-validate-json-schema/blob/master/json_validate.py
# http://donofden.com/blog/2020/03/15/How-to-Validate-JSON-Schema-using-Python

def get_schema(filename):
    """This function loads the given schema available"""
    with open(f'{filename}.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema('1.user_schema')

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


# Convert json to python object.
jsonData = json.loads('{"id" : "10","name": "DonOfDen","contact_number":1234567890}')
# jsonData = json.loads('{"id" : 10,"name": "DonOfDen","contact_number":1234567890}')

# validate it
is_valid, msg = validate_json(jsonData)
print(msg)

# For example, here’s a snippet illustrating how to use the number type:
# { "type": "number" }
# works: 42
# works: -1
#Simple floating point number: 5.0
# Exponential notation also works: 2.99792458e8
# Numbers as strings are rejected: "42"

