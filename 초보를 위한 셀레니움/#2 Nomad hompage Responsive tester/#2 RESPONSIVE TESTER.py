from math import ceil
import time
from selenium import webdriver

class ResponsiveTester:
    def __init__(self, url):
        self.browser = webdriver.Chrome('../chromedriver.exe')
        self.browser.maximize_window()
        self.url = url
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1027
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0, 0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight"
            )
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(
                    f"window.scrollTo(0, {section * BROWSER_HEIGHT})"
                )
                time.sleep(2)
                self.browser.save_screenshot(f"screenshots/{size}x{section}.png")

    def start(self):
        # for url in self.urls:
        self.screenshot(self.url)
        self.browser.quit()

tester = ResponsiveTester("https://nomadcoders.co")
tester.start()