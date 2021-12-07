import allure

from base_page import BasePage
from common.commonstep import *
import time

class AddInfoPage(BasePage):
    @allure.story('填入项目基本信息')
    def add_basic_info(self,pinlei):
        self.set_file_key(pinlei)
        return AddInfoPage(self.driver)
    def wait_ele(self):
        list = ['主要类型','次要类型','内容类型','语言','年代','主题','风格','地区']
        choice_biaoqian(self.driver,list)
    def upload_image_video(self,pinlei):
        if pinlei=='知识付费':tu = 2
        else:tu=1
        self.upload_yangpian(tu)


