from tkinter import *
from tkinter import ttk
import datetime, sys, os
from tkinter import messagebox
from PIL import ImageTk, Image
images_for_return = "images.png"
color = "#F0F0F0"
total_duty = 0
cars = {
    "auto1":  {
    'марка': 'Toyota',
    'номер': 'А 001 АА 116',
    'цвет': 'белый',
    'год выпуска': 2019,
    'модель': 'Toyota Camry',
    'взял': 'Иванов Иван Иванович',
    'дата': '15 апреля 2023 г.',
    'цена проката': 3000
    },
    "auto2": {
        "марка": "BMW",
        "номер": "Е444МО",
        "цвет": "синий",
        "год выпуска": 2020,
        "модель": "5 series",
        "взял": "Андрей Ковальчук Андреевич",
        "дата": "27 мая 2023",
        "цена проката": 3500
    },
    "auto3": {
        "марка": "Mercedes-Benz",
        "номер": "М666АА",
        "цвет": "черный",
        "год выпуска": 2021,
        "модель": "E-Class",
        "взял": "Мария Мачо Мариевна",
        "дата": "2023-04-28",
        "цена проката": 4000,
    },
    "auto4": {
        'марка': 'Ford',
        'номер': 'Е777МР',
        'цвет': 'Синий',
        'год выпуска': 2020,
        'модель': 'Ford Focus',
        'взял': 'Петров Петр Петрович',
        'дата': '12.06.2023',
        'цена проката': 2500
    },
    "auto5": {
        'марка': 'Honda',
        'номер': 'М444ОР',
        'цвет': 'Черный',
        'год выпуска': 2021,
        'модель': 'Honda Civic',
        'взял': 'Сидоров Сидор Сидорович',
        'дата': '23.07.2023',
        'цена проката': 3000
    },
    "auto6": {
        'марка': 'BMW',
        'номер': 'О123КК',
        'цвет': 'Белый',
        'год выпуска': 2022,
        'модель': 'BMW X5',
        'взял': 'Кузнецова Ольга Ивановна',
        'дата': '04.08.2023',
        'цена проката': 3000
    },
    "auto7": {
        'марка': 'Toyota',
        'номер': 'А001ВС',
        'цвет': 'Красный',
        'год выпуска': 2019,
        'модель': 'Toyota Camry',
        'взял': 'Иванов Иван Иванович',
        'дата': '01.05.2023',
        'цена проката': 2000
    },
}


Result_cars = {

}
data = []





class LoginWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Login Window")
        self.master.geometry("570x250")
        self.master.resizable(False, False)
#         # self.master.iconbitmap("@favicon.xbm")
        self.master.config(width=700, height=700, bg="#edf1f7")
        self.create_widgets()

    def create_widgets(self):
        lbl_AUTORENT = Label(text="Автопрокат programm", pady=5, font=("Arial", 20, "bold", "underline"), foreground="red")
        lbl_AUTORENT.grid(row=0, column=1)
        lbl_ENTRY = Label(text="Input your password and login", pady=20, font=("Arial", 15, "bold"))
        lbl_ENTRY.grid(row=1, column=1)

        lbl_login = Label(text="Login: ", pady=5, font=("Arial", 15))
        lbl_login.grid(row=2)
        lbl_password = Label(text="Password: ", font=("Arial", 15))
        lbl_password.grid(row=3)

        self.user_login = Entry(bd=3, width=40)
        self.user_login.grid(row=2, column=1)
        self.user_password = Entry(bd=3, show="*", width=40)
        self.user_password.grid(row=3, column=1)
        self.user_password.bind("<Return>", self.login)

        self.lbl = Label()
        self.lbl.grid(row=4)
        self.btn_login = ttk.Button(text="Login", command=self.login)
        self.btn_login.grid(row=5, column=1, columnspan=1)

        self.btn_quit = ttk.Button(text="Exit", command=self.exit)
        self.btn_quit.grid(row=5, column=0, columnspan=1)

        self.var1 = IntVar()
        self.check_button = Checkbutton(text="Show password", font=("Arial", 12), variable=self.var1, command=self.show_password)
        self.check_button.grid(row=3, column=2, columnspan=1)

        self.btn_save = ttk.Button(text="Save", command=self.save)
        self.btn_save.grid(row=5, column=2)

    def save(self):
        data = {
            "Login": self.user_login.get(),
            "Password": self.user_password.get()
        }
        with open(r"C:\Users\Professional\PycharmProjects\Step\Others/account.txt", "w") as file:
            for i in data.items():
                file.writelines(": ".join(i) + "\n")
                print(i)

    def login(self, event=None):
        login = self.user_login.get()
        password = self.user_password.get()
        if login == "Lego" and password == "12345":
            self.master.withdraw()
            self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
            self.info_window = InitialWindow(self.new_infoWindow)  # Вызов созданного окна
        else:
           messagebox.showinfo(title="Error data", message="Wrong password or login")

    def exit(self):
        self.master.withdraw()

    def show_password(self):
        if self.var1.get() == 1:
            self.user_password['show'] = ""
        else:
            self.user_password['show'] = "*"


class InitialWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("400x500")
        self.master.resizable(False, False)
#         # self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()

    def create_widgets(self):
        self.rent_car = Button(self.master, text="Rent a car", width=10, font=("Arial", 20), background=color, command=self.rent_button)
        self.rent_car.place(x=120, y=100)

        self.history = Button(self.master, text="Look History", width=10, font=("Arial", 20), background=color, command=self.look_history_button)
        self.history.place(x=120, y=170)

        self.information = Button(self.master, text="Information", width=10, font=("Arial", 20), background=color, command=self.information_button)
        self.information.place(x=120, y=240)

        self.Help = Button(self.master, text="Help", width=10, font=("Arial", 20), background=color, command=self.help_button)
        self.Help.place(x=120, y=310)


    def rent_button(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = RentWindow(self.new_infoWindow)  # Вызов созданного окна


    def look_history_button(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = HistoryWindow(self.new_infoWindow)  # Вызов созданного окна


    def information_button(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = InformationWindow(self.new_infoWindow)  # Вызов созданного окна


    def help_button(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = HelpWindow(self.new_infoWindow)  # Вызов созданного окна



class RentWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("1000x800")
        self.master.resizable(False, False)
        # self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()

    def create_widgets(self):
        self.welcom_label = Label(self.master, text="Welcome", width=10, font=("Arial", 30), background=color)
        self.welcom_label.place(x=370, y=50)

        self.find_car = Button(self.master, text="Find car", width=15, pady=10, font=("Arial", 20), background=color, command=self.move_find_car)
        self.find_car.place(x=370, y=200)

        self.add_new_deal = Button(self.master, text="New deal", width=15, pady=10, font=("Arial", 20), background=color, command=self.move_deal)
        self.add_new_deal.place(x=370, y=300)

        self.delete_deal = Button(self.master, text="Delete all deals", width=15, pady=10, font=("Arial", 20), background=color, command=self.move_deleate_deal)
        self.delete_deal.place(x=370, y=400)

        self.duty = Button(self.master, text="Total duty", width=15, pady=10, font=("Arial", 20), background=color, command=self.move_total_duty)
        self.duty.place(x=370, y=500)

        self.show_info = Button(self.master, text="Show info", width=15, pady=10, font=("Arial", 20), background=color, command=self.move_show_info)
        self.show_info.place(x=370, y=600)

        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color, command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)
    # MOVE BUTTONS
    '-----------------------------------------------------------------------------------------'
    def move_find_car(self):
        self.find_car['state'] = DISABLED
        self.find_car.place(x=550, y=200)
        self.add_new_deal.place(x=250, y=300)
        self.delete_deal.place(x=250, y=400)
        self.duty.place(x=250, y=500)
        self.show_info.place(x=250, y=600)

        self.lstbox_option = Listbox(self.master, selectmode=SINGLE, bd=5, width=22, height=6, font=("Arial", 15))
        self.lstbox_option.insert(0, "Поиск по марке")


        self.lstbox_option.insert(1, "Поиск по цвету")
        self.lstbox_option.insert(2, "Поиск по номеру")
        self.lstbox_option.insert(3, "Поиск по году выпуска")
        self.lstbox_option.insert(4, "Поиск по имени")
        self.lstbox_option.insert(5, "Поиск по диапазону цен")
        self.lstbox_option.place(x=550, y=300)
        self.submit_btn = Button(self.master, text="Submit", width=10, pady=5, font=("Arial", 14), background=color, command=self.find_info_option)
        self.submit_btn.place(x=615, y=460)

    def find_info_option(self):
        self.selected_element = self.lstbox_option.curselection()
        if len(self.selected_element) != 0:
            self.submit_btn.place(x=615, y=530)
            self.cancel_btn = Button(self.master, text="Another option", width=12, pady=3, font=("Arial", 8), background=color)
            self.cancel_btn.place(x=630, y=580)
            def ret():
                try:
                    self.find_mark1.destroy()
                    self.find_mark2.destroy()
                    self.ot_label.destroy()
                    self.do_label.destroy()
                    self.submit_btn.place(x=615, y=460)
                    self.find_mark_label.destroy()
                    self.cancel_btn.destroy()
                    self.lstbox_option.destroy()
                    self.submit_btn.destroy()
                    self.find_mark.destroy()
                    self.move_find_car()
                except Exception:
                    self.find_mark.destroy()
                    self.submit_btn.place(x=615, y=460)
                    self.find_mark_label.destroy()
                    self.cancel_btn.destroy()
                    self.lstbox_option.destroy()
                    self.submit_btn.destroy()
                    self.move_find_car()
            self.cancel_btn.config(command=ret)

        try:
            match self.selected_element[0]:
                case 0:
                    self.find_mark_label = Label(self.master, text="Введите марку:", width=20, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=560, y=460)
                    self.find_mark = Entry(self.master, width=20, font=("Arial", 15))
                    self.find_mark.place(x=560, y=495)
                    self.submit_btn.config(command=self.search_mark)
                case 1:
                    self.find_mark_label = Label(self.master, text="Введите цвет:", width=20, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=560, y=460)
                    self.find_mark = Entry(self.master, width=20, font=("Arial", 15))
                    self.find_mark.place(x=560, y=495)
                    self.submit_btn.config(command=self.search_color)
                case 2:
                    self.find_mark_label = Label(self.master, text="Введите номер:", width=20, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=560, y=460)
                    self.find_mark = Entry(self.master, width=20, font=("Arial", 15))
                    self.find_mark.place(x=560, y=495)
                    self.submit_btn.config(command=self.search_number)
                case 3:
                    self.find_mark_label = Label(self.master, text="Введите год выпуска:", width=20, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=560, y=460)
                    self.find_mark = Entry(self.master, width=20, font=("Arial", 15))
                    self.find_mark.place(x=560, y=495)
                    self.submit_btn.config(command=self.search_year)
                case 4:
                    self.find_mark_label = Label(self.master, text="Введите имя:", width=20, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=560, y=460)
                    self.find_mark = Entry(self.master, width=20, font=("Arial", 15))
                    self.find_mark.place(x=560, y=495)
                    self.submit_btn.config(command=self.search_rentator)
                case 5:
                    self.find_mark_label = Label(self.master, text="Введите диапазон:", width=15, pady=3, font=("Arial", 15), background=color)
                    self.find_mark_label.place(x=590, y=460)
                    self.ot_label = Label(self.master, text="От:", width=15, pady=2, font=("Arial", 15), background=color)
                    self.ot_label.place(x=500, y=495)
                    self.do_label = Label(self.master, text="До:", width=15, pady=2, font=("Arial", 15), background=color)
                    self.do_label.place(x=620, y=495)
                    self.find_mark1 = Entry(self.master, width=5, font=("Arial", 15))
                    self.find_mark1.place(x=620, y=495)
                    self.find_mark2 = Entry(self.master, width=5, font=("Arial", 15))
                    self.find_mark2.place(x=730, y=495)
                    self.submit_btn.config(command=self.search_price)
        except IndexError:
             pass

    def search_mark(self):
        self.op = self.find_mark.get()
        for key, auto in cars.items():
            if auto["марка"] == self.op and len(self.op) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()


    def search_color(self):
        self.op = self.find_mark.get()
        for key, auto in cars.items():
            if self.op in auto['цвет'] and len(self.op) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()



    def search_number(self):
        self.op = self.find_mark.get()
        for key, auto in cars.items():
            if self.op in auto['номер'] and len(self.op) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()


    def search_year(self):
        self.op = self.find_mark.get()
        for key, auto in cars.items():
            if self.op in str(auto['год выпуска']) and len(self.op) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()


    def search_rentator(self):
        self.op = self.find_mark.get()
        for key, auto in cars.items():
            if self.op in auto['взял'] and len(self.op) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()


    def search_price(self):
        for key, auto in cars.items():
            if (int(self.find_mark1.get()) < auto['цена проката'] < int(self.find_mark2.get())) and len(self.find_mark1.get()) > 0 and len(self.find_mark2.get()) > 0:
                Result_cars.update({key: auto})
            else:
                print('Not found')
        self.move_new_deal()


    '---------------------------------------------------------------------------'




    def move_deal(self):
        self.move_find_car()


    def move_new_deal(self):
        if self.find_car['state'] == DISABLED:
            # self.master.withdraw()
            # self.new_infoWindow = Toplevel(self.master)
            # self.info_window = RentWindow(self.new_infoWindow)
            self.lstbox_option.destroy()
            self.submit_btn.destroy()
            try:
                self.find_mark1.destroy()
                self.find_mark2.destroy()
                self.ot_label.destroy()
                self.do_label.destroy()
                self.lstbox_option.destroy()
                self.submit_btn.destroy()
                self.find_mark_label.destroy()
                self.cancel_btn.destroy()
            except Exception:
                self.lstbox_option.destroy()
                self.submit_btn.destroy()

            try:
                self.find_mark_label.destroy()
                self.find_mark.destroy()
                self.cancel_btn.destroy()
            except Exception:
                pass


            self.find_car['state'] = ACTIVE
        self.add_new_deal.place(x=550, y=300)
        self.find_car.place(x=250, y=200)
        self.delete_deal.place(x=250, y=400)
        self.duty.place(x=250, y=500)
        self.show_info.place(x=250, y=600)
        self.deal_found_cars()

    def deal_found_cars(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)
        self.info_window = DealCarsWindow(self.new_infoWindow)


    def move_deleate_deal(self):
        global total_duty, data
        total_duty = 0
        data = []
        messagebox.showinfo("Delete", "ВСЕ ДАННЫЕ ВАШИХ ЗАКАЗОВ УСПЕШНО УДАЛЕНЫ")

    def move_total_duty(self):
        global total_duty
        messagebox.showinfo("Duty", f"Your duty: {total_duty}")

    def move_show_info(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)
        self.info_window = ShowInfoWindow(self.new_infoWindow)



    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)

    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] =color
        self.RETURN["text"] = ""

    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = InitialWindow(self.new_infoWindow)  # Вызов созданного окна


class DealCarsWindow(Frame):
    def __init__(self, master=None, item=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("1000x650")
        self.master.resizable(False, False)
#         self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.item = item
        self.create_widgets()

    def create_widgets(self):
        self.list_box_cars_found = Listbox(self.master, selectmode=SINGLE, bd=5, width=52, height=10,
                                           font=("Arial", 20), relief="groove")
        count = 0
        for values in Result_cars.values():
            self.list_box_cars_found.insert(count,
                                            ''.join(str(values.values())).replace('(', '').replace('[', '').replace(
                                                "dict_values", "").replace(',', "; ").replace(']', ";").replace(')', ""))
            count += 1
        self.list_box_cars_found.place(x=120, y=20)
        self.add_btn = Button(self.master, text="ADD", width=12, pady=3, font=("Arial", 15), background=color,
                              command=self.pay)
        self.add_btn.place(x=420, y=370)

        self.scrollbar = Scrollbar(self.master, orient=HORIZONTAL)
        self.scrollbar.pack(side=BOTTOM, fill=X)
        self.list_box_cars_found.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_box_cars_found.xview)

        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color,
                             command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)





    def pay(self):
        global total_duty
        self.option = self.list_box_cars_found.curselection()[0]
        self.duty = self.list_box_cars_found.get(self.option)
        self.res_duty = int(self.duty[-2:-6:-1][-1::-1])
        total_duty += self.res_duty
        data = str(self.list_box_cars_found.get(self.option)).replace('("', "").replace('",', "").replace('")', '')
        self.add_to_history(data)



        self.add_btn.destroy()
        self.card_number = Label(self.master, text="Введите номер карты:", width=20, pady=2, font=("Arial", 15),
                                 background=color)
        self.card_number.place(x=200, y=370)
        self.number_enter = Entry(self.master, width=20, font=("Arial", 15))
        self.number_enter.place(x=200, y=400)
        self.card_number = Label(self.master, text="Введите дату:", width=20, pady=2, font=("Arial", 15),
                                 background=color)
        self.card_number.place(x=550, y=370)
        self.data_enter = Entry(self.master, width=20, font=("Arial", 15))
        self.data_enter.place(x=550, y=400)
        self.card_number = Label(self.master, text="Введите cvc код:", width=20, pady=2, font=("Arial", 15),
                                 background=color)
        self.card_number.place(x=390, y=430)
        self.cvc_enter = Entry(self.master, width=20, font=("Arial", 15))
        self.cvc_enter.place(x=390, y=460)

        self.submit_btn = Button(self.master, text="Sumbit", width=12, pady=3, font=("Arial", 10), background=color,
                                 command=self.active_btn)
        self.submit_btn.place(x=450, y=490)

        self.pay_btn = Button(self.master, text="RENT", width=12, pady=3, font=("Arial", 15), background=color,
                              state=DISABLED)
        self.pay_btn.place(x=430, y=530)

    def active_btn(self):
        if len(self.number_enter.get()) == 16 and (7 <= len(self.data_enter.get()) <= 11) and len(
                self.cvc_enter.get()) == 3:
            self.pay_btn['state'] = ACTIVE
            self.pay_btn.config(command=self.show_disabled)
        else:
            messagebox.showinfo("Ошибка",
                                "Некоректные данные, убедитесь что длина введенных данных соответствует исходнику!")

    def show_disabled(self):
        global total_duty
        self.number_enter["state"] = DISABLED
        self.data_enter["state"] = DISABLED
        self.cvc_enter["state"] = DISABLED
        messagebox.showinfo("Заголовок окна", "Машина арендована | The car has been rented")


    def add_to_history(self, datas=None):
        global data
        data.append(datas)

    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)

    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] = color
        self.RETURN["text"] = ""

    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = RentWindow(self.new_infoWindow)  # Вызов созданного окна


class ShowInfoWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("1300x600")
        self.master.resizable(False, False)
#         self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="Список всех автомобилей", pady=2, font=("Arial", 30),
                                 background=color).place(x=400, y=10)
        placey = 150
        for values in cars.values():
            Label(self.master, text=(''.join(str(values.values())).replace('(', '').replace('[', '').replace("dict_values", "").replace(',', "; ").replace(']', '').replace(')', ';')), pady=2, font=("Arial", 15),
                                 background=color).place(x=150, y=placey)
            placey += 60



        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color,
                             command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)


    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)


    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] = color
        self.RETURN["text"] = ""


    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = RentWindow(self.new_infoWindow)  # Вызов созданного окна




class HistoryWindow(Frame) :#, DealCarsWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("1000x800")
        self.master.resizable(False, False)
#         self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()



    def create_widgets(self):
        global data
        self.history_label = Label(self.master, text="История", width=20, pady=2, font=("Arial", 30, "underline"),
                                 background=color)
        self.history_label.place(x=280, y=10)


        if len(data) == 0:
            Label(self.master, text="История пуста!", pady=2, font=("Arial", 40), foreground="red", background=color).place(x=320, y=400)
        else:
            self.data_lst_box = Listbox(self.master, selectmode=SINGLE, bd=5, width=70, height=15, font=("Arial", 15))
            for item in range(len(data)):
                self.data_lst_box.insert(item, f"{datetime.datetime.now()}:  {data[item]}")

            self.data_lst_box.place(x=130, y=200)
            self.scrollbar = Scrollbar(self.master, orient=HORIZONTAL)
            self.scrollbar.pack(side=BOTTOM, fill=X)
            self.data_lst_box.config(xscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=self.data_lst_box.xview)






        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color,
                             command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)

    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)

    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] = color
        self.RETURN["text"] = ""

    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = InitialWindow(self.new_infoWindow)  # Вызов созданного окна




class InformationWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("1400x660")
        self.master.resizable(False, False)
#         self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()

    def create_widgets(self):
        info_name_label = Label(self.master, text="О ПРИЛОЖЕНИИ", font=("Arial", 30), background=color)
        info_name_label.place(x=500, y=10)
        info_label = Label(self.master, text="Данное приложение предоставляет возможность аренды автомобилей в режиме онлайн. В данном приложении представлен широкий выбор автомобилей от эконом до премиум-класса,\n а также различные варианты аренды - от нескольких часов до нескольких недель. Пользователь может выбрать необходимый автомобиль, указать дату и время аренды. В приложении доступна возможность оплаты аренды онлайн с помощью банковской карты. Кроме того, приложение предоставляет подробную информацию об условиях аренды, страховке и дополнительных услугах.".replace('. ', ".\n"), font=("Arial", 15), background=color)
        info_label.place(x=100, y=70)
        info_name_rent_terms = Label(self.master, text="Условия аренды, аренды, страховки и дополнительных услугах", font=("Arial", 30), background=color)
        info_name_rent_terms.place(x=120, y=250)
        info_rent_terms = Label(self.master, text="Условия аренды автомобиля могут немного отличаться в зависимости от компании, которая предоставляет услуги аренды. Обычно, чтобы арендовать автомобиль, необходимо иметь водительские права и кредитную карту. Кроме того, возможно требование возраста водителя не моложе 21 или 25 лет. Страховка часто является обязательным условием аренды. Обычно есть два вида страховки - базовая и дополнительная. Базовая страховка обычно покрывает основные риски, такие как ущерб автомобиля и страховую ответственность. Дополнительная страховка может включать в себя дополнительные опции,\n такие как защита от угона, защита от повреждений шин, стекол и кузова автомобиля. Среди дополнительных услуг, которые могут предоставляться при аренде автомобиля, могут быть:\n навигационная система, автомобильное кресло для ребенка, дополнительный водитель, доставка автомобиля и др. Каждая компания имеет свой перечень дополнительных услуг, и стоимость их может варьироваться. Также стоит учитывать, что условия аренды автомобиля могут меняться в зависимости от страны, в которой вы арендуете автомобиль. Например, в некоторых странах может быть обязательным наличие международного водительского удостоверения. Поэтому перед арендой автомобиля необходимо тщательно ознакомиться с условиями аренды и дополнительными услугами,\n чтобы избежать неприятных сюрпризов.".replace('. ', ".\n"), font=("Arial", 15), background=color)
        info_rent_terms.place(x=100, y=300)
        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color, command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)


    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)

    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] =color
        self.RETURN["text"] = ""

    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = InitialWindow(self.new_infoWindow)  # Вызов созданного окна


class HelpWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Main window")
        self.master.geometry("470x400")
        self.master.resizable(False, False)
#         self.master.iconbitmap(default=photo)
        self.master.config(width=700, height=700, bg=color)
        self.create_widgets()

    def create_widgets(self):
        help_name_label = Label(self.master, text="ТЕХ-ПОДДЕРЖКА", font=("Arial", 20), background=color)
        help_name_label.place(x=130, y=10)
        help_label_email = Label(self.master, text="emails:", font=("Arial", 15), background=color)
        help_label_email.place(x=140, y=70)
        help_email = Label(self.master, text="support1@mail.com", font=("Arial", 10), background=color)
        help_email.place(x=110, y=100)
        help_email = Label(self.master, text="support2@mail.com", font=("Arial", 10), background=color)
        help_email.place(x=110, y=130)

        help_label_email = Label(self.master, text="contacts:", font=("Arial", 15), background=color)
        help_label_email.place(x=300, y=70)
        help_email = Label(self.master, text="+89012222222", font=("Arial", 10), background=color)
        help_email.place(x=300, y=110)
        help_email = Label(self.master, text="+89012222222", font=("Arial", 10), background=color)
        help_email.place(x=300, y=150)
        help_email = Label(self.master, text="+89012222222", font=("Arial", 10), background=color)
        help_email.place(x=300, y=190)
        help_email = Label(self.master, text="+89012222222", font=("Arial", 10), background=color)
        help_email.place(x=300, y=230)

        help_web = Label(self.master, text="Наши соцсети:", font=("Arial", 15), background=color)
        help_web.place(x=180, y=280)
        self.image_vk = Image.open("./VK.png")
        self.image_vk = self.image_vk.resize((40, 40))
        self.img_vk = ImageTk.PhotoImage(self.image_vk)
        vk_image = Label(self.master, image=self.img_vk, background=color)
        vk_image.place(x=180, y=320)
        self.image_ok = Image.open("images/OK.png")
        self.image_ok = self.image_ok.resize((40, 40))
        self.img_ok = ImageTk.PhotoImage(self.image_ok)
        label_vk_link = Label(self.master, text="https://vk.com/", font=("Arial", 10), background=color)
        label_vk_link.place(x=160, y=360)
        ok_image = Label(self.master, image=self.img_ok, background=color)
        ok_image.place(x=280,y=320)
        label_ok_link = Label(self.master, text="https://ok.ru/", font=("Arial", 10), background=color)
        label_ok_link.place(x=260, y=360)

        self.image = Image.open(images_for_return)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)
        self.RETURN = Button(self.master, text="", image="", width=5, height=800, background=color, command=self.return_)
        self.RETURN.bind('<Enter>', self.Return_in)
        self.RETURN.bind('<Leave>', self.Return_out)
        self.RETURN.pack(side=LEFT)


    def Return_in(self, event=None):
        self.RETURN["image"] = self.img
        self.RETURN["width"] = 100
        self.RETURN["background"] = "#fff"
        self.RETURN["text"] = "Return"
        self.RETURN["font"] = ("Arial", 20)

    def Return_out(self, event=None):
        self.RETURN["image"] = ""
        self.RETURN["width"] = 2
        self.RETURN["background"] =color
        self.RETURN["text"] = ""

    def return_(self):
        self.master.withdraw()
        self.new_infoWindow = Toplevel(self.master)  # Создание нового окна
        self.info_window = InitialWindow(self.new_infoWindow)  # Вызов созданного окна





if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    app.mainloop()
