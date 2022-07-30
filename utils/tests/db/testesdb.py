dicionario = {
    "products": [
        {
            "id": 1234,
            "productName":"ProductTest",
            "type": 1, 
            "price": 19.90,
            "avaliable": True
        },
        {
            "id": 2345,
            "productName":"nome",
            "type": 1, 
            "price": 19.90,
            "avaliable": True
        },
        {
            "id": 3456,
            "productName": "nome",
            "type": 1, 
            "price": 19.90,
            "avaliable": True
        }
    ],
    "users": [
        {
            "name": "Admin",
            "login": "AdminLog",
            "products": []
        }
    ],
    "purchaseHistory": [
        {
            "productID": 1234,
            "user": "Admin", 
            "productName": "ProductTest",
            "date": "data de compra"
        }
    ]
}

print(dicionario)