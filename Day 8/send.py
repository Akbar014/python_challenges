
import requests
import sys
from formatting import format_msg
from datetime import datetime
# def send(name, website):
#     msg = format_msg(my_name=name, my_website=website)
#     # send the message
#     return msg

def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name,my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name,website)
    # send the message
    
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error."
    
    # return msg

if __name__ == "__main__":
    print(sys.argv)
    name= "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name,verbose=True)
    print(response)




