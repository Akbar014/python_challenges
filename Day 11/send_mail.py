
import smtplib  # for sending message form server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates import Template
# env varable 
# username = "TestWebApp"
# password = "ujjm riau coqc ejmu"


# TestWebApp
username = 'akbar.cse47@gmail.com'
password = 'ujjm riau coqc ejmu' 

class Emailer():
    subject = "Hello world"
    context={}
    to_emails = []
    has_html = False
    test_send = False
    from_email='Test <akbar.cse47@gmail.com>'
    template_html = None
    template_name = None
    def __init__(self, subject="", template_name=None, context={}, template_html=None, to_emails=None, test_send=False):

        if template_name == None and template_html == None:
            raise Exception ("You must set a template")
        
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject
        self.test_send = test_send

        if template_html !=None:
            self.has_html = True
            self.template_html = template_html
        self.template_name = template_name
        self.context = context

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject

        if self.template_name !=None:
            tmp_str = Template(template_name=self.template_name,context=self.context)
            txt_part = MIMEText(tmp_str.render(),'plain')
            msg.attach(txt_part)
        
        if self.template_html !=None:
            tmp_str = Template(template_name=self.template_html,context=self.context)
            html_part = MIMEText(tmp_str.render(),'html')
            msg.attach(html_part)


        # txt_part = MIMEText(text,'plain')
        # msg.attach(txt_part)

        # if html !=None:
        #     html_part = MIMEText(html,'html')
        #     msg.attach(html_part)
        
        msg_str = msg.as_string()
        return msg_str



    def send_mail(self):
        # assert হল পাইথনে একটি সহজ এবং কার্যকর টুল, যা ডিবাগিং এবং টেস্টিং-এর জন্য ব্যবহৃত হয়। এটি কোডের ভিতরে কোনো শর্ত পূরণ হচ্ছে কিনা তা পরীক্ষা করে এবং সমস্যা থাকলে তা আগে থেকেই ধরে দেয়। তবে প্রোডাকশন পরিবেশে এটি ব্যবহার করা উচিত নয়।
        msg = self.format_msg()

        # login to smtp server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        
        did_send= False
        if not self.test_send:

            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try:
                    server.sendmail(self.from_email,self.to_emails, msg)
                    server.quit()
                    did_send = True
                except:
                    did_send = False
        return did_send
            


# send_mail(to_emails=['aliakbartutul749@gmail.com'])

    

     