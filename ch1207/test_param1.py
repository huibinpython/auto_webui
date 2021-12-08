import pytest

search_list = ['java', 'C#', 'go']


# 单参数
@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list


# 参数化传入多个参数
# 需注意，参数化的名字需要同  方法参数名一致
# 传入多组参数，使用列表传入，参数用列表、或元祖的方式传入
# 给方法命名，使用ids，ids 参数个数和 参数数量一致
@pytest.mark.parametrize('test,expected', [('3+5', 8), ('1+9', 10), ('2+5', 7), ('7+9', 16)],
                         ids=['测试1', '测试2', '测试3', '测试4'])
def test_mark_more(test, expected):
    # eval 把字符串转换成 表达式
    assert eval(test) == expected


# 笛卡尔积参数
@pytest.mark.parametrize('a',[1,2,3,4],ids=['变量a=1', '变量a=2', '变量a=3', '变量a=4'])
@pytest.mark.parametrize('b',['a','b','c','d'],ids=['变量b=a', '变量b=b', '变量b=c', '变量b=d'])
def test_dikaer(a,b):
    print(f'变量1{a}，变量2{b}')