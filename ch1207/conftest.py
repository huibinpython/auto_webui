from typing import List

import pytest


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# 笛卡尔积参数
@pytest.mark.parametrize('a',[1,2,3,4],ids=['变量a=1', '变量a=2', '变量a=3', '变量a=4'])
@pytest.mark.parametrize('b',['a','b','c','d'],ids=['变量b=a', '变量b=b', '变量b=c', '变量b=d'])
def test_dikaer(a,b):
    print(f'变量1{a}，变量2{b}')