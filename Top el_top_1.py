import tkinter as tk
#import json

class AlibabaHyperApp:
    def __init__(self):
        self.search_entry = None
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.title("Alibaba Hyper")
        self.selected_items = {}
        self.total_price = 0
        self.create_login_page()
        self.items = {
            "Sports":{"Football":{"modul":2022,"brand":"add","price":150},
              "Soccar":{"modul":2020,"barnd":"add","price":200},
              "T-shirt":{"modul":2021,"barnd":"add","price":100},
              "Shorts":{"modul":2022,"brand":"add","price":120},
              "Shoes":{"modul":2015,"brand":"add","price":130},
              "Gloves":{"modul":2019,"brand":"add","price":180}
        },
            "Home appliances":{"Oven":{"modul":2022,"brand":"sharp","price":300},
              "mixer":{"modul":2020,"barnd":"sharp","price":500},
              "television":{"modul":2021,"barnd":"aaa","price":600},
              "iron":{"modul":2022,"brand":"dd","price":50},
              "washing machine":{"modul":2015,"brand":"aaaa","price":130},
              "refrigerator":{"modul":2019,"brand":"vv","price":180}

        },
            "Electronics":{"laptop":{"modul":2022,"brand":"apple","price":300},
              "tablet":{"modul":2020,"barnd":"samsung","price":500},
              "phone":{"modul":2021,"barnd":"apple","price":600},
              "watch":{"modul":2022,"brand":"samsung","price":50},
              "power bank":{"modul":2015,"brand":"apple","price":130},
              "heyboard":{"modul":2019,"brand":"apple","price":180}

        },
            "Fashion":{"T-shirt":{"modul":2022,"brand":"add","price":300},
              "jacket":{"modul":2020,"barnd":"sharp","price":500},
              "shirt":{"modul":2021,"barnd":"aaa","price":600},
              "shoes":{"modul":2022,"brand":"dd","price":50},
              "shorts":{"modul":2015,"brand":"aaaa","price":130},
              "pants":{"modul":2019,"brand":"vv","price":180}

        },
            "Books":{"Book 3":{"modul":2022,"brand":"book","price":300},
              "Book 2":{"modul":2020,"barnd":"book","price":500},
              "Book 1":{"modul":2021,"barnd":"book","price":600},
              "Book 6":{"modul":2022,"brand":"book","price":50},
              "Book 4":{"modul":2015,"brand":"book","price":130},
              "Book 5":{"modul":2019,"brand":"book","price":180}

        },
            "food products":{"tomatoes":{"modul":2022,"brand":"food","price":300},
              "carrot":{"modul":2020,"barnd":"food","price":500},
              "onion":{"modul":2021,"barnd":"food","price":600},
              "apple":{"modul":2022,"brand":"food","price":50},
              "grapes":{"modul":2015,"brand":"food","price":130},
              "watermelon":{"modul":2019,"brand":"food","price":180}

        }
    }
        self.item_info_text = None

    def cart(self, items_list):
        store_var = []
        for item in items_list:
            var = tk.IntVar()
            var.set(0)
            item_checkbutton = tk.Checkbutton(
                self.root,
                text=item,
                onvalue=items_list[item]["price"],
                offvalue=0,
                variable=var,
                font=('Arial', 20)
            )
            item_checkbutton.pack(side="top", ipadx=20)
            store_var.append(var)

        def show():
            total = 0
            for a in store_var:
                total += a.get()
            my_label["text"] = f"Total = {total}"

        my_label = tk.Label(self.root, text="")
        my_label.pack()
        tk.Button(
            self.root,
            text="If you want to add anything to the cart, enter here",
            font="Arial 12 bold",
            command=show
        ).pack(padx=0, pady=5)

    def sort(self, category_name):
        category_name = category_name
        items_list = self.items.get(category_name, [])


        def quicksort(dictionary):
            if len(dictionary) <= 1:
                return dictionary
            pivot_key = list(dictionary.keys())[len(dictionary) // 2]
            left = {key: value for key, value in dictionary.items() if key < pivot_key}
            middle = {key: value for key, value in dictionary.items() if key == pivot_key}
            right = {key: value for key, value in dictionary.items() if key > pivot_key}
            return {**quicksort(left), **middle, **quicksort(right)}

        sorted_items = quicksort(items_list)

        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App - Sorted by Name", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.cart(sorted_items)

        btn6 = tk.Button(self.root, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.pack()


    def search(self, category_name):
        category_name = category_name
        search_query = self.search_entry.get()
        items_dict = self.items.get(category_name, {})

        matching_items = {key: value for key, value in items_dict.items() if search_query in key.lower()}

        self.clear_window()
        label = tk.Label(self.root, text=f"Books - Search Results for '{search_query}'", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.cart(matching_items)

        btn6 = tk.Button(self.root, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.pack()




    def create_login_page(self):
        self.clear_window()
        label = tk.Label(self.root, text="Login", font=('arial', 20))
        label.pack(padx=20, pady=20)

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(self.root, name="email_entry")
        email_entry.pack()

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.root, show="*", name="password_entry")
        password_entry.pack()

        error_label = tk.Label(self.root, text="", fg="red", name="error_label")
        error_label.pack()

        login_button = tk.Button(self.root, text="Login", command=self.handle_login)
        login_button.pack()

        register_button = tk.Button(self.root, text="Register", command=self.create_register_page)
        register_button.pack()

    def create_register_page(self):
        self.clear_window()
        label = tk.Label(self.root, text="Register", font=('arial', 20))
        label.pack(padx=20, pady=20)

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        name_label = tk.Label(self.root, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        phone_label_reg = tk.Label(self.root, text='Phone Number:')
        phone_label_reg.pack()
        phone_entry_reg = tk.Entry(self.root)
        phone_entry_reg.pack()

        id_label_reg = tk.Label(self.root, text='Id Number:')
        id_label_reg.pack()
        id_entry_reg = tk.Entry(self.root)
        id_entry_reg.pack()

        age_label_reg = tk.Label(self.root, text='Age:')
        age_label_reg.pack()
        age_entry_reg = tk.Entry(self.root)
        age_entry_reg.pack()

        governorate_label_reg = tk.Label(self.root, text='Governorate:')
        governorate_label_reg.pack()
        governorate_entry_reg = tk.Entry(self.root)
        governorate_entry_reg.pack()

        gender_label_reg = tk.Label(self.root, text='Gender:')
        gender_label_reg.pack()
        gender_entry_reg = tk.Entry(self.root)
        gender_entry_reg.pack()

        back_button = tk.Button(self.root, text="Register", command=self.create_home_page)
        back_button.pack()

        back_button = tk.Button(self.root, text="Back to Login", command=self.create_login_page)
        back_button.pack()


    def create_home_page(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Alibaba Hyper", font=('arial', 20))
        label.pack(padx=20, pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        def home_app():
            self.clear_window()
            self.Home_app()

        btn1 = tk.Button(button_frame, text="Home Appliances", font=('Arial', 50), command=home_app)
        btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        def electronics():
            self.clear_window()
            self.electronics()

        btn2 = tk.Button(button_frame, text="Electronics", font=('Arial', 50), command=electronics)
        btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        def sports():
            self.clear_window()
            self.Sports()

        btn3 = tk.Button(button_frame, text="Sports", font=('Arial', 50), command=sports)
        btn3.grid(row=1, column=0, sticky=tk.W + tk.E)

        def books():
            self.clear_window()
            self.Books()

        btn4 = tk.Button(button_frame, text="Books", font=('Arial', 50), command=books)
        btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

        def fashion():
            self.clear_window()
            self.Fashion()

        btn5 = tk.Button(button_frame, text="Fashion", font=('Arial', 50), command=fashion)
        btn5.grid(row=2, column=0, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')

        def back():
            self.clear_window()
            self.create_login_page()

        btn7 = tk.Button(self.root, text="Logout", font=('Arial', 50), command=back)
        btn7.pack()



    def create_admin_page(self):
        self.clear_window()
        label = tk.Label(self.root, text="Admin Page", font=('arial', 20))
        label.pack(padx=20, pady=20)



        btn = tk.Button(self.root, text="Add", font=('Arial', 50), command=self.add_items)
        btn.pack()

        btn = tk.Button(self.root, text="Home page", font=('Arial', 50), command=self.create_home_page)
        btn.pack()

        btn.pack(fill='x')

    def add_items(self):
        add_item_window = tk.Toplevel(self.root)
        add_item_window.title("Add New Item")

        category_label = tk.Label(add_item_window, text="Category:")
        category_label.pack()
        category_entry = tk.Entry(add_item_window)
        category_entry.pack()

        name_label = tk.Label(add_item_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(add_item_window)
        name_entry.pack()

        model_label = tk.Label(add_item_window, text="Model:")
        model_label.pack()
        model_entry = tk.Entry(add_item_window)
        model_entry.pack()

        brand_label = tk.Label(add_item_window, text="Brand:")
        brand_label.pack()
        brand_entry = tk.Entry(add_item_window)
        brand_entry.pack()

        price_label = tk.Label(add_item_window, text="Price:")
        price_label.pack()
        price_entry = tk.Entry(add_item_window)
        price_entry.pack()

        def add_item():
            category = category_entry.get()
            name = name_entry.get()
            model = model_entry.get()
            brand = brand_entry.get()
            price = float(price_entry.get())

            if category not in self.items:
                self.items[category] = {}

            self.items[category][name] = {
                "modul": model,
                "brand": brand,
                "price": price
            }

            add_item_window.destroy()

        submit_button = tk.Button(add_item_window, text="Add Item", command=add_item)
        submit_button.pack()

        close_button = tk.Button(add_item_window, text="Close", command=add_item_window.destroy)
        close_button.pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def handle_login(self):
        email_entry = self.root.nametowidget("email_entry")

        password_entry = self.root.nametowidget("password_entry")

        error_label = self.root.nametowidget("error_label")

        email = email_entry.get()
        password = password_entry.get()

        if email == "admin@gmail.com" and password == "admin123":
            self.clear_window()
            self.create_admin_page()
        elif email == "normal@gmail.com" and password == "normal123":
            self.clear_window()
            self.create_home_page()
        else:
            error_label.config(text="Invalid email or password")

    def sort_books(self):
        category_name = "Books"
        self.sort(category_name)


    def sort_elec(self):
        category_name = "Electronics"
        self.sort(category_name)

    def sort_Fashion(self):
        category_name = "Fashion"
        self.sort(category_name)

    def sort_Sports(self):
        category_name = "Sports"
        self.sort(category_name)

    def sort_Home_app(self):
        category_name = "Home appliances"
        self.sort(category_name)


    def search_books(self):
        category_name = "Books"
        self.search(category_name)

    def search_sports(self):
        category_name = "Sports"
        self.search(category_name)
    def search_fashion(self):
        category_name = "Fashion"
        self.search(category_name)


    def search_Home_app(self):
        category_name = "Home appliances"
        self.search(category_name)

    def search_Electronics(self):
        category_name = "Electronics"
        self.search(category_name)



    def Home_app(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", font=('Arial', 20), command=self.search_Home_app)
        search_button.pack()

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)



        category_name = "Home appliances"
        items_list = self.items.get(category_name, [])

        self.cart(items_list)

        sort_button = tk.Button(button_frame, text="Sort by Name", font=('Arial', 50), command=self.sort_Home_app)
        sort_button.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn6 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')


    def electronics(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", font=('Arial', 20), command=self.search_Electronics)
        search_button.pack()

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        category_name = "Electronics"
        items_list = self.items.get(category_name, [])

        self.cart(items_list)

        sort_button = tk.Button(button_frame, text="Sort by Name", font=('Arial', 50), command=self.sort_elec)
        sort_button.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn6 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')


    def Books(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", font=('Arial', 20), command=self.search_books)
        search_button.pack()

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        category_name = "Books"
        items_list = self.items.get(category_name, [])

        self.cart(items_list)

        sort_button = tk.Button(button_frame, text="Sort by Name", font=('Arial', 50), command=self.sort_books)
        sort_button.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn6 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')


    def Fashion(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", font=('Arial', 20), command=self.search_fashion)
        search_button.pack()

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        category_name = "Fashion"
        items_list = self.items.get(category_name, [])

        self.cart(items_list)

        sort_button = tk.Button(button_frame, text="Sort by Name", font=('Arial', 50), command=self.sort_Fashion)
        sort_button.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn6 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=self.create_home_page)
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')


    def Sports(self):
        self.clear_window()
        label = tk.Label(self.root, text="Welcome to Home App", font=('arial', 20))
        label.pack(padx=20, pady=20)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", font=('Arial', 20), command=self.search_sports)
        search_button.pack()

        button_frame = tk.Frame(self.root)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        category_name = "Sports"
        items_list = self.items.get(category_name, [])

        self.cart(items_list)

        sort_button = tk.Button(button_frame, text="Sort by Name", font=('Arial', 50), command=self.sort_Sports)
        sort_button.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn6 = tk.Button(button_frame,text="Back", font=('Arial', 50),command=self.create_home_page)
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        button_frame.pack(fill='x')



    def run(self):
        self.root.mainloop()

# if __name__ == "__main0__":
app = AlibabaHyperApp()
app.run()

