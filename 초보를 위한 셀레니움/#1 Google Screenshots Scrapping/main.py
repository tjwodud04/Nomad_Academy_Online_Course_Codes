from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import shutil
import os

class GoogleKeywordScreenshooter:
    def __init__(self, keyword, screenshots_dir):
        self.browser = webdriver.Chrome('../chromedriver.exe')
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        try:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
        except Exception:
            pass

        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        def repetitive(self):
            try:
                shitty_element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
                )
                self.browser.execute_script(
                    """
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty)
                """,
                    shitty_element,
                )
            except Exception:
                pass

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index}.png"
            )
 # ---------------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[3]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index+10}.png"
            )
# ---------------------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[4]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 20}.png"
            )
# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[5]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 30}.png"
            )

# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[6]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 40}.png"
            )

# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[7]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 50}.png"
            )
# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[8]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 60}.png"
            )
# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[9]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 70}.png"
            )
# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[10]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 80}.png"
            )
# ----------------------------------------------------------------------
        next_page_button = self.browser.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[11]/a')
        next_page_button.click()

        repetitive(self)

        search_results = self.browser.find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index + 90}.png"
            )

    def finish(self):
        self.browser.quit()

    def tozipfile(self):
        shutil.make_archive('screentshotresults', 'zip', 'screenshots')
        shutil.rmtree('screenshots/')

domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
domain_competitors.tozipfile()

# python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
# python_competitors.start()
# python_competitors.finish()