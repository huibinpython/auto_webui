import sys,time,os
import time
from page import myConst
points = myConst.points

def findElement(driver, name, sleeptime=0.1):  # 具体业务CASE中与waifForElement配合使用,如果有找不到的情况，waitelement会返回-1
    time.sleep(sleeptime)
    ele = points[name]
    type = ele['type']
    locator = ele['locator']
    if type == 'id':
        return driver.find_element_by_id(locator)
    elif type == 'link_text':
        return driver.find_element_by_link_text(locator)
    elif type == 'xpath':
        return driver.find_element_by_xpath(locator)
    elif type == 'css_selector':
        return driver.find_element_by_css_selector(locator)
    elif type == 'class_name':
        return driver.find_element_by_class_name(locator)
    else:
        return -1

def findElements(driver, name, sleeptime=0.3):  # 具体业务CASE中与waifForElement配合使用,如果有找不到的情况，waitelement会返回-1
    time.sleep(sleeptime)
    ele = points[name]
    type = ele['type']
    locator = ele['locator']
    if type == 'id':
        return driver.find_elements_by_id(locator)
    elif type == 'link_text':
        return driver.find_element_by_link_text(locator)
    elif type == 'xpath':
        return driver.find_elements_by_xpath(locator)
    elif type == 'css_selector':
        return driver.find_elements_by_css_selector(locator)
    elif type == 'class_name':
        return driver.find_elements_by_class_name(locator)
    else:
        return -1
def scroll_to(driver, target_element):
    """
    将页面滚动到指定元素可见
    @param driver:
    @param target_element: 而不是元素名。所以调用之前先取得元素
    @return:
    """
    try:
        driver.execute_script("arguments[0].scrollIntoView();", target_element)
    except Exception as e:
        print(Exception, ":", e)
def waitForElement(driver ,name, n=150):
    try:
        for i in range(n):  # 默认等15秒，等不到就超时，想改时间就传为第三个参数
            try:
                if findElement(driver,name):
                    time.sleep(1)
                    break
            except:
                pass
            time.sleep(0.1)
        else:
            return -1
    except:
        return -1

def set_value(driver, ele, contant):
    element = findElement(driver,ele)
    element.clear()
    element.send_keys(contant)

def getTimeStamp(type=1):
    if type ==1:
        return time.strftime('%m%d%H%M', time.localtime(time.time()))  # 时间戳格式如20160422100000
    elif type==2  :  # 视频发文时会验证标题中不许有连续3个以上相同数字，所以加这个类型的输出
        return time.strftime('%Y年%m月%d日%H:%M:%S', time.localtime(time.time()))  # 时间戳格式如2016年04月22日10:00:00
    elif type ==3:  # CMS，好多地方验18个字长的标题，所以改短一点
        return time.strftime('%m%d%H%M', time.localtime(time.time()))  # 时间戳格式如0422100000
    elif type == 4:  # 2017-04-17 15:02:00
        return time.strftime('%Y-%m-', time.localtime(time.time()))

def write_an_inputArea(driver ,eleName ,content,isclear=1):
    if waitForElement(driver ,eleName) != -1:
        time.sleep(1)
        if isclear == 1:
            findElement(driver ,eleName).clear()
        findElement(driver ,eleName).send_keys(content)
    else :print ('未找到元素')

def click_an_ele_name(driver ,ele,to_move=1):
    # 通过points 里面的  值 找到元素点击
    time.sleep(0.2)
    if waitForElement(driver,ele) != 1:
        ele_name = findElement(driver, ele)
        if to_move == 1:
            rect = ele_name.rect  # 以字典方式返回元素的大小和坐标
            driver.execute_script("window.scrollTo(0,{})".format((rect['y'] - 80)))
        driver.execute_script("arguments[0].click();", ele_name)

def click_an_element(driver ,eleName,toyidong=1):
    # 找到元素点击
    time.sleep(0.2)
    if toyidong ==1:
        rect = eleName.rect  # 以字典方式返回元素的大小和坐标
        driver.execute_script("window.scrollTo(0,{})".format((rect['y'] - 80)))
    driver.execute_script("arguments[0].click();", eleName)




def select_actors(driver ,ele ,contant):
    # 填入演职人员
    findElement(driver,ele).send_keys(contant)
    time.sleep(1.3)
    points['ss_click'] = {'type':'xpath','locator':f"//span[contains(text(),'{contant}')]"}
    findElement(driver,'ss_click').click()

def choice_biaoqian(driver,ele,to_click=1):
    for name in ele:
        points['biaoqian'] = {'type': 'xpath',
                              'locator': f"//label[text()='{name}']/../following-sibling::div/div/div"}
        points['biaoqianc'] = {'type': 'xpath',
                               'locator': f"//label[text()='{name}']/../following-sibling::div//div["
                                          f"@class='DumpSelect_optionItem__rInYT'][1]"}
        biaoqianc = findElement(driver,'biaoqianc')
        biaoqian = findElement(driver,'biaoqian')
        time.sleep(0.2)
        click_an_element(driver,biaoqian)
        print('点击标签输入框')
        time.sleep(0.5)
        biaoqianc.click()
        if to_click==1:
            time.sleep(0.3)
            biaoqian.click()

def send_pdf_to_input(driver,name):
    # 输入PDf
    points['pdf_ele'] = {'type':'xpath','locator':f"//*[contains(text(),'{name}')]/../following-sibling::div//input"}
    con_filepath = f'F:\\XingTu\\doc\\{name}.pdf'
    findElement(driver,'pdf_ele').send_keys(con_filepath)

def select_radio(driver,ele,xx_name):
    # 选择，单选项，或多选项
    points['radio_ele_linshi'] = {'type':'xpath','locator':
                                  f"//*[contains(text(),'{ele}')]/../following-sibling::div//label[contains(text(),'{xx_name}')]"}
    click_an_ele_name(driver,'radio_ele_linshi')

def select_time(driver,ele_input,ele_zujian):
    # 选择出品时间
    findElement(driver,ele_input).click()
    time.sleep(0.3)
    findElement(driver,ele_zujian).click()

def beian_radio(driver,pinlei,beian):
    if pinlei == '网络剧':
        points['beian_si'] = {'type':'xpath','locator':"//*[contains(text(),'备案司')]/../following-sibling::div//label"}
        beiansi = findElements(driver,'beian_si')
        if beian in [7,8]:
            beiansi[1].click()
        elif beian == 9:
            beiansi[2].click()
    points['beian_zt'] = {'type': 'xpath', 'locator': "//*[contains(text(),'备案状态')]/../following-sibling::div//label"}
    beianzt = findElements(driver, 'beian_zt')
    if beian in [2,5,8]:
        click_an_element(driver,beianzt[1])
        print(f'点击元素{beianzt[1].text}')
    if beian in [3,6]:
        click_an_element(driver,beianzt[2])
        print(f'点击元素{beianzt[2].text}')
#--用windos控件上传单个资源---------------------------------------------------------------------------------------
def uploadMyFile(args):#调用这个方法前，建议先判断if driver.switch_to_alert():
    try:
        #传参形如   args="D:\\testpic\\6.jpg"
        file=getParentPath()+u'\\autoscripts\\upload_single_file.exe'+' '+args
        os.system(file)
    except Exception as e:
        print(e)
#--得到当前所在路径的父路径，保存截图、结果用-------------------------------------------------------------------------
def getParentPath():
    path=os.path.dirname(os.path.split(os.path.realpath(__file__))[0])  #common文件夹的父路径
    return str(path)
#--用windos控件上传多个图片---------------------------------------------------------------------------------------
def uploadMultiImage():#调用这个方法前，建议先判断if driver.switch_to_alert():
    try:
        file = getParentPath() + u'\\autoscripts\\upload_multi_img.exe'
        os.system(file)
    except Exception as e:
        print(e)

#--用windos控件上传一个图片---------------------------------------------------------------------------------------
def uploadSingleImage():#调用这个方法前，建议先判断if driver.switch_to_alert():
    try:#不用默认的就调uploadMyFile
        uploadMyFile('D:\\testpic\\6.jpg')
    except Exception as e:
        print(e)
#-------------------点一个上传按钮，上传一个图片，等待一个标识元素出现，找不到上传按钮时提示errmsg--------------
def upload_single_file(driver,buttonEleName,flagEleName,errmsg,filepath=''):
    #    buttonEleName:上传按钮
    #    flagEleName:上传成功的标识元素
    #errmsg:找不到上传按钮时报错信息
    #filepath:文件路径，##传参形如"D:\\testpic\\6.jpg"
    try:
        result = False
        if waitForElement(driver,buttonEleName) != -1:
            scrollTo(driver, findElement(driver, buttonEleName))
            findElement(driver, buttonEleName).click()
            # if driver.switch_to_alert():
            if filepath=='':
                uploadSingleImage()
            else:
                uploadMyFile(filepath)
            if waitForElement(driver, flagEleName) != -1:
                result = True
            else:print (u'未找开上传成功的标识',flagEleName)
            # else:print (u'未弹出选图对话框')
        else:print (errmsg)
        return result
    except Exception as e:
        print(e)
        return result

#-----------scroll to target element-----------------------------------------------------------------------
def scrollTo(driver,targetelement):#将页面滚动到指定元素可见
    ## targetelement指的是元素，而不是元素名。所以调用之前先取得元素
    try:
        driver.execute_script("arguments[0].scrollIntoView();", targetelement)
    except Exception as e:
        print(e)
