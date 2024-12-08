# from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt6 import uic
# import sys

# class Login(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("login.ui", self)
#         self.btnRegister.clicked.connect(self.show_register)
#         self.btnLogin.clicked.connect(self.check_login)
#         self.msg_box = QMessageBox()

#     def check_login(self):
#         email = self.txtEmail.text()
#         password = self.txtPass.text()
#         if email == "admin" and password == "admin":
#             main.show()
#             self.close()
#         else:
#             self.msg_box.setText("Please check your email or password")
#             self.msg_box.exec()

#     def show_register(self):
#         register.show()
#         self.close()

# class Register(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("register.ui", self)
#         self.btnRegister.clicked.connect(self.show_login)
#         self.msg_box = QMessageBox()

#     def show_login(self):
#         login.show()
#         self.close()

# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("main.ui", self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     login = Login()
#     register = Register()
#     main = Main()
#     login.show()
#     app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.btnRegister.clicked.connect(self.show_register)
        self.btnLogin.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPass.text()
        if self.validate_user(email, password):
            main.show()
            self.close()
        else:
            self.msg_box.setText("Invalid email or password")
            self.msg_box.exec()

    def validate_user(self, email, password):
        if not os.path.exists("users.txt"):
            return False
        with open("users.txt", "r") as file:
            for line in file:
                saved_email, saved_password = line.strip().split(",")
                if email == saved_email and password == saved_password:
                    return True
        return False

    def show_register(self):
        register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("register.ui", self)
        self.btnRegister.clicked.connect(self.register_user)
        self.msg_box = QMessageBox()

    def register_user(self):
        email = self.txtEmail.text()
        password = self.txtPass.text()
        if email and password:
            if self.save_user(email, password):
                self.msg_box.setText("Registration successful! Please login.")
                self.msg_box.exec()
                login.show()
                self.close()
            else:
                self.msg_box.setText("User already exists!")
                self.msg_box.exec()
        else:
            self.msg_box.setText("All fields are required!")
            self.msg_box.exec()

    def save_user(self, email, password):
        if not os.path.exists("users.txt"):
            with open("users.txt", "w") as file:
                pass
        with open("users.txt", "r") as file:
            for line in file:
                saved_email, _ = line.strip().split(",")
                if email == saved_email:
                    return False
        with open("users.txt", "a") as file:
            file.write(f"{email},{password}\n")
        return True

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    register = Register()
    main = Main()
    login.show()
    app.exec()
