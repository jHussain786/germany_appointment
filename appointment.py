
# from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib

url = "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

email_count = 0

while True:
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')  # Converts to BeautifulSoup Object
        select_element = soup.select('select[name="fields[3].content"]')
        options = select_element[0].find_all('option')
        search_text = {"summer","summer semester", "summer semester 2024", "2024"}
        send_email = False
        for option in options:
            for x in search_text:
                if(option.text.find(x) != -1):
                    print("\n-------------------- ",x,"----------------------- \n")
                    send_email = True
        if(send_email != True):
            print("NOT FOUND \n")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("jamillaghari2000@gmail.com", "dmqb xkcd yikn ewtb")
            message = "The appointments for germany are open please go to this website to fill for me \nhttps://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600 \npassport no: KA6919401 telephone: 03485947677"
            s.sendmail("jamillaghari2000@gmail.com", "jamillaghari2000@gmail.com", message)
            sleep(120)
        else:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("jamillaghari2000@gmail.com", "dmqb xkcd yikn ewtb")
            message = "The appointments for germany are open please go to this website to fill for me \nhttps://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600 \npassport no: KA6919401 telephone: 03485947677"
            s.sendmail("jamillaghari2000@gmail.com", "jamillaghari2000@gmail.com", message)
            s.sendmail("jamillaghari2000@gmail.com", "intizarlaghari@gmail.com", message)
            s.sendmail("jamillaghari2000@gmail.com", "Abrarlaghari@hotmail.com", message)
            s.sendmail("jamillaghari2000@gmail.com", "lgharizahra@gmail.com", message)
            s.sendmail("jamillaghari2000@gmail.com", "engr.alamdar@gmail.com", message)
            s.quit()
            email_count += 1
            print("\n-------------------- FOUND ----------------------- \n")
            if email_count > 5:
                break
        sleep(10)
    except:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("jamillaghari2000@gmail.com", "dmqb xkcd yikn ewtb")
        message = "Web is down"
        s.sendmail("jamillaghari2000@gmail.com", "jamillaghari2000@gmail.com", message)
        sleep(10)