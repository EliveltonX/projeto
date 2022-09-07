from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_DIR = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_DIR/'bin'/CHROMEDRIVER_NAME

# --headless


def make_chrome_browser(*options):

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser()
    browser.get('https://www.blender.org')
    browser.quit()