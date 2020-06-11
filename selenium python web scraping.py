from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')

#use unique css selector
elem = browser.find_element_by_css_selector('ul:nth-child(20) > li:nth-child(1) > a')
elem.click()

#find by css tag
elems = browser.find_elements_by_css_selector('p')

#fill an input field
browser.get('https://Google.com/')
elem = browser.find_element_by_css_selector('input[name="q"]')
elem.send_keys('hi')
elem.submit()

browser.back()
browser.forward()
browser.refresh()
#browser.quit()

#get entire web page
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body')
print(elem.text)


# take a sscreenshot of the page and save in the current directory
driver.save_screenshot("screenshot.png")
driver.close()








