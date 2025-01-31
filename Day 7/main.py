

def my_print(txt):
    print(txt)

# my_print("abc")

# msg_template = """Hello {name}. Thank your for joining {website} . 
# We are very happy to have you with us """.formmat(name="some", website="xyz.com")

msg_template = """Hello {name}. Thank your for joining {website} .
We are very happy to have you with us """


# def format_msg(my_name="akbar", my_website="xyz.com"):
#     my_msg = msg_template.format(name=my_name, website=my_website)
#     # print(my_msg)
#     return my_msg

    
def format_msg(my_name, my_website=None):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg

names = ['a', 'b', 'c']
for name in names:
    this_person_msg = format_msg(name)
    print(this_person_msg )


# format_msg()