#اطلاعات کتابو بگبره و بعد درصد تخفیف بگیره و از قیمت کم کنه
# تمرین4
class Book:
    def __init__(self , title , author , price):
        self.title = title
        self.author = author
        self.price = price
        
        
    def display_details(self):
        print(f"عنوان کتاب {self.title}:")
        print(f"نویسنده ی کتاب: {self.author}")
        print(f"قیمت کتاب : {self.price} دلار")
                  
        
    def apply_discount(self,percent):
        self.discount_takhfif = self.price * (percent / 100)
        self.price -= self.discount_takhfif      
        
        
title = input("عنوان کتاب را وارد کنین:")
author = input("نام نویسنده را وارد کنین:")
price = int(input("قیمت کتاب را وارد کنین:"))

book1 = Book(title , author , price)

percent = int(input("درصد تخفیف را وارد کنبن:"))
book1.apply_discount(percent)

print(f"بعد از تخفیف *****{book1.discount_takhfif}")
book1.discount_takhfif()

