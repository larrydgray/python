from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://web.archive.org/web/20150906082429/http://brinkoffreedom.net/outdoor-activities/trapping-for-winter-survival-or-all-around-for-food-fur-and-fun-part-2/')
#in_put = browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
#button = browser.find_element_by_xpath('//*[@id="su"]').click()
page = browser.page_source
#print(page)
with open('trapping1-3.html', 'w') as f:
    f.write(page)

