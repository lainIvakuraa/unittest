import pytest
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class TestSearchNews(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_news(self):
        driver = self.driver
        driver.get("https://www.roseltorg.ru/")
        driver.find_element(By.CLASS_NAME, "menu__link").click()
        search = driver.find_element(By.CLASS_NAME, 'search-autocomplete__keywordinput')
        search.click()
        search.send_keys('0328300032823000956')
        search.send_keys(Keys.ENTER)
        

    def tearDown(self):
        self.driver.quit()

unittest.main()
TestSearchNews.setUp(unittest.TestCase)
TestSearchNews.test_search_news(unittest.TestCase)


'''driver.find_element(By.CSS_SELECTOR, "h1.news__title > a").click()
        driver.find_element(By.LINK_TEXT, "Спорт").click()
        last_element_text = driver.find_element(By.CLASS_NAME, "is-last").text
        assert last_element_text == "Спорт", "Крайний элемент в хлебных крошках не называется 'Спорт'"'''