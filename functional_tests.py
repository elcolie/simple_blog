from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000/posts')
assert 'Django' in browser.title
browser.quit()