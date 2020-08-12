
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


# Returns file name in the formate of 
# key1 key2 - datetime.html
def get_file_name(key1, key2):
    return  ("{} {} - {}.html".format(key1, key2, datetime.now())).replace(":","")

# Generates summary in form of html page
def generate_html_page(data):
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    f = open(get_file_name(data['key1'], data['key2']) ,'w+')

    f.write(template.render(data=data))
    f.close()
    
