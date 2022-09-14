from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser


class RecipeHomePageFunctionalTest(LiveServerTestCase):
    def test_the_test(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
