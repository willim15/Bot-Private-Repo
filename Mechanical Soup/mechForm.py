import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open('http://ajmal.pythonanaywhere.com')
browser.select_form()




browser.get_current_form().print_summary() # get_current_form() returns the form object pointing to the currently selected form
browser['name'] = 'morgan'

browser['age'] = 21

browser['gender'] = '1' 

browser['about_me'] = 'I am learning MechanicalSoup'