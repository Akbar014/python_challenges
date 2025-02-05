
import smtplib  # for sending message form server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# env varable 
# username = "TestWebApp"
# password = "ujjm riau coqc ejmu"


# TestWebApp
username = 'akbar.cse47@gmail.com'
password = 'ujjm riau coqc ejmu' 

def send_mail(text='Emsil Body', subject='Hello world', from_email='Test <akbar.cse47@gmail.com>', to_emails=None, html=None):
    # assert হল পাইথনে একটি সহজ এবং কার্যকর টুল, যা ডিবাগিং এবং টেস্টিং-এর জন্য ব্যবহৃত হয়। এটি কোডের ভিতরে কোনো শর্ত পূরণ হচ্ছে কিনা তা পরীক্ষা করে এবং সমস্যা থাকলে তা আগে থেকেই ধরে দেয়। তবে প্রোডাকশন পরিবেশে এটি ব্যবহার করা উচিত নয়।
    assert(isinstance(to_emails, list))
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['subject'] = subject
    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    if html !=None:
        html_part = MIMEText(html,'html')
        msg.attach(html_part)
    
    msg_str = msg.as_string()

    # login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email,to_emails, msg_str)
    server.quit()


# send_mail(to_emails=['aliakbartutul749@gmail.com'])

    

     