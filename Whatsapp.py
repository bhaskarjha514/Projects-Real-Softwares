from selenium import webdriver 
driver = webdriver.Chrome(executable_path='C:/Users/bhask/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of person or group: ")
msg = input("Enter the msg here: ")

count = int(input('Enter the count'))
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')
for i in range (count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    
