from mindee import Client, PredictResponse, product
import json


# Init a new client
mindee_client = Client(api_key="57f9525e3143c1bafb47b2db82ef5e79")

# Load a file from disk
input_doc = mindee_client.source_from_path("../test_data/receipt_7.png")

# Load a file from disk and parse it.
# The endpoint name must be specified since it cannot be determined from the class.
result: PredictResponse = mindee_client.parse(product.ReceiptV5, input_doc)

# Print a summary of the API result
# print(type(result.document.inference.prediction.total_amount.value))

# with open('test.txt', 'a') as file:
#     # Write the text to the file
#     file.write(str(result.document.inference.prediction.total_amount.value))

# print(result.document.inference.prediction.total_amount)
# line_items = result.document.inference.prediction.line_items
# for item in line_items:
#     print(item.description, type(item.description),  end=", ")
#     if item.quantity is not None:
#         print(item.quantity, type(item.quantity), end=", ")
#     else:
#         print("1")
#     if item.unit_price is not None:
#         print(item.unit_price, type(item.unit_price), end=", ")
#     print(item.total_amount, type(item.total_amount))
data = result.document.inference.prediction
print(data.locale.country)
print(data.locale.language)
print(data.category.value)
print(data.date.value)

# Print the document-level summary


# with open("result.json", "w") as json_file:
    # json.dump(result.document.inference.prediction, json_file, indent=4)


'''

prediction content can be accesed by using . operator
['category', 'date', 'document_type', 'line_items', 'locale', 'subcategory', 'supplier_address', 'supplier_company_registrations', 'supplier_name', 'supplier_phone_number', 'taxes', 'time', 'tip', 'total_amount', 'total_net', 'total_tax', '__module__', '__annotations__', '__doc__', '__init__', '_line_items_separator', '_line_items_to_str', '__str__', '__dict__', '__weakref__', '__new__', '__repr__', '__hash__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

line_items is list

'''