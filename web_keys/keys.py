'''
    关键字驱动
'''
from time import sleep
from selenium import webdriver


def open_browse(txt):

    try:
        # 反射机制
        driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    # 临时driver对象
    def __init__(self, type):
        self.driver = open_browse(type)
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locate(name, value).click()

    # 强制等待
    def sleep(self, time):
        sleep(int(time))

    # 关闭
    def quit(self):
        self.driver.close()

    # 断言文本信息
    def assert_text(self, name, value, expect):
        try:
            reality == self.locate(name, value).text
            assert reality == expect, '{}不等于{}'.format(reality, expect)
            print('断言成功！')
            return True
        except Exception as e:
            print(e)
            return False