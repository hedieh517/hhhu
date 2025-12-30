import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        
####################################################################################        
        # گرفتن مبلغ کل از ورودیی
        total = float(entry_total.get())
        
        
####################################################################################
        
        # گرفتن تعداد تفرات از ورودی
        people = int(entry_people.get())

        if people == 0:
            messagebox.showwarning("خطا", "تعداد نفرات نميتوه که صفر باشه")
            return

        share = total / people

        messagebox.showinfo("نتيجه", f"سهم هر نفر: {share} تومان")


####################################################################################
    except:
        # اگر کاربر به جای عدد حروف الف با را وارد کنه
        messagebox.showwarning("خطا", "لطفا عدد درست وارد کنيد")




root = tk.Tk()
root.title("محاسبه خرج دوستانه")
root.geometry("300x200")

label_total = tk.Label(root, text="مبلغ کل")
label_total.pack()

entry_total = tk.Entry(root)
entry_total.pack()

label_people = tk.Label(root, text="تعداد نفرات")
label_people.pack()

entry_people = tk.Entry(root)
entry_people.pack()

btn = tk.Button(root, text="محاسبه کردن سعم هر نفر", command=calculate)
btn.pack(pady=10)

root.mainloop()
