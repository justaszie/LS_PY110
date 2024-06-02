"""
PROBLEM
- Input: 
    - Inventory Item ID (int)
    - List of transactions (dictionary)
- Output: List of transactions (list of dict) for the item ID specified by input
- Explicit Rules:
    - Input item ID is integer
    - Input list of transactions is a list of dictionary values. Each dictionary has the format:
        {'id' : {int id}, 
        "movement": {"in" / "out"}, 
        "quantity": {int quantity}
        }
    - Output format is the same as transactions input format.
    - Output list contains dictionary values where id == input item id value.
    - 
- Implicit Rules:
    - Assuming that no validation of input values is required. 
    - Assuming that output is empty list if no transactions match the input ID
- Questions: 
    - input transactions validatio required? 
        - id > 0
        - quantity > 0
        - movement: must be "in" or "out" in lowervase

EXAMPLES
- 1 example Provided 
- Additional example :
transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10}]
print(transactions_for(1000, transactions))
# Outputs: [] 


DATA STRUCTURES
List of dictionaries [{}, {}] where each dictionary is a transaction. Used in input and output

ALGORITHM
1. Create an empty list "result"
2. Iterate over the input list of transactions. For each transaction:
    A. If the value associated with "id" key of the current transaction matches the input id value:
        - Add the current transaction to the "result" list
3. Return the "result" list 

IMPLEM NOTES
- selection based on id value
- no transformation 

transaction in tra

"""

def transactions_for(item_id, transactions):
    return [transaction for transaction in transactions if transaction['id'] == item_id]

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

print(transactions_for(101, transactions))
# prints
# [ {"id": 101, "movement": "in",  "quantity":  5},
#   {"id": 101, "movement": "in",  "quantity": 12},
#   {"id": 101, "movement": "out", "quantity": 18} ]


print(transactions_for(1000, transactions))