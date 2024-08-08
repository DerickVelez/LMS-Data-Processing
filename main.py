from fastapi import FastAPI, HTTPException
from schemas import Addresses

app = FastAPI()

# address = [
#     {'address_id': 1, 'current_address': 'canlubang', 'permanent_address': 'calamba'},
#     {'address_id': 2, 'current_address': 'canlubang', 'permanent_address': 'calamba'}
# ]

@app.get('/Addresses')   

def address() -> list[Addresses]: 
    
    address = [
    {'address_id': 1, 'current_address': 'canlubang', 'permanent_address': 'calamba'},
    {'address_id': 3, 'current_address': 'canlubang', 'permanent_address': 'calamba'}
]

    return address
        #  "dsf"
    
