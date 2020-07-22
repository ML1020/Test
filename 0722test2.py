# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com')


# 多层框架/窗口定位
# switch_to_frame()
# switch_to_window()
## coding=utf-8
# from selenium import webdriver
# import time
# import os
# browser = webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('frame.html')
# browser.get(file_path)
# browser.implicitly_wait(30)
# #先找到到ifrome1（id = f1）
# browser.switch_to_frame("f1")
# #再找到其下面的ifrome2(id =f2)
# browser.switch_to_frame("f2")
# #下面就可以正常的操作元素了
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# time.sleep(3)
# browser.quit()

# 多层窗口的定位
# #coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import os
# dr = webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('level_locate.html')
# dr.get(file_path)
# #点击Link1链接（弹出下拉列表）
# dr.find_element_by_link_text('Link1').click()
# #找到id 为dropdown1的父元素
# WebDriverWait(dr,10).until(lambda the_driver:
# the_driver.find_element_by_id('dropdown1').is_displayed())
# #在父亲元件下找到link 为Action 的子元素
# menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')
# #鼠标定位到子元素上
# webdriver.ActionChains(dr).move_to_element(menu).perform()
# time.sleep(2)
# dr.quit()


# 下拉框的处理
# #coding=utf-8
# from selenium import webdriver
# import os,time
# driver= webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('drop_down.html')
# driver.get(file_path)
# time.sleep(2)
# #先定位到下拉框
# m=driver.find_element_by_id("ShippingMethod")
# #再点击下拉框下的选项
# m.find_element_by_xpath("//option[@value='10.69']").click()
# time.sleep(3)
# driver.quit()