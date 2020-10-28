import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\bogdayn\тест бот\chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://miet.ru/search")
        try:
        	search_bar = driver.find_element_by_class_name("search-bar__int")
        	search_bar.send_keys("asdasd")
        except Exception:
        	print("Ошибка с поиском")
        #поиск элемента ввода по атрибуту имени класса
        try:
        	driver.get("https://miet.ru/search")
        	search_bar = driver.find_element_by_class_name("search-bar__input")
        except Exception:
        	print("Ошибка с поиском")
        #отсылаю нажатия клавиш
        search_bar.send_keys("Кожухов")
        search_bar.send_keys(Keys.RETURN)
        #проверка наличия таблицы с результатми
        try:
        	list_of_results = driver.find_element_by_class_name("result-list")
        except Exception:
        	print("Результаты не найдены")
        #переход по ссылке если текст в классе соответствует введеному тут значению
        people = driver.find_element_by_link_text("Люди")
        people.send_keys(Keys.RETURN)

        elem2 = driver.find_element_by_link_text("Кожухов Игорь Борисович")
        elem2.send_keys(Keys.RETURN)
    def tearDown(self):
    	#закрытие вкладки браузера
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
