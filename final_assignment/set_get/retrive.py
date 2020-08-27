
class ProductData():
    def __init__(self, name, discount_code, content_code, cost, product_code, describe, stock):
        self.product_code = product_code
        self.name = name
        self.discount = discount_code
        self.content = content_code
        self.describe = describe
        self.cost = cost
        self.stock = stock

    def set_product_code(self, product_code):
        self.product_code = product_code

    def get_product_code(self):
        return self.product_code

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_discount_code(self, discount):
        self.discount = discount

    def get_discount_code(self):
        return self.discount

    def set_content_code(self, content_code):
        self.content = content_code

    def get_content_code(self):
        return self.content

    def set_describe(self, describe):
        self.describe = describe

    def get_describe(self):
        return self.describe

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def set_stock(self, stock):
        self.stock = stock

    def get_stock(self):
        return self.stock


class Customer():
    def __init__(self, id, first, last, address, phone, delivery, age, email):
        self.id = id
        self.first = first
        self.last = last
        self.address = address
        self.phone = phone
        self.deliver = delivery
        self.age = age
        self.mail = email

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_first_name(self, first):
        self.first = first

    def get_first_name(self):
        return self.first

    def set_last_name(self, last):
        self.last = last

    def get_last_name(self):
        return self.last

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_delivery(self, delivery):
        self.deliver = delivery

    def get_delivery(self):
        return self.deliver

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_mail(self, mail):
        self.last = mail

    def get_mail(self):
        return self.mail


class Offer():
    def __init__(self, discount_id, discount, content_id, content):
        self.discount_id = discount_id
        self.discount = discount
        self.content_id = content_id
        self.content = content

    def set_discount_id(self, discount_id):
        self.discount_id = discount_id

    def get_discount_id(self):
        return self.discount_id

    def set_content_id(self, content_id):
        self.content_id = content_id

    def get_content_id(self):
        return self.content_id

    def set_discount(self, discount):
        self.discount = discount

    def get_discount(self):
        return self.discount

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content


class Buy():
    def __init__(self, id, email, quantity, product_code, date):
        self.id = id
        self.email = email
        self.quantity = quantity
        self.product_code = product_code
        self.date = date

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_email(self, mail):
        self.email = mail

    def get_mail(self):
        return self.email

    def set_quantity(self, quantity):
        self.id = quantity

    def get_quantity(self):
        return self.quantity

    def get_product_code(self):
        return self.product_code

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date