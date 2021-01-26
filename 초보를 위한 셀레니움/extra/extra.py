from selenium import webdriver

browser = webdriver.Chrome('../chromedriver.exe')

browser.get("https://repl.it/login")

username_input = browser.find_element_by_xpath(
    '/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div/input'
)
password_input = browser.find_element_by_xpath(
    '/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[2]/div/div/div/input'
)
# login_btn = browser.find_element_by_link_text("Log in")
login_btn = browser.find_element_by_partial_link_text("Log")

username_input.send_keys("something")
password_input.send_keys(input("What is your password?"))
login_btn.click()