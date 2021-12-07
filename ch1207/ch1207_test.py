# 类里面的是方法，类外面的是函数
# 命名规范
# 文件：test_ 开头，或_test结尾
# 类 Test开头
# 方法或函数，test_开头
# 测试类中不可添加_init_构造函数

def inc(x):
    return x +1

def test_answer():
    print('fawefawe')
    assert inc(3) == 5

# 执行文件里某一个类：pytest ch1207_test.py::TestDemo
# 执行文件里类的某一个方法：pytest ch1207_test.py::TestDemo::test_demo2 -v
# 加 -v 会显示执行的用例
class TestDemo:
    def test_demo1(self):
        print('这里是demo  方法1')
    def test_demo2(self):
        print('这里是demo  方法2')

