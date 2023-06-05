import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ActionChains

user = '学号'
pwd = '密码'
def check(j, k):
    try:
        driver.find_element('xpath',"//*[@id='ajaxForm1']/div[2]/div[1]/div[2]/table[{}]/tbody/tr[{}]/td[2]/div/div[1]/label/input".format(j,k)).click()
        print('已点击')
    except:
        print('未找到，进行下一个')



if __name__ == '__main__':
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    action = ActionChains(driver)
    driver.maximize_window()
    #登录页面
    url1 = 'http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html'
    #教学评价页面（因网址带有个人学号等资料，请自行复制自己的教学评价网址）
    url2 = '因网址带有个人学号等资料，请自行复制自己的教学评价网址'
    driver.get(url1)
    time.sleep(3)
    u = driver.find_element('xpath', "//*[@id='yhm']")
    p = driver.find_element('xpath', "//*[@id='mm']")
    u.send_keys(user)
    p.send_keys(pwd)
    d = driver.find_element('xpath', "//*[@id='dl']")
    d.click()
    time.sleep(2)
    driver.get(url2)
    time.sleep(2)
    sl = driver.find_element('xpath', "//*[@id='pager_center']/table/tbody/tr/td[8]/select/option[7]")
    sl.click()
    time.sleep(1)
    #获取完成情况
    done = driver.find_element('xpath', "//*[@id='bc']/span")
    notdone = driver.find_element('xpath', "//*[@id='wp']/span")
    start = int(done.text) + 1
    end = int(notdone.text) + start - 1
    #开始评价
    for i in range(start, end + 1):
        driver.find_element('xpath', "//*[@id={}]".format(i)).click()
        time.sleep(1)
        #遍历评价（嫌慢可以修改j的个数，建议不低于6）
        for j in range(1, 11):
            for k in range(1, 11):
                check(j, k)
                time.sleep(0.1)
        driver.find_element('xpath', "//*[@id='btn_xspj_bc']").click()
        time.sleep(1)
        driver.find_element('xpath', "//*[@id='btn_ok']").click()
        time.sleep(1)
    #提交评价并自动关闭浏览器
    driver.find_element('xpath', "//*[@id='btn_xspj_tj']").click()
    time.sleep(1)