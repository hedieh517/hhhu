import tkinter as tk
import csv

data = ["Ali", "Sara", "Reza", "Maryam", "Hossein"]

def update_list(items):
    listbox.delete(0, tk.END)
    for i in items:
        listbox.insert(tk.END, i)

# جستجو بين اسم ها بر اساس متن ورودی
def search():
    text = entry.get()
    result = []
    for name in data:
        if text in name:
            result.append(name)
    update_list(result)



####################################################################################




# حذف کردن مخاطب انتخاب شده از ليستمون
def delete():
    sel = listbox.curselection()
    if sel:
        name = listbox.get(sel[0])
        data.remove(name)
        update_list(data)



####################################################################################


# قبل از خارخ شدن اطلاعات ذخيره ميشه توی فايل
def exit_app():
    with open("save_to_csv.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for name in data:
            writer.writerow([name])
    root.destroy()

root = tk.Tk()
root.title("Contacts")

entry = tk.Entry(root)
entry.pack()

btn_search = tk.Button(root, text="جستجو", command=search)
btn_search.pack()

listbox = tk.Listbox(root)
listbox.pack()

btn_delete = tk.Button(root, text="حذف", command=delete)
btn_delete.pack()

btn_exit = tk.Button(root, text="خروج", command=exit_app)
btn_exit.pack()


####################################################################################


update_list(data)

root.mainloop()
  
    
  
    
  
    
