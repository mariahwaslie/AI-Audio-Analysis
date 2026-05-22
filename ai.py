import streamlit as st
import openai
import bs4 as BeautifulSoup
import requests
import moviepy
from openai import OpenAI
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()



client =OpenAI(api_key=API)
video_url= 'https://2370711-10.kaf.kaltura.com/browseandembed/index/media-redirect/entryid/1_c9jzequc/showDescription/false/showTitle/false/showTags/false/showDuration/false/showOwner/false/showUploadDate/false/playerSize/608x342/playerSkin/42909941/thumbEmbed//autoPlay//startTime//endTime/'
output_file = "video.mp4"  # Output file name
first_class_name = "mwPlayerContainer kdark ua-mouse ua-win ua-chrome size-medium start-state"
class_name_two = 'videoHolder hover'
class_name_three = 'videoDisplay'
username = 'w3144020'


driver = webdriver.Chrome()
driver.get(video_url)
time.sleep(1)
dropdown = driver.find_element(By.ID,'campus-select')
select = Select(dropdown)
select.select_by_visible_text(university)
driver.find_element(By.TAG_NAME,'button').click()
time.sleep(1)
student_id = driver.find_element(By.ID,'input27')
pass_input = driver.find_element(By.ID,'input35')

student_id.send_keys(username)
pass_input.send_keys(password)
driver.find_element(By.CLASS_NAME,'o-form-button-bar').click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,'o-form-button-bar').click()
time.sleep(60)

video_transcript = (driver.execute_script("return document.getElementsByXPath('/html/body/div[1]/div[3]/div[1]/video')[0].innerText"))
#
# div = driver.find_element(By.ID,"application")
# div2 = div.find_element(By.ID,'wrapper')
# div1 = div2.find_element(By.ID,'main')
# div3= div1.find_element(By.ID,'not_right_side')
# div4 = div3.find_element(By.ID,"content-wrapper")
# div5 = div4.find_element(By.ID,'content')
# div6 = div5.find_element(By.ID,'wiki_page_show')
# div7 =div6.find_element(By.CLASS_NAME,'show-content')
# div8 = div7.find_element(By.TAG_NAME,'p')
# iframe = div8.find_element(By.CSS_SELECTOR,'iframe')
#
#
#
#
# inside_iframe = iframe.text
# print(inside_iframe)
# doc_html = iframe.find_element(By.TAG_NAME,'html')
# doc_body = doc_html.find_element(By.TAG_NAME,'body')
# doc_div = doc_body.find_element(By.ID,'contentWrap')
# doc_div2 = doc_div.find_element(By.ID,'wrap')
# doc_div3 = doc_div2.find_element(By.ID,'content')
# doc_div4 = doc_div3.find_element(By.ID,'entryMedia')
# doc_div5 = doc_div4.find_element(By.ID,'mediaContainer')
# doc_div6 = doc_div5.find_element(By.ID,'wrapper')
# doc_div7 = doc_div6.find_element(By.ID,'player')
# doc_div8 = doc_div7.find_element(By.ID,'kplayer')
# iframe2 = doc_div8.find_element(By.TAG_NAME,'iframe')
#
# doc_div10 = doc_div8.switch_to.frame("kplayer_ifp")
#
# doc_div11 = doc_div10.find_element(By.TAG_NAME,'html')
# doc_div12 = doc_div11.find_element(By.TAG_NAME,'body')
# doc_div13 = doc_div12.find_element(By.TAG_NAME,'div')
# doc_div14 = doc_div13.find_element(By.CLASS_NAME,'videoHolder hover')
# doc_div15 = doc_div14.find_element(By.CLASS_NAME,'videoDisplay')
# video = doc_div15.find_element(By.TAG_NAME,'video')
# video_url = video.get_attribute('src')
#
# print(video_url)


# div8 = div7.find_element(By.CLASS_NAME,'lti-embed-container')
#
# #iframe_element = div7.find_element(By.TAG_NAME,'iframe')

#
# div3 =div2.execute_script("return document.getElementsById('not_right_side')")
# div4= div3.execute_script("return document.getElementsById('content-wrapper')")
# div5 = div4.execute_script("return document.getElementsById('content')")
# div6 = div5.execute_script("return document.getElementsById('wiki_page_show')")
# div7=div6.execute_script("return document.getElementsByClass('show-content user_content clearfix lti-content enhanced')")
# div8 =div7.execute_script("return document.getElementsByTag('iframe')")

# JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
# network_requests = driver.execute_script(JS_get_network_requests)
print(div6)
print("success")
driver.close()
# for i, url in enumerate(urls):
#     response = requests.get(i)
#     with open('video', "wb") as f:
#

