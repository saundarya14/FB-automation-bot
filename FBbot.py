from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string, random


class FBAutom:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()

        user_name = "add username"
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(user_name)

        passw = "add password here"
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(passw)

        self.driver.find_element_by_xpath('//*[@id="u_0_d"]').click()

    def updateStatus(self):
        message = "Enter your message here"

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]'))).send_keys(message)

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,

                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div'))).click()

    def addFriend(self):
        letter = str(random.choice(string.ascii_letters).lower())
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                               '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div/div/div/label/input'))).click()

        searchbar = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input')
        searchbar.click()
        searchbar.send_keys(letter).send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/a/div[1]/div[2]/div'))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]'))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="{"name":"users_location","args":"103764692995857"}"]/div/div[1]/div'))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[3]/span/divdle'))).click()

    def comment(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a'))).click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[3]/div[1]'))).click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[6]/div[2]/div[1]/a/span'))).click()
        comment_to_post = "add your comment"
        sleep(10)

        recentpost = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div')
        recentpost.send_keys(comment_to_post).send_keys(Keys.ENTER)

    def home(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[1]/a/svg/path[1]'))).click()


bot = FBAutom()
bot.login()
sleep(20)
bot.addFriend()
bot.home()
bot.comment()
bot.home()
bot.updateStatus()
