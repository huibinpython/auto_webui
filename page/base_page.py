import random
import time

import allure

from web_ui.xt.common.project_config import *
from selenium import webdriver
from web_ui.xt.common.file_config import *
from web_ui.xt.common.commonstep import *

class BasePage:

    def __init__(self, base_driver = None):
        # chrome --remote-debugging-port=9222
        if base_driver == None:
            # self.driver = webdriver.Chrome()
            # self.driver.get('https://dev.mp.v.qq.com')
            opt = webdriver.ChromeOptions()
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=opt)
            # self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        else :
            self.driver = base_driver
    # 填入所有 项目信息
    def set_file_key(self,pinlei):
        file_list = []
        with allure.step('设置付费类型需要输入的字段'):
            if 'FuFei' in pinlei_config[pinlei].keys():
                file_list += fufei_config[pinlei_config[pinlei]['FuFei']]
        with allure.step('设置是否IP需要输入的字段'):
            file_list += ip_config[pinlei_config[pinlei]['ip']]
        with allure.step('设置资质信息需要的字段'):
            file_list += beian_config[pinlei_config[pinlei]['beiAn']]
        # print(file_list)
        file_list += pinlei_file_config_dic[pinlei]
        for file in file_list:
            file_dic = file_config_dic[file]

            with allure.step(f'使用【{file_dic["func"]}】方法，操作【{file}】字段'):
                self.call_my_fun(eval(file_dic['func']),**file_dic['arg'])
        if pinlei != '知识付费':
            self.set_banquan_pdf()

    def create_project_basic(self,pinlei):
        # 创建项目，成片
        click_an_ele_name(self.driver,'cjxm_btn')
        create_file_list = []
        project_leixing = pinlei_config[pinlei]['project_leixing']
        shouquan = pinlei_config[pinlei]['shouquan']
        sj = getTimeStamp(3)
        if project_leixing == 1:
            project_name = '{}初审不通过'.format(pinlei) + sj
        else:
            create_file_list.append('选择项目方案')
            project_name = '{}方案测试'.format(pinlei) + sj
        if shouquan != 1:
            create_file_list.append('授权非独播')
        if pinlei in ['纪录片方案','少儿方案']:
            create_file_list += ['投资成本', '启动时间', '项目提交-btn']
        else:
            create_file_list += ['投资成本','出品时间','项目提交-btn']
        write_an_inputArea(self.driver,'xm_mc',project_name)
        for i in create_file_list:
            print(f'开始输入{i}')
            file_dic = file_config_dic[i]
            self.call_my_fun(eval(file_dic['func']), **file_dic['arg'])
        points['ls_project_name'] = {'type':'xpath','locator':f'//*[contains(text(),"{project_name}")]'}
        waitForElement(self.driver,'ls_project_name')

    def call_my_fun(self,funcname, **kwargs):
        funcname(self.driver,**kwargs)


    def set_banquan_pdf(self):
        # 输入版权证明
        bq_name = ['出品方版权证明文件', '联合出品方版权正面文件', '发行方版权证明文件']
        pdf_list = findElements(self.driver, 'pdf')
        for i in range(1,4):
            print(f'输入{bq_name[-i]}')
            time.sleep(0.2)
            pdf_list[-i].send_keys(u'F:\XingTu\doc\{}.pdf'.format(bq_name[-i]))


    def upload_yangpian(self,tu):
        # 上传样片
        name = self.driver.find_element_by_xpath('//*[contains(@class,"projName")]')
        click_an_ele_name(self.driver,'yp_xy')
        upload_single_file(self.driver,'yp_sc','yp_sc_sucess','没找到上传按钮',u'F:\\XingTu\\video\\video_2.mp4')
        if  tu ==1:
            write_an_inputArea(self.driver,'haibao_heng',f'F:\XingTu\image\横图\\{random.randint(1,12)}.jpg',2)
            time.sleep(1.5)
            write_an_inputArea(self.driver, 'haibao_shu', f'F:\XingTu\image\竖图\\{random.randint(1, 9)}.jpg',2)
            click_an_ele_name(self.driver,'juzhao',2)
            findElement(self.driver,'jz_tc').click()
            time.sleep(2)
            file =getParentPath()+u'\\autoscripts\\upload_some.exe'
            os.system(file)
            time.sleep(3.5)
            findElement(self.driver, 'qr_btn').click()
            time.sleep(3)
        findElement(self.driver,'xm_bccg').click()
        findElement(self.driver, 'by_yl').click()
        time.sleep(5)
        click_an_ele_name(self.driver,'tijiao')
        time.sleep(1)
        findElement(self.driver, 'qr_btn').click()
        if 'ls_project_name' not in points.keys():
            points['ls_project_name'] = {'type': 'xpath', 'locator': f'//*[contains(text(),"{name}")]'}
        waitForElement(self.driver, 'ls_project_name')







