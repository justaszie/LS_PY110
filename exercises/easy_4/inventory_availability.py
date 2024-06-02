"""
PROBLEM
- Input: item id (int) and transactions (list of dictionaries)
- Output: True / False representing whether the item matching input item id is available 
- Explicit Rules:
    - True if final quantity for the item is > 0. False otherwise.
    - Final quantity = (sum of all "in" transactions for the item - sum of all "out" transactions for the item)
    - Use "transactions_for" function 
- Implicit Rules
    - Assuming False if no transactions at all for the item. 
- Questions
    - N/A

EXAMPLES
- 3 examples Provided
- Additional example for the case with no transactions for the item 
transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 ]
print(is_item_available(1099, transactions))
# Outputs False

DATA STRUCTURES
- List of dictionaries 

ALGORITHM
1. Set item quantity = 0 
2. get all the transactions for the item
3. Sum up the quantity values of "inbound" transactions
4. sum up the quantity values of "outbound" transactions
5. Add the sum of inbound transactions quantity to item quantity
6. Subtract the sum of outbound transactions quantity from the item quantity
7. if item quantity > 0:
    - return True
8. else:
    - return False 

IMPLEM NOTES
- start with quantity = 0, in case no transactions at all 
- create a get_quantity_sum(transactions, direction) function for steps 3 & 4
"""

def transactions_for(item_id, transactions):
    return [transaction for transaction in transactions if transaction['id'] == item_id]

def get_quantity_sum(transactions, direction):
    total = 0 + sum([txn['quantity'] for txn in transactions if txn["movement"] == direction])
    return total


def is_item_available(item_id, transactions):
    quantity = 0
    item_transactions = transactions_for(item_id, transactions)

    quantity += get_quantity_sum(item_transactions, "in")
    quantity -= get_quantity_sum(item_transactions, "out")

    return quantity > 0


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

print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True
print(is_item_available(1000, transactions))  # False