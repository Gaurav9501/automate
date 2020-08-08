import smtplib

gmail_user = 'gauravagarwal9501@gmail.com'
gmail_password = 'activa9501'
message =  input("Enter your name")
gmail_user_To = input("Enter To send mail")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send()
    server.sendmail(gmail_user, gmail_user_To, message)
    server.quit()

except:
    print ('Something went wrong...')
