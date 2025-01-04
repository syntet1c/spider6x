from modules import arg_parse
from modules import get_all
import pyfiglet

f = pyfiglet.figlet_format("spider6x", font="slant")
print(f)
print("\tVersion: 1.1\t\tBy syntet1c\n\n\n")

url = arg_parse.arguments_f()["url"]
element = arg_parse.arguments_f()["element"]

if "attribute" in arg_parse.arguments_f().keys():
    attribute = arg_parse.arguments_f()["attribute"]
    data = get_all.extract(url, element, attribute)
else:
    data = get_all.extract(url, element)

for d in data:
    print(d)