# -*- coding: utf-8 -*-
import datetime
# ###############维护用例中用到的点击元素，存成key-value######################################################################
points = {}

# 按照这个格式填加：
# points['点击元素起个名字']={'type':'id/link_text/xpath/css_selector/class_name','locator':"表达式"}

# login
points['btn-login'] = {'type':'class_name','locator':"loginBtn___1ygQZ"} # 登录按钮
points['login-qq'] = {'type':'xpath','locator':"//*[text()='QQ登录']"}
points['qqlogin'] = {'type':'id','locator':"switcher_plogin"} #QQ帐号密码登录
points['qquser'] = {'type':'id','locator':'u'} #QQ号
points['qqpass'] = {'type':'id','locator':'p'} #QQ密码
points['login_button'] = {'type':'id','locator':'login_button'} #QQ登录按钮

#创建项目
points['post-text'] = {'type':'link_text','locator':"全部项目"} # 全部项目按钮
points['xm_fa_xuanxiang'] = {'type':'xpath','locator':"//*[contains(text(),'合作模式')]/../following-sibling::div/div[2]"} # 项目方案选项
points['cjxm_btn'] = {'type':'xpath','locator':'//*[contains(text(),"新建项目")]'}#创建项目按钮
points['xm_cpsj_zujian'] = {'type':'xpath','locator':"//tbody//div[text()='28']"}
points['xm_mc'] = {'type':'id','locator':'projName'} #项目名称输入框
points['xm_tzcb'] = {'type':'id','locator':'investmentCost'} #投资成本输入框
points['xm_cpsj'] = {'type':'xpath','locator':"//*[contains(text(),'出品时间')]/../following-sibling::div//input"} #出品时间输入框
points['xm_qdsj'] = {'type':'xpath','locator':"//*[contains(text(),'启动时间')]/../following-sibling::div//input"}
points['sqxz_fdj'] = {'type':'xpath','locator':"//*[contains(text(),'授权性质')]/../following-sibling::div//label[text()='非独家']"}
points['sqxz_dj'] = {'type':'xpath','locator':"//*[contains(text(),'授权性质')]/../following-sibling::div//label[text()='独家']"}
points['riqi_zj'] = {'type':'xpath','locator':"//tbody//div[text()='28']"}
points['xm_tj_btn'] = {'type':'xpath','locator':'//button[contains(text(),"创建")]'} # 创建项目提交按钮


#补充资料
### 演职人员信息
points['project_name'] = {'type':'id','locator':'projName'}
points['post-text'] = {'type':'link_text','locator':"补充资料"} #补充资料按钮
points['xm_zj_price'] = {'type':'id','locator':'coverUnitPrice'}                # 专辑单价
points['xm_zj_avg_price'] = {'type':'id','locator':'coverAvgPrice'}                 # 知识付费特有，专辑均价
points['daoyan'] = {'type':'id','locator':'directors.0'}   #导演
points['bianju'] = {'type':'id','locator':'writers.0'}                      # 编剧
points['zhipianren'] = {'type':'id','locator':'producters.0'}               # 制片人
points['zhuyan'] = {'type':'id','locator':'leadingActors.0.realName'}       # 主演
points['yanyuan'] = {'type':'id','locator':'actors.0.realName'}                 # 演员
points['zhuyan_shi'] = {'type':'id','locator':'leadingActors.0.roleName'}       # 主演饰
points['yanyuan_shi'] = {'type':'id','locator':'actors.0.roleName'}             # 演员饰
points['jiabin'] = {'type':'id','locator':'guestActors.0'}                      # 嘉宾(飞行）
points['jiabin_changzhu'] = {'type':'id','locator':'permanentGuestActors.0'}                      # 常驻嘉宾
points['zz_tudui'] = {'type':'id', 'locator':'productionTeam.0'}                # 制作团队
points['zz_tudui_are'] = {'type':'id', 'locator':'productionTeamStr'}
points['lv_shuoming'] = {'type':'id', 'locator':'resumeAndDesc'}                   # 履历说明
# points['ss_click'] = {'type':'xpath','locator':'//span[contains(text(),"测试专用")]'}       #搜索到人后点击
points['zhizuotuandui_jj'] = {'type':'id','locator':'productionTeamStr'} # 制作团队简介
# 内容信息
points['jishu'] = {'type':'id','locator':'episodeNumber'}                       # 集数
points['shichang'] = {'type':'id','locator':'perEpisodeLength'}                 # 单集时长
points['xm_knologe_speak'] = {'type':'id','locator':'speaker'}                  # 主讲人
points['knologe_introduction'] = {'type':'id','locator':'projIntroductionStr'}                  # 知识付费-简介
points['ipname'] = {'type':'id','locator':'IPName'}                             # IP名称
points['no_ip'] = {'type':'xpath','locator':"//*[contains(text(),'IP改编')]/../following-sibling::div//label[text()='否']"}
points['IP_jieshao'] = {'type':'xpath','locator':"//*[contains(text(),'改编IP介绍')]/../following-sibling::div//input"}     # 改编IP介绍
points['IP_sqzhengming'] = {'type':'xpath','locator':"//*[contains(text(),'授权证明')]/../following-sibling::div//input"}     # 改编IP授权证明
points['xm_jieshao'] = {'type':'id','locator':'movieAbstract'}                  # 项目介绍
points['xm_liangdian'] = {'type':'id','locator':'projHighlight'}                # 项目亮点
points['ds_bochu'] = {'type':'id','locator':'tvBroadcastPlatform'}              # 电视播出平台
points['dianhua'] = {'type':'id','locator':'contactPhoneNumber'}                # 联系电话
points['youxiang'] = {'type':'id','locator':'contactEmail'}                     # 邮箱
points['jinghuakandian'] = {'type':'id','locator':'watchingFocus'}              # 影片精华看点
points['doubanid'] = {'type':'id','locator':'doubanID'}                         # 豆瓣ID
points['pdf'] = {'type':'xpath','locator':'//div[contains(@class,"uploadBtn___-ZNsl")]/input'}            # PDF上传按钮
points['ipdf'] = {'type':'xpath','locator':'//div[contains(@class,"uploadBtn___2I0Uv")]/input'}            # IP 改编授权正面
points['biaoqianc'] = {'type':'xpath','locator':'//div[contains(@class,"wid___12f86")]/div'}                    # 标签框
points['biaoqian'] = {'type':'xpath','locator':'//div[contains(@class,"optionList___7vMqq")]/div/div[1]'}       # 标签
points['nr_lianxiren_name'] = {'type':'id', 'locator':'contactName'}
points['nr_lianxiren_adress'] = {'type':'id', 'locator':'contactAddress'}

# 备案信息
points['wlj_sxba'] = {'type':'xpath','locator':'//label[contains(text(),"有上线备案号但总局未审")]'}#网络剧专用 上线备案
points['wu_beian'] = {'type':'xpath','locator':"//*[contains(text(),'状态')]/../following-sibling::div//label[contains(text(),'无备案')]"}

points['beianhao'] = {'type':'xpath','locator':"//*[contains(text(),'备案号')]/../following-sibling::div//input"}                 # 备案号
points['xuke_z_hao'] = {'type':'xpath','locator':"//*[contains(text(),'许可证号')]/../following-sibling::div//input"}  # 备案文件
points['cpf'] = {'type':'id','locator':'executiveProduceSide.0.name'}           # 出品方
points['lhcpf'] = {'type':'id','locator':'cooperatedProduceSide.0.name'}        # 联合出品方
points['fxf'] = {'type':'id','locator':'publisher.0.name'}                      # 发行方
points['zpf'] = {'type':'id','locator':'producer.0'}                            #制片方
points['dx_radio'] = {'type':'xpath','locator':'//div[contains(@class,"radioContainer___iEXTe")]/div[1]'}       # 所有radio

# 样片 图片
points['xyb_btn'] = {'type':'xpath','locator':'//button[contains(text(),"下一步")]'}                  # 下一步按钮
points['yp_xy'] = {'type':'xpath','locator':"//*[contains(text(),'并同意')]"}               # 样片协议
points['yp_sc'] = {'type':'xpath','locator':'//*[contains(text(),"上传视频")]'}                      # 上传样片按钮
points['yp_sc_sucess'] = {'type':'xpath','locator':"//*[text()='上传成功']"}
points['haibao_heng'] = {'type':'xpath','locator':"//*[contains(text(),'横版')]/../../input"}    # 海报图
points['haibao_shu'] = {'type':'xpath','locator':"//*[contains(text(),'竖版')]/../../input"}    # 海报图
points['juzhao'] = {'type':'xpath','locator':'//*[contains(text(),"上传图片")]'}                       # 剧照
points['jz_tc'] = {'type':'xpath','locator':"//button[text()='上传']"}                 # 弹窗
points['qr_btn'] = {'type':'xpath','locator':'//button[contains(text(),"确定")]'}

points['xm_bccg'] = {'type':'xpath','locator':'//button[contains(text(),"保存草稿")]'}
points['by_yl'] = {'type':'xpath','locator':'//button[contains(text(),"保存并预览")]'}
points['tijiao'] = {'type':'xpath','locator':'//button[contains(text(),"提交")]'}




points[''] = {'type':'id','locator':''}
points[''] = {'type':'id','locator':''}
points[''] = {'type':'id','locator':''}
points[''] = {'type':'id','locator':''}


