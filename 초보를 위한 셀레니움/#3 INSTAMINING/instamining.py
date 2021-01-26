import csv
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# main_hashtag = "dog"
max_hashtags = 15
initial_hashtag = "dog"
browser = webdriver.Chrome('../chromedriver.exe')
counted_hashtags = []
used_hashtags = []

def wait_for(locator):
    return WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))

# browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

# header = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "header"))
# )

# header = wait_for((By.TAG_NAME, "header"))
#
# hashtags = header.find_elements_by_class_name("AC7dP")
#
# for hashtag in hashtags:
#     # hashtag.click()
#     ActionChains(browser).key_down(Keys.COMMAND).click(hashtag).perform()
#
# counted_hashtags = []
# used_hashtags = []

# for window in browser.window_handles:
#     browser.switch_to.window(window)
    # hashtag_name = browser.find_element_by_tag_name("h1")
    # print(hashtag_name.text[1:])
def clean_hashtag(hashtag):
    return hashtag[1:]

def extract_data():
    hashtag_name = wait_for((By.TAG_NAME, "h1"))
    post_count = wait_for((By.CLASS_NAME, "g47SY"))
    if post_count:
        post_count = int(post_count.text.replace(",", ""))
    if hashtag_name:
        # hashtag_name = hashtag_name.text[1:]
        hashtag_name = clean_hashtag(hashtag_name.text)
    if hashtag_name and post_count:
        if hashtag_name not in used_hashtags:
            counted_hashtags.append((hashtag_name, post_count))
            used_hashtags.append(hashtag_name)

# for window in browser.window_handles[0:-1]:
#     browser.switch_to.window(window)
#     browser.close()

def get_related(target_url):
    browser.get(target_url)
    header = wait_for((By.TAG_NAME, "header"))
    hashtags = header.find_elements_by_class_name("AC7dP")
    for hashtag in hashtags:
        # ActionChains(browser).key_down(Keys.COMMAND).click(hashtag).perform()
        hashtag_name = clean_hashtag(hashtag.text)
        if hashtag_name not in used_hashtags:
            ActionChains(browser).key_down(Keys.COMMAND).click(hashtag).perform()

    for window in browser.window_handles:
        browser.switch_to.window(window)
        extract_data()
        time.sleep(1)

    if len(used_hashtags) < max_hashtags:
        for window in browser.window_handles[0:-1]:
            browser.switch_to.window(window)
            browser.close()
        browser.switch_to.window(browser.window_handles[0])
        get_related(browser.current_url)

# time.sleep(3)
# browser.quit()

get_related(f"https://www.instagram.com/explore/tags/{initial_hashtag}")
# print(counted_hashtags)

file = open(f"{initial_hashtag}-report.csv", "w")
writer = csv.writer(file)
writer.writerow(["Hashtag", "Post Count"])

for hashtag in counted_hashtags:
    writer.writerow(hashtag)

browser.quit()