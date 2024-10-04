from uuid import uuid4


class Customer:
    def __init__(self, name: str, email: str, phone_number: int):
        self.customer_id = uuid4()
        self.name = name
        self.email = email
        self.phone_number = phone_number
