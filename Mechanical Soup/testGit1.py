from __future__ import print_function
import argparse
import mechanicalsoup
from getpass import getpass
parser = argparse.ArgumentParser(description="Login to GitHub.")
parser.add_argument("username")
args = parser.parse_args()

# failure.
login_page.raise_for_status()
# login_page.soup is a BeautifulSoup object
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup
# we grab the login form
login_form = mechanicalsoup.Form(login_page.soup.select_one('#login form'))
# specify username and password
login_form.input({"login": args.username, "password": args.password})
# submit form
page2 = browser.submit(login_form, login_page.url)
# verify we are now logged in
messages = page2.soup.find("div", class_="flash-messages")
if messages:
print(messages.text)
assert page2.soup.select(".logout-form")
print(page2.soup.title.text)
# verify we remain logged in (thanks to cookies) as we browse the rest of
# the site
page3 = browser.get("https://github.com/MechanicalSoup/MechanicalSoup")
assert page3.soup.select(".logout-form")
