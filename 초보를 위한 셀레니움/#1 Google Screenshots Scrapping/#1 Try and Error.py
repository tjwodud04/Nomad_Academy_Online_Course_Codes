from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

KEYWORD = "buy domain"

browser = webdriver.Chrome(r'../chromedriver.exe')

browser.get('https://www.google.com/')

search_bar = browser.find_element_by_class_name('gLFyf')

# search_bar.send_keys("hello!")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)
'''
g kno-kp mnr-c g-blk
'''

# for index, search_result in enumerate(search_results):
#     class_name = search_result.get_attribute("class")
#     print(class_name)

# for search_result in search_results:
#     title = search_result.find_element_by_tag_name("h3")
#     if title:
#         print(title.text)
#     elif title is None:
#         pass
'''
이미지
Hello (아델의 노래) - 위키백과, 우리 모두의 백과사전
Hello (Adele song) - Wikipedia
Hello(싱글) - 나무위키
“HELLO!!” - 나무위키
HELLO
헬로네이처 - 오늘이 맛있는 탐험
'''

# shitty_element = browser.find_element_by_class_name("g kno-kp mnr-c g-blk")

shitty_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

# print(shitty_element)

# for index, search_result in enumerate(search_results):
#     class_name = search_result.get_attribute("class")
#     # print(class_name)
#     if "liYKde g" not in class_name:
#         search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.execute_script(
    """
    const shitty = arguments[0];
    shitty.parentElement.removeChild(shitty)
    """,
    shitty_element,
)

search_results = browser.find_elements_by_class_name("g")

# for index, search_result in enumerate(search_results):
#             search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
#
#         try:
#             next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[3]/a')
#             next_page_button.click()
#
#             for index, search_result in enumerate(search_results):
#                 search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
#
#         except Exception:
#             pass

for index, search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.quit()

# try:
#             shitty_element = WebDriverWait(self.browser, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))
#             self.browser.execute_script(
#                 """
#                 const shitty = arguments[0];
#                 shitty.parentElement.removeChild(shitty)
#                 """,
#                 shitty_element,
#             )
#         except Exception:
#             pass
#
#         search_results = self.browser.find_elements_by_class_name("g")
#
#         try:
#             if not os.path.exists('screenshots'):
#                 os.makedirs('screenshots')
#         except Exception:
#             pass