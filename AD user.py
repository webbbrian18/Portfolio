import pyad
import tkinter as tk
from tkinter import ttk

def create_user():
    pyad.set_ldap_connection("YOUR DOMAIN")
    first_name = first_entry.get()
    last_name = last_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    ou = ou_entry.get()
    
    new_user = pyad.aduser.ADUser.create(username, password=password)
    new_user.update_attribute("givenName", first_name)
    new_user.update_attribute("sn", last_name)
    new_user.update_attribute("mail", email)
    
    ou_container = pyad.adcontainer.ADContainer.from_dn("OU=" + ou + ",DC=DOMAIN,DC=DOMAIN")
    new_user.move(ou_container)
    
    result_label.config(text="User created successfully.")

# Create the main window and form widgets
window = tk.Tk()
window.geometry("400x300")
window.title("Create AD User")

first_label = ttk.Label(window, text="First Name:")
first_label.pack()
first_entry = ttk.Entry(window)
first_entry.pack()

last_label = ttk.Label(window, text="Last Name:")
last_label.pack()
last_entry = ttk.Entry(window)
last_entry.pack()

email_label = ttk.Label(window, text="Email Address:")
email_label.pack()
email_entry = ttk.Entry(window)
email_entry.pack()

username_label = ttk.Label(window, text="Username:")
username_label.pack()
username_entry = ttk.Entry(window)
username_entry.pack()

password_label = ttk.Label(window, text="Password:")
password_label.pack()
password_entry = ttk.Entry(window, show="*")
password_entry.pack()

ou_label = ttk.Label(window, text="Organizational Unit:")
ou_label.pack()
ou_entry = ttk.Entry(window)
ou_entry.pack()

create_button = ttk.Button(window, text="Create User", command=create_user)
create_button.pack()

result_label = ttk.Label(window)
result_label.pack()

# Start the main event loop
window.mainloop()
