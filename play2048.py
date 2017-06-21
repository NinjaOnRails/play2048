from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

gameContainer = browser.find_element_by_class_name('game-container')
gameOver = None
while not gameOver:
    try:
        gameOver = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.CLASS_NAME, "game-over")))
    except TimeoutException:
        gameContainer.send_keys(Keys.UP)
    if not gameOver:
        try:
            gameOver = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.CLASS_NAME, "game-over")))
        except TimeoutException:
            gameContainer.send_keys(Keys.RIGHT)
    else:
        break
    if not gameOver:
        try:
            gameOver = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.CLASS_NAME, "game-over")))
        except TimeoutException:
            gameContainer.send_keys(Keys.DOWN)
    else:
        break
    if not gameOver:
        try:
            gameOver = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.CLASS_NAME, "game-over")))
        except TimeoutException:
            gameContainer.send_keys(Keys.LEFT)
    else:
        break
print('Game Over.')
