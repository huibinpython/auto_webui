from web_ui.xt.page.add_info_page import AddInfoPage
from web_ui.xt.page.base_page import BasePage
from web_ui.xt.common.commonstep import *
import time


class MainPage(BasePage):
    def Login_xt(self):
        if waitForElement(self.driver,'btn-login') != -1:
            findElement(self.driver,'btn-login').click()
            click_an_ele_name(self.driver,'login-qq',2)
            self.driver.switch_to.frame("_login_frame_quick_")
            self.driver.switch_to.frame('ptlogin_iframe')
            findElement(self.driver,'qqlogin').click()
            set_value(self.driver,'qquser', '2625295983')
            set_value(self.driver,'qqpass', 'ZY9956zy..--++')
            findElement(self.driver,'login_button').click()
            time.sleep(8)
        else:
            print('没找到帐号输入框')
        return MainPage(self.driver)
    def go_project_list(self,pinlei):
        pl_ming = ''
        if pinlei == "网络电影":
            pl_ming = 'net_film'
        elif pinlei == '动漫':
            pl_ming = 'animation'
        elif pinlei == '纪录片':
            pl_ming = 'documentary'
        elif pinlei == '网络剧':
            pl_ming = 'net_series'
        elif pinlei == '少儿':
            pl_ming = 'kids'
        elif pinlei == '知识付费':
            pl_ming = 'knowledge'
        elif pinlei == '微短剧':
            pl_ming = 'micro_short_drama'
        elif pinlei == '综艺':
            pl_ming = 'variety_show'
        url = f'https://dev.mp.v.qq.com/dashboard/manage/{pl_ming}'
        self.driver.get(url)
        time.sleep(8)
        return MainPage(self.driver)

    def create_project(self,pinlei):
        # 创建项目，成片
        # self.check_riqi_input
        self.create_project_basic(pinlei)
        return MainPage(self.driver)

    def go_add_info(self):
        self.driver.find_element_by_link_text('补充资料').click()
        # wh = self.driver.window_handles
        # self.driver.switch_to_window(wh[-1])
        # print(f'跳转到新打开的页面时间：{getTimeStamp(2)}')
        time.sleep(3)
        return AddInfoPage(self.driver)







