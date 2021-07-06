#coding=utf-8
#@time   :2021/6/2  11:15
#@Author :wangjuan
import pytest
if __name__ == '__main__':
    # 运行指定的文件
    pytest.main(['-s','-v','./pytest_case','--html=./Reports/report.html'])


