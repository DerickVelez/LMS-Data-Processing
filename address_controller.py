from fastapi import FastAPI
from schemas import Addresses
from tables.addresses import AddressRepository 
from typing import List

app = FastAPI()

@app.get('/get')   
def get_address() -> List[Addresses]: 
    address_repository = AddressRepository()
    addresses = []
    address_list = address_repository.get_all()
    
    for row in address_list:
        address = Addresses(address_id= row[0],current_address= row[1],permanent_address=row[2])
        addresses.append(address)

    return addresses
    
    
    
@app.put('/update') 
def update(current_address: str, permanent_address: str, address_id: int):
    address_repository = AddressRepository()
    updated_address = address_repository.update_address(current_address=current_address,permanent_address=permanent_address,address_id=address_id)
    Addresses(address_id=updated_address[2],current_address=updated_address[0],permanent_address=updated_address[1])
    return [{
        "address_id: {Addresses.address_id}",
        "current_address: {Addresses.current_address}",
        "permanent_address: {Addresses.permanent_address}"
        
    }]
    



@app.post("/create_user/") #No response
async def create_address(current_address: str, permanent_address: str):
    ar = AddressRepository()
    ar.create_address(current_address=current_address, permanent_address=permanent_address)

@app.delete('/delete')
def delete_address(id:int):
    ar = AddressRepository()
    ar.delete_address(address_id= id)
    
@app.get('/get_by_id') 
def get_by_id(id:int) -> List[Addresses]:
    ar = AddressRepository()
    address= ar.get_by_id(id)
    
    result =[ Addresses(address_id=address[0],current_address=address[1],permanent_address=address[2])]
    return result

    
