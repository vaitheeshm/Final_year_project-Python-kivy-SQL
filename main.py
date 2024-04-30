from kivymd.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDRaisedButton,MDIconButton
from kivy.core.window import Window
from kivy.properties import BooleanProperty,ObjectProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import ScreenManager,FadeTransition,SlideTransition
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget ,CheckboxLeftWidget
from kivymd.uix.snackbar import Snackbar
from pyzbar.pyzbar import ZBarSymbol
import mysql.connector as DB
import random
from functools import partial

###################################### DATABASE  ######################################

# ('John Doe', '1234567890', 'Male'),
# ('Jane Smith', '9876543210', 'Female'),
# ('Alice Johnson', '4561237890', 'Female'),
# ('Bob Brown', '7894561230', 'Male'),
# ('Emily Davis', '6549873210', 'Female'),
# ('Michael Wilson', '3217896540', 'Male'),
# ('Emma Martinez', '9873214560', 'Female'),
# ('William Taylor', '4567891230', 'Male'),
# ('Olivia Anderson', '6541239870', 'Female'),
# ('James Thompson', '3214567890', 'Male'),
# ('Sophia White', '7893216540', 'Female'),
# ('Benjamin Clark', '1237894560', 'Male'),
# ('Isabella Hall', '4566541230', 'Female'),
# ('Jacob Rodriguez', '7899873210', 'Male'),
# ('Mia Lee', '1236547890', 'Female'),
# ('Ethan Walker', '9877896540', 'Male'),
# ('Ava Perez', '4563219870', 'Female'),
# ('Alexander Green', '7896541230', 'Male'),
# ('Charlotte King', '1239874560', 'Female'),
# ('Liam Harris', '6543217890', 'Male');

#####################################################################################

try:
    mydb = DB.connect(
        host="localhost",
        user="root",
        password="Isvaitro14",
        database="myapp"
    )
    print("Connected successfully!")
except DB.Error as err:
    print(f"Error: {err}")

cursor_obj = mydb.cursor()

cursor_obj.execute("Select * from contacts")

result = cursor_obj.fetchall()

class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        # Add your custom widgets and logic specific to Screen 2 here


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        # Add your custom widgets and logic specific to Screen 2 here


class QuickPay(MDApp):
    bottom_sheet_visible = BooleanProperty(False)
    amount_field = ObjectProperty(None)

    def build(self):
        Window.size = (360, 640)
        self.theme_cls.primary_palette = "Orange"
        # LabelBase.register(name="font", fn_regular="static/Platypi-Bold.ttf")
        self.theme_cls.font_styles["Platypi-Bold"] = ["Platypi-Bold",16,False,0.15,]
        return Builder.load_file("App.kv")

    def Main_page(self):
        self.screen_manager = self.root.ids.manager
        self.screen_manager.transition = SlideTransition(direction='left')
        self.root.ids.manager.current = 'Main_page'

    def feedback(self):
        self.root.ids.manager.current = 'feedback'
        # feedback = self.root.ids.feedback_input.text
        # print("Feedback submitted:", feedback)

    def password(self):
        self.root.ids.manager.current ="password"

    def sk(self):
        self.root.ids.manager.current = 'select_contact'
        self.contacts=self.root.ids.contacts

        for i in result:
            # random_choice = random.randint(0, 2)

            string1 = "image2.png"
            string2 = "image3.png"

            # Pick the corresponding string
            gender = "image2.png" if i[3] == "Female" else "image3.png"
            # else:
            #     gender=string3
            self.gen_list=TwoLineAvatarListItem(ImageLeftWidget(
                source=gender,radius=75),
                text=f"{i[1]}",secondary_text= f"{i[2]}",
                )
            # Bind on_release event using partial to pass arguments
            self.gen_list.bind(on_release=partial(self.jump_to_payment_page, i[1], i[2]))
            self.root.ids.contacts.add_widget(self.gen_list)
    
    def jump_to_payment_page(self,instance1,instance2,instance):
        self.root.ids.manager.current = 'gateway'
        self.root.ids.payee_name.text = instance1
        self.root.ids.payee_number.text = instance2


    def on_symbols(self, instance, symbols):
        if symbols:  # Check if symbols is not empty
            for symbol in symbols:
                try:
                    decoded_data = symbol.data.decode()
                    print("Your QR code is:", decoded_data)
                    # Snackbar(
                    #     # secondary_text="Your QR code ID:",   #{}".format(decoded_data),#
                    #     md_bg_color="green",
                    #     # font_size=25
                    # ).open()
                    self.root.ids.manager.current = 'gateway'
                except UnicodeDecodeError:
                    print("Error decoding QR code data. Might not be text-based.")

    def QR(self):
        self.root.ids.manager.current = 'qr'

    def Savings(self):
        self.root.ids.manager.current = 'savings'

    def bitcoin (self):
        self.root.ids.manager.current = 'wallet'

    def bills(self):
        self.root.ids.manager.current = 'bills'

    def open_settings(self):
        self.root.ids.manager.current = 'settings'

    def bank_transfer(self):
        self.root.ids.manager.current = 'bank_transfer'

    def open_help(self):
        self.root.ids.manager.current = 'help'

    def password(self):
        self.root.ids.manager.current = 'password'
        self.root.ids.amount_field.text = ""
        self.root.ids.text_field.text = ""
        self.root.ids.note_text.text = ""
        self.close_bottom_sheet()

    def cibil(self):
        self.root.ids.manager.current = 'CIBIL'

    def t_history(self):
        self.root.ids.manager.current = 't_history'
    
    def b_b(self):
        self.root.ids.manager.current = 'b_b'

    def recharge(self):
        self.root.ids.manager.current = 'recharge'
    
    def payment_successful(self):
        self.amt_text = self.root.ids.text_field.text.strip()
        if self.amt_text == "password":
            self.root.ids.manager.current = 'success'
            self.label=self.root.ids.thumbsup
            anim = Animation(font_size=80, duration=1.2) + Animation( font_size=140, duration=1.2)
            anim.repeat = True
                
            anim.start(self.label)
    
    def darkmode(self):
        self.theme_cls.theme_style="Dark"

    def lightmode(self):
        self.theme_cls.theme_style="Light"

    def toggle_bottom_sheet_visibility(self):
        entered_amount = self.root.ids.amount_field.text.strip()  # Retrieve the text from the MDTextField and remove leading/trailing spaces
        if entered_amount:  # Check if entered_amount is not empty
            bottom_sheet = self.root.ids.bottom_sheet
            arrow_button = self.root.ids.arrow_button
            if not self.bottom_sheet_visible:
                Animation(y=0, d=0.3).start(bottom_sheet)

            else:
                Animation(y=-dp(200), d=0.3).start(bottom_sheet)

            self.bottom_sheet_visible = not self.bottom_sheet_visible
            self.root.ids.pay.text = f"[b] Pay ₹ {entered_amount} [/b]"  # Update the text of the "Pay ₹" button
        else:
            self.bottom_sheet_visible = False

    def close_bottom_sheet(self):
        bottom_sheet = self.root.ids.bottom_sheet
        arrow_button = self.root.ids.arrow_button
        Animation(y=-dp(200), d=0.3).start(bottom_sheet)
        # arrow_button.icon = "arrow-right"
        self.bottom_sheet_visible = False

QuickPay().run()

