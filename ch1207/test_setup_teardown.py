# 测试装置
# setup_module/teardown_module   执行模块前后分别调用此方法
# setup_class/teardown_class 执行类前后调用
# setup_function/teardown_function   执行类外面的函数，调用
# setup_method/teardown_method 执行类内的方法，调用
# setup/teardonw  在类中，运行调用方法的前后调用（作用同上）\

# 模块级别
import pytest


def setup_module():
    print('开始测试：模块执行前调用此方法：setup_module')

def teardown_module():
    print('开始测试：模块执行完后调用此方法：teardown_module')

def test_case1():
    print('开始测试：类外面的方法：case1')
def test_case2():
    print('开始测试：类外面的方法：case2')

def setup_function():
    print('开始测试：执行类外面的方法前调用：setup_function')

def teardown_function():
    print('开始测试：执行类外面的方法后调用：teardown_function')
#
class TestDemo:
    def setup_class(self):
        print('开始测试：类执行前调用：setup_class')

    def teardown_class(self):
        print('开始测试：类执行后调用：teardown_class')

    def setup(self):
        print('开始测试：类里面的方法执行前调用：setup')

    def teardown(self):
        print('开始测试：类里面的方法执行后调用：teardown')

    def test_class_dmeo1(self):
        print('开始测试，类里面的方法：test_class_demo1')

    def test_class_dmeo2(self):
        print('开始测试，类里面的方法：test_class_demo2')

class TestDemo2:
    def setup_class1(self):
        print('开始测试：类执行前调用：setup_class1')

    def teardown_class(self):
        print('开始测试：类执行后调用：teardown_class1')

    def setup(self):
        print('开始测试：类里面的方法执行前调用：setup1')

    def teardown(self):
        print('开始测试：类里面的方法执行后调用：teardown1')

    def test_class1_dmeo1(self):
        print('开始测试，类里面的方法：test_class1_demo1')

    @pytest.mark.skip
    def test_class1_dmeo2(self):
        print('开始测试，类里面的方法：test_class1_demo2')

    @pytest.mark.dd
    def test_case111(self):
        print('测试用例1')

    @pytest.mark.dd
    def test_case222(self):
        print('测试用例1')

    @pytest.mark.skip
    def test_case333(self):
        print('测试用例1')