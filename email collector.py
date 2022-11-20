#email collector
import re

str = """
full page of blog. the emails are included here that you want to search

"""
emails = re.compile(r'[\w]+[@][\w]+[.][\w][\w][\w]')
# emails = re.compile(r'[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]')
match = emails.findall(str)
for matches in match:
    print(matches)
