
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://courses.letskodeit.com/practice")
get_wait = WebDriverWait(driver, 10)


class TestActions:

    def radio_button(self):
        click_bmw = driver.find_element(By.ID, 'bmwradio')
        assert not click_bmw.is_selected()
        click_bmw.click()
        assert click_bmw.is_selected()

        click_benz = driver.find_element(By.ID, 'benzradio')
        assert not click_benz.is_selected()
        click_benz.click()
        assert click_benz.is_selected()

        click_honda = driver.find_element(By.ID, 'hondaradio')
        assert not click_honda.is_selected()
        click_honda.click()
        assert click_honda.is_selected()

    def checkbox(self):
        click_BMW = driver.find_element(By.ID, 'bmwcheck')
        assert not click_BMW.is_selected()
        click_BMW.click()
        assert click_BMW.is_selected()
        click_BMW.click()

        click_Benz = driver.find_element(By.ID, 'benzcheck')
        assert not click_BMW.is_selected()
        click_Benz.click()
        assert click_Benz.is_selected()
        click_Benz.click()

        click_honda = driver.find_element(By.ID, 'hondacheck')
        assert not click_Benz.is_selected()
        click_honda.click()
        assert click_honda.is_selected()

        click_Benz.click()
        assert click_Benz.is_selected(), click_honda.is_selected()
        assert not click_BMW.is_selected()

        click_BMW.click()
        assert click_BMW.is_selected(), click_honda.is_selected()
        assert click_Benz.is_selected()

        click_honda.click()
        assert not click_honda.is_selected()
        assert click_Benz.is_selected(), click_BMW.is_selected()
        click_honda.click()
        get_wait.until(EC.presence_of_element_located((By.ID, 'hondacheck')))

        click_Benz.click()
        assert not click_Benz.is_selected()
        assert click_honda.is_selected(), click_BMW.is_selected()

    def switch_window(self):
        check_open_window = driver.find_element(By.CSS_SELECTOR, 'button[id="openwindow"]')
        assert check_open_window.is_enabled()

    def switch_tab(self):

        get_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="openwindow"]')))
        check_open_tab = driver.find_element(By.ID, 'opentab')
        assert check_open_tab.is_enabled()

    def select_class(self):

        car_types_field = driver.find_element(By.ID, 'carselect')
        car_types_field.click()
        cars = Select(car_types_field)
        cars.select_by_index(0)
        cars.select_by_value("honda")

        car_types_field.select_by_index(0)
        assert car_types_field.is_displayed()

        car_types_field.select_by_value("benzene")
        assert car_types_field.is_displayed()

        car_types_field.select_by_value("bmw")
        assert car_types_field.is_displayed()

    def multiple_select(self):
        get_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'option[value="apple"]')))
        click_apple = driver.find_element(By.CSS_SELECTOR, 'option[value="apple"]')
        click_apple.click()
        assert click_apple.is_displayed()
        click_orange = driver.find_element(By.CSS_SELECTOR, 'option[value="orange"]')
        click_orange.click()
        assert click_orange.is_displayed()
        click_peach = driver.find_element(By.CSS_SELECTOR, 'option[value="peach"]')
        click_peach.click()
        assert click_peach.is_displayed()

    def element_displayed(self):

        click_hide = driver.find_element(By.ID, 'hide-textbox')
        click_hide.click()
        click_show = driver.find_element(By.ID, 'show-textbox')
        input_fild = driver.find_element(By.CSS_SELECTOR, 'input[id="displayed-text"')
        assert not input_fild.is_displayed()
        click_show.click()
        input_fild.send_keys("kakach")
        assert input_fild.is_displayed()

    def alert_section(self):
        first_name = "Steven"
        second_name = "Green"

        alert_fild = driver.find_element(By.CSS_SELECTOR, 'input[name="enter-name"]')
        alert_fild.send_keys(first_name)

        click_alert = driver.find_element(By.ID, 'alertbtn')
        click_alert.click()
        click_alert = driver.switch_to.alert
        assert click_alert.text == f"Hello {first_name}, share this practice page and share your knowledge"
        click_alert.accept()

        get_wait.until(EC.element_to_be_clickable((By.ID, 'confirmbtn')))
        alert_fild = driver.find_element(By.CSS_SELECTOR, 'input[name="enter-name"]')
        alert_fild.send_keys(second_name)
        click_confirm = driver.find_element(By.ID, 'confirmbtn')
        click_confirm.click()
        click_confirm = driver.switch_to.alert
        assert click_confirm.text == f"Hello {second_name}, Are you sure you want to confirm?"
        click_confirm.accept()
        driver.execute_script("window.scrollBy(0, 200);")

    def mouse_hover(self):

        click_hove = driver.find_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        get_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="mousehover"]')))
        hove_fild = ActionChains(driver)
        hove_fild.move_to_element(click_hove).perform()

        click_top = driver.find_element(By.CSS_SELECTOR, 'a[href="#top"]')
        assert click_top.is_enabled()
        click_reloady = driver.find_element(By.XPATH, '//a[contains(text(), "Reload")]')
        assert click_reloady.is_enabled()



obj = TestActions()
obj.radio_button()
obj.checkbox()
obj.switch_window()
obj.switch_tab()
obj.select_class()
obj.multiple_select()
obj.element_displayed()
obj.alert_section()
obj.mouse_hover()