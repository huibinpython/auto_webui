import sys

import pytest


@pytest.mark.skip
def test_skip_case1():
    print('这里是方法：test_skip_case1')

# 跳过执行，并给出跳过的原因
@pytest.mark.skip(reason='代码未实现')
def test_skip_case1():
    print('这里是方法：test_skip_case1')

def check_login():
    return False

def test_skip_case2():
    print('开始执行测试用例')
    if  check_login():
        # if 未真 则跳过执行
        pytest.skip('跳过执行此用例')
    print('结束执行')

# 满足某个条件就会跳过 执行
@pytest.mark.skipif(sys.version_info<(3,8),reason='python 版本小于3.8')
def test_skipif_case1():
    print('python 版本小于 3.8执行此用例')


# 执行成功标识，xpath,执行失败，标识xFail
@pytest.mark.xfail
def test_xfail_case1():
    assert 2==2
    print('执行xfail 方法')


xfail = pytest.mark.xfail
@xfail(reason='bug  xxxx')
def test_xfail_case2():
    print('执行xfial_case2')
    assert 1==2