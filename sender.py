from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import telebot


TELEGRAM_TOKEN = ''
CHAT_ID = ''
bot = telebot.TeleBot(TELEGRAM_TOKEN)


CHROME_DRIVER_PATH = r""
URL = ''

sent_ads = set()  

def setup_selenium():

def fetch_ads(driver):

def send_to_telegram(ad):

def main():

if __name__ == '__main__':
    main()