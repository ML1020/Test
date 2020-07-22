# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
time.sleep(3)
browser.get("http://www.baidu.com")



# 多层框架或窗口的定位：
# switch_to_frame()

# 鼠标事件
# browser.find_element_by_id("kw").send_keys("乃万")
# su1 = browser.find_element_by_id("su")
# # 右击
# ActionChains(browser).context_click(su1).perform()
# time.sleep(5)
# # 双击
# ActionChains(browser).double_click(su1).perform()
# time.sleep(5)
# browser.quit()

# 键盘键组合使用
# #输入框输入内容
# browser.find_element_by_id("kw").send_keys("selenium")
# time.sleep(3)
# #ctrl+a 全选输入框内容
# browser.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# time.sleep(3)
# #ctrl+x 剪切输入框内容
# browser.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# time.sleep(3)
# #输入框重新输入内容，搜索
# browser.find_element_by_id("kw").send_keys("webdriver")
# browser.find_element_by_id("su").click()
# time.sleep(3)
# browser.quit()

#浏览器的滚动
# browser.find_element_by_id("kw").send_keys("乃万")
# browser.find_element_by_id("su").submit()
# browser.maximize_window()
# time.sleep(5)
# # 滚动到最低端
# js = "var q=document.documentElement.scrollTop=10000"
# browser.execute_script(js)
# time.sleep(5)
# # 滚动到最顶端
# js = "var q=document.documentElement.scrollTop=0"
# browser.execute_script(js)
# time.sleep(5)
# browser.quit()

# 浏览器的后退与前进
# browser.find_element_by_id("kw").send_keys("乃万")
# browser.find_element_by_id("su").submit()
# time.sleep(5)
# browser.back()
# time.sleep(5)
# browser.forward()
# time.sleep(5)
# browser.quit()

#页面的放大与缩小
# time.sleep(5)
# browser.maximize_window()
# time.sleep(5)
# browser.minimize_window()
# time.sleep(5)
# browser.set_window_size(20,40)
# time.sleep(3)
# browser.quit()

#打印标题和网址
# title = browser.title
# print(title)
# url = browser.current_url
# print(url)
# browser.quit()

#等待
# browser.find_element_by_id("kw").send_keys("乃万")
# browser.find_element_by_id("su").submit()
# # time.sleep(6)    #固定等待
# #智能等待
# browser.implicitly_wait(6)
# browser.find_element_by_link_text("乃万_百度百科").click()
# time.sleep(5)
# browser.quit()

#一些操作
# time.sleep(3)
# browser.find_element_by_css_selector("#kw").send_keys("520")
# browser.find_element_by_xpath("//*[@id='su']").click()
# time.sleep(10)
# # class前面加.   ， id前面加#
# browser.find_element_by_css_selector(".s_ipt").clear()
# time.sleep(10)
# browser.find_element_by_id("kw").send_keys("步步惊心")
# browser.find_element_by_id("su").submit()
# time.sleep(10)
# browser.quit()