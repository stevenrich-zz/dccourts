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

alph1 = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
alph2 = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
alph3 = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

for a in alph1:
  for b in alph2:
    for c in alph3:
      driver = webdriver.Firefox()
      driver.get("https://www.dccourts.gov/cco/maincase.jsf")
      element = driver.find_element_by_name("appData:searchform:jspsearchpage:lastName")
      element.send_keys(str(a) + str(b))
      element2 = driver.find_element_by_name("appData:searchform:jspsearchpage:firstName")
      element2.send_keys(str(c))
      driver.find_element_by_name("appData:searchform:jspsearchpage:submitSearch").click()
      page = driver.page_source
      soup = BeautifulSoup(page)
      outfile = open("scrape/" + str(c) + "_" + str(a) + str(b) + ".txt", "w")
      print >> outfile, soup.prettify()
      print >> compile_file, str(last) + "," + str(first)
      print "Found cases for " + str(last) + ", " + str(first)
      driver.quit()
