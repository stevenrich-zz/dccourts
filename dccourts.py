import time
import re
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import csv

print "Scraping DC Superior Court site..."

display = Display(visible=0, size=(800,600))
display.start()
