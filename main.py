import smtplib

my_email = "pagaredevika2002@gmail.com"
password = "********"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="pagare.devika17@yahoo.com" , 
    msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()