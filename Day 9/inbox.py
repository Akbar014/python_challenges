import imaplib # open inbox from server
import email


host = 'imap.gmail.com'
username = 'akbar.cse47@gmail.com'
password = 'ujjm riau coqc ejmu' 

def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    # mail.select("inbox")
    mail.select('[Gmail]/Spam')
    # _, search_data = mail.search(None, 'ALL')
    status, search_data = mail.search(None, 'ALL')
    # status, search_data = mail.search(None, 'ALL')
    # _, search_data = mail.search(None, '(FROM "support@micro1.ai" SUBJECT "Open roles @ top Silicon Valley companies")')
    # if status != 'OK':
    #         print("No emails found!")

    # print(status)       # given output = ok
    # print(search_data)    # given output = [b'1 2 3']
    # print(type(search_data))

    # # print(".......................")

    # print(search_data[0])    # given output = b'1 2 3'
    # print(type(search_data[0]))    # given output = <class 'bytes'>
    # print(search_data[0].split())    # given output = [b'1', b'2', b'3']
    # print(type(search_data[0].split()))    # given output = <class 'list'>
    # data = search_data[0].split()
    # print(data[0])          # given output = b'1'

    my_message = []
    for num in search_data[0].split():
        # print(num)
        email_data ={}
        _, data = mail.fetch(num, 'RFC822')
        # print(_)            # given output = ok
        # print(data)       # given output - mail data
        # print(type(data))
        # print(data[0]) 
        # print(data[1])
        _, b = data[0] 
        # msg_str = str(b)
        # print(msg_str)
        email_msg = email.message_from_bytes(b)
        
        # print(email_msg)
        for header in ['subject', 'to', 'from', 'date']:
            # print("{} : {}".format(header, email_msg[header]))
            email_data['header'] =  email_msg[header]

        for part in email_msg.walk():
            if part.get_content_type() == "text/plain" :
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":

                html_body = part.get_payload(decode=True)
                # print(html_part.decode())
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
        # print(my_message)
    return my_message



#  coding for entrepreneur tutorial code for inbox .........................................

# def get_inbox():
#     mail = imaplib.IMAP4_SSL(host)
#     mail.login(username, password)
#     mail.select("inbox")
#     _, search_data = mail.search(None, 'UNSEEN')
#     my_message = []
#     for num in search_data[0].split():
#         email_data = {}
#         _, data = mail.fetch(num, '(RFC822)')
#         # print(data[0])
#         _, b = data[0]
#         email_message = email.message_from_bytes(b)
#         for header in ['subject', 'to', 'from', 'date']:
#             print("{}: {}".format(header, email_message[header]))
#             email_data[header] = email_message[header]
#         for part in email_message.walk():
#             if part.get_content_type() == "text/plain":
#                 body = part.get_payload(decode=True)
#                 email_data['body'] = body.decode()
#             elif part.get_content_type() == "text/html":
#                 html_body = part.get_payload(decode=True)
#                 email_data['html_body'] = html_body.decode()
#         my_message.append(email_data)
#     return my_message

#  coding for entrepreneur tutorial code for inbox .....................................



# get_inbox()
if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)