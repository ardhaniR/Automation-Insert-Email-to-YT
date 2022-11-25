import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import ctypes  # An included library with Python install.
from time import sleep

from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import ttk
# from tkinter.messagebox import showinfo

def Mbox(title, text, style):
    ##  Styles:
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox
    
    # Styles can be combined as follow
    # 0x00000004L --> OK NO button
    # 0x00004000L --> Always on TOP
    # 0x00040004L --> OK NO button & Always on TOP

    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Define a function to return the Input data
def display_data(emails):
    print(emails)
    label_output.config(text= emails, font= ('Helvetica 8'))

def insert_emails_to_YT():
    emails = entry_emails_subs.get().splitlines()
    # # Web Automation Started here --------------------------------------
    # PATH = 'C:\Program Files (x86)\chromedriver.exe'
    # driver = webdriver.Chrome(PATH)
    driver = uc.Chrome(use_subprocess=True)
    # driver = uc.Chrome()
    wait = WebDriverWait(driver,60)
    
    # URL = "https://studio.youtube.com/video/YcCRxfHbiS8/edit"
    driver.get(entry_YT_Link.get())

    # wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys('thefineardh@gmail.com')
    wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(entry_email_login.get())
    MboxResult = Mbox('Konfirmasi Login', 'Apakah Login Sudah Selesai ?', 0x00040004)
    print('MboxResult : ',MboxResult)
    if MboxResult == 6: #IDOK
        display_data(emails)
        # 2 | runScript | window.scrollTo(0,0) | 
        driver.execute_script("window.scrollTo(0,0)")
        # 3 | click | css=#select-button > .remove-defaults | 
        driver.find_element(By.CSS_SELECTOR, "#select-button > .remove-defaults").click()
        # 4 | click | css=#private-radio-button > #radioLabel | 
        driver.find_element(By.CSS_SELECTOR, "#private-radio-button > #radioLabel").click()
        # 5 | click | css=.private-share-edit-button > .label | 
        driver.find_element(By.CSS_SELECTOR, ".private-share-edit-button > .label").click()
        # 6 | sendKeys | id=text-input | alamat email + ${KEY_ENTER}
        for email in emails:
            driver.find_element(By.ID, "text-input").send_keys(email, Keys.ENTER)
        # 9 | click | css=#done-button > .label | 
        # driver.find_element(By.CSS_SELECTOR, "#done-button > .label").click()

        # sleep(99999)
    elif MboxResult == 7: #IDOK
        no_message = 'No button Pressed -- Please fill the input again'
        print (no_message)
        display_data(no_message)
        driver.close()
        pass

    # return MboxResult

# email = 'thefineardh@gmail.com\n'
#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("600x250")
win.title('Emails insert to YT Channel')

# Create label & entry widget for YT Studio account
label_email_login= Label(win, text="Masukkan Alamat Akun Email YT Studio", font=('Helvetica 10'))
label_email_login.place(relx= .5, rely= .1, anchor= CENTER)
entry_email_login = Entry(win, width= 42)
entry_email_login.place(relx= .5, rely= .2, anchor= CENTER)
# default fill of entry widget
# entry_email_login.insert(END, '********.com')

# Create label & entry widget for YT Studio link that we will add the private list
label_YT_Link= Label(win, text="Masukkan Alamat YT Studio edit Video", font=('Helvetica 10'))
label_YT_Link.place(relx= .5, rely= .3, anchor= CENTER)
entry_YT_Link = Entry(win, width= 42)
entry_YT_Link.place(relx= .5, rely= .4, anchor= CENTER)
# default fill of entry widget
# entry_YT_Link.insert(END, 'https://studio.youtube.com/video/*********/edit')

# Create label & entry widget for subcriber emails (copy paste from gsheet or excel)
label_emails_subs= Label(win, text="Masukkan Alamat Email Subscriber", font=('Helvetica 10'))
label_emails_subs.place(relx= .5, rely= .5, anchor= CENTER)
entry_emails_subs = Entry(win, width= 42)
entry_emails_subs.place(relx= .5, rely= .6, anchor= CENTER)
# default fill of entry widget
# entry_emails_subs.insert(END, '******.com\n********.com\n')

# Create button for submit and run the function
ttk.Button(win, text= "Submit", command= insert_emails_to_YT).place(relx= .5, rely= .7,anchor= CENTER)

# display output emails inputted
label_output= Label(win, text="", font=('Helvetica 13'))
label_output.place(relx= .5, rely= .8, anchor= CENTER)

win.mainloop()