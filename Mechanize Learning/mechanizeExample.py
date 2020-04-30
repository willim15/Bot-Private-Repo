import re
from mechanize import Browser

br = Browser()
br.open("http://www.example.com/")
# follow second link with element text matching regular expression
response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
assert br.viewing_html()
print br.title()
print response1.geturl()
print response1.info()  # headers
print response1.read()  # body
response1.close()  # (shown for clarity; in fact Browser does this for you)

br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).
br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
response2 = br.submit()  # submit current form

# print currently selected form (don't call .submit() on this, use br.submit())
print br.form

response3 = br.back()  # back to cheese shop (same data as response1)
# the history mechanism returns cached response objects
# we can still use the response, even though we closed it:
response3.seek(0)
response3.read()
response4 = br.reload()  # fetches from server

for form in br.forms():
    print form
# .links() optionally accepts the keyword args of .follow_/.find_link()
for link in br.links(url_regex="python.org"):
    print link
    br.follow_link(link)  # takes EITHER Link instance OR keyword args
    br.back()