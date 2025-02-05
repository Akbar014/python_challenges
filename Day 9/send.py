
import requests
import sys
from formatting import format_msg
from datetime import datetime

from send_mail import send_mail
# def send(name, website):
#     msg = format_msg(my_name=name, my_website=website)
#     # send the message
#     return msg

def send(name, website=None, to_email=None ,verbose=False):
    if website != None:
        msg = format_msg(my_name=name,my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:   # verbose refers to a mode or setting that provides detailed output or feedback during the execution of a program. 
        print(name,website) # Verbose mode can be used in logging to show detailed information about the program's operations.

    # send the message
    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
    
    return sent

    
    # r = requests.get("http://httpbin.org/json")
    # if r.status_code == 200:
    #     return r.json()
    # else:
    #     return "There was an error."
    
    # return msg

if __name__ == "__main__":
    print(sys.argv)
    name= "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]

    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]

    response = send(name,to_email=email, verbose=True)
    
    print(response)




