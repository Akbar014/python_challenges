msg_template = """Hello {name}. Thank your for joining {website} .
We are very happy to have you with us """


# def format_msg(my_name, my_website):
#     msg = msg_template.format(name = my_name, website=my_website)
#     return msg

def format_msg(my_name, my_website='default website name'):
    msg = msg_template.format(name = my_name, website=my_website)
    return msg

