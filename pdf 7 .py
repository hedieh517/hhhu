# کلاس ساده برای مخاطب‌  ها
class Contact:
    def __init__(self, name, phone):
        if not phone.isdigit():
            raise ValueError("شماره باید فقط عدد باشه")
        self.name = name
        self.phone = phone
####################################################################################


# لیست مخاطب‌ها رو اینجا نگه میدارییم
contacts = []




while True:
    print("\nمنوی اصلی:")
    print("1. افزودن مخاطب")
    print("2. نمایش همه")
    print("3. ذخیره و خروج")

####################################################################################


    # گرفتن ورودی منو
    try:
        choice = int(input("لطفا شماره گزینه رو وارد کن: "))
    except ValueError:
        print("لطفا عدد وارد کنید")
        continue

    if choice == 1:
        
        
####################################################################################
        
        # گرفتنن اطلاعات مخاطب
        name = input("نام مخاطب: ")
        phone = input("شمارهه مخاطب: ")
        try:
            new_contact = Contact(name, phone)
            contacts.append(new_contact)
            print("مخاطب با موفقیت اضافه شد")
        except ValueError:
            print("فرمت شماره اشتباه است، دوباره تلاش کنید.")

    elif choice == 2:
        
####################################################################################       
        
        # نمایش دادن همه مخاطبان
        if not contacts:
            print("مخاطبی اضافه نکردین هنووز")
        else:
            print("لیست مخاطب‌ها:")
            for c in contacts:
                print(f"{c.name} - {c.phone}")

    elif choice == 3:
        print("برنامه در حال ذخیره‌سازی و خروج است...")
        break

    else:
        print("گزینه نامعتبره، لطفا یکی از گزینه‌های منو رو انتخاب کن")
