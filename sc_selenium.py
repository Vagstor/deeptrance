import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import Settings
from config.constants import constant
import utils
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

# Настройки
SMARTCAT_LOGIN = Settings.SC_LOGIN
SMARTCAT_PASSWORD = Settings.SC_PASSWORD
#FILE_PATH = os.path.join(constant.root_dir, 'orig', 'Forklift_EN.docx')  # Файл для перевода
#TARGET_LANGUAGE = "Russian"  # Язык перевода

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# 1. Вход в Smartcat
def login():
    driver.get("https://smartcat.ai/user/login")
    driver.find_element(By.NAME, "email").send_keys(SMARTCAT_LOGIN)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # sc-button sc-button_44 sc-button_cta-black email-form__submit
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys(SMARTCAT_PASSWORD + Keys.ENTER)

# 2. Загрузка документа
def open_file():
    time.sleep(3)
    driver.get("https://smartcat.com/workspace")
    
    # Создание проекта
    #time.sleep(5)
    #driver.find_element(By.XPATH,"/project/a0e5505e-6ac0-49ec-8c08-dafecaa7584d")
    #driver.find_element(By.CSS_SELECTOR, "[data-testid='CreateProjectButtonMainMenu']").click()
    #driver.find_element(By.ID, "project-name").send_keys("AutoTranslate Project")
    
    # Открытие файла
    time.sleep(2)
    all_project_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-testid='GoToProject']")
    #project_selection = input('Which project to open?')
    all_project_buttons[0].click()
    #driver.execute_script("all_project_buttons[0].click();", all_project_buttons)
    all_project_files = driver.find_elements(By.CSS_SELECTOR, "[data-testid='link-name']")
    all_project_files[0].click()

    # Загрузка файла
    # upload_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='select-file-btn']")
    # upload_input.send_keys(FILE_PATH)
    # time.sleep(5)  # Ожидание загрузки
    # driver.find_element(By.CSS_SELECTOR, "button[data-test-id='next-btn']")
    
    # Выбор языка перевода
    # time.sleep(4)
    # Select(driver.find_element(By.ID, "target-language")).select_by_visible_text(TARGET_LANGUAGE)
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(2)

def enter_with_timeout():
    while True:
        time.sleep(1)
        active_element = driver.switch_to.active_element
        #time.sleep(1)
        active_element.send_keys(Keys.CONTROL + "1")
        #actions = ActionChains(driver)
        #actions.key_down(Keys.CONTROL).send_keys("1").key_up(Keys.CONTROL).perform()
        active_element.send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(1)

def pass_to_cell():
    cells_number = driver.find_elements(By.CLASS_NAME, "grid-number-column__value")
    client = utils.create_ds_client()

    for i in cells_number:
        messages = utils.create_starting_message()
        #time.sleep(3)
        active_element = driver.switch_to.active_element
        #active_element.clear()
        active_element.send_keys(Keys.TAB)
        #time.sleep(1)
        active_element = driver.switch_to.active_element
        active_element.send_keys(Keys.CONTROL + 'a')
        #time.sleep(1)
        active_element.send_keys(Keys.CONTROL + 'c')
        #time.sleep(1)
        while True:
            try:
                print(pyperclip.paste())
                messages = utils.add_string_to_message(messages, pyperclip.paste())
                completion = utils.create_completion(client, messages)
            except:
                print("No response from server, trying again...")
                time.sleep(10)
                continue
            finally:
                print(f"Segment {i.text} translated, moving on to paste")
                pyperclip.copy(completion.choices[0].message.content)
                break
        #time.sleep(1)
        active_element.send_keys(Keys.TAB)
        active_element = driver.switch_to.active_element
        #time.sleep(2)
        active_element.send_keys(Keys.CONTROL + 'a')
        #time.sleep(1)
        active_element.send_keys(Keys.CONTROL + 'v')
        #active_element.send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(0.5)
        active_element.send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(6)
    time.sleep(1)

# 3. Запуск машинного перевода
# def start_translation():
#     # Выбор MT (например, Smartcat MT)
#     driver.find_element(By.CSS_SELECTOR, "button[data-test-id='pre-translate-btn']").click()
#     driver.find_element(By.XPATH, "//span[contains(text(),'Smartcat MT')]").click()
#     driver.find_element(By.CSS_SELECTOR, "button[data-test-id='pre-translate-run-btn']").click()
#     time.sleep(10)  # Ожидание перевода

# 4. Скачивание результата
# def download_file():
#     driver.find_element(By.CSS_SELECTOR, "button[data-test-id='export-btn']").click()
#     driver.find_element(By.XPATH, "//span[contains(text(),'Download')]").click()
#     time.sleep(5)  # Ожидание скачивания

# Главная функция
def main():
    try:
        login()
        open_file()
        enter_with_timeout()
        #pass_to_cell()
        #download_file()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()