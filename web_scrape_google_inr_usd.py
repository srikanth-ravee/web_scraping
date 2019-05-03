from selenium import webdriver
from datetime import datetime
import time
import csv
import smtplib
#Credentials
#Store your gmail login and password in
import secred


try:
    browser = webdriver.Chrome("C:/Program Files (x86)/chromedriver_win32/chromedriver.exe")
    web_url = 'https://www.google.com/search?q=usd+to+inr'
    browser.get(web_url)
    time.sleep(3)

    cur_input = browser.find_element_by_xpath('//input[@id="knowledge-currency__src-input"]')
    cur_output = browser.find_element_by_xpath('//input[@id="knowledge-currency__tgt-input"]')

    input_value = cur_input.get_attribute("value")

    output_value = cur_output.get_attribute("value")

    time.sleep(2)

    browser.quit()
    date = datetime.today()
    #print(date)
    temp_list = [output_value, input_value, date]
    with open('inr_usd.csv', 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(temp_list)
except Exception:
    print("process failed")

gmail_user = secred.gmail_user
gmail_password = secred.gmail_password
sent_from = gmail_user
to = ['rite2ravee@gmail.com']#, 'surveabhishek22@gmail.com']
subject = 'USD to INR Update'
body = "INR: {} for {} USD".format(output_value, input_value)

email_text = """\
From: %s
To: %s
Subject: %s


%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email Sent!')
except:
    print('Something went wrong while sending email...')






