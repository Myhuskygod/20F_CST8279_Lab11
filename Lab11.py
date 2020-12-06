import base64, import sqlite3, import webbrowser
Number = input("Please enter a number(1-24) or Q(exit)：")
flag = True
while flag:
    if Number.isnumeric() and Number = int(n):
        if Number > 0 and Number < 25:
            flag = False
        else: 
            Number = input("The number that you entered is not accepted, please try again or exit")
    else:
        if Number == "Q":
            exit()
        else:
            Number = input("The number that you entered is not accepted, please try again or exit")
conn = sqlite3.connect('week11.db')
c = conn.cursor()
c.execute('select Link from Lab10 where id=%d'% Number)
link = str(c.fetchone()[0])
print(link)
base64_message = link
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
webbrowser.open_new(message)
City_name = input("Please enter the city name: ")
Country_name = input("Please enter the country name: ")
c.execute('Update Lab10 SET City ="%s", Country ="%s" WHERE ID = %s'% (City_name, Country_name, Number))
conn.commit()
c.close()
conn.close()
print('Update finished')
