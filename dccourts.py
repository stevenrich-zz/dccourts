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
