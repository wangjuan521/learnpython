*** Settings ***
# setting用于导入相关的库
Library  Selenium2Library
Library  connetsql.py
# Resource
Test Setup  #每个测试用例前置
Test Teardown  #每个测试用例后置
Suite Setup    #每个用例集的前置操作
Suite Teardown  #每个用例集的后置操作
*** Test Cases ***
testclass01 #用例1
    log    hello word
    search
    connet_sql
testclass02 #用例2
    log    hello word


*** Keywords ***
search
    [Documentation]  注释，封装一个关键字,搜索功能
    open browser    ${url}   chrome
    input text    xpath=//input[@id="kw"]   python
    sleep     3
    click element    xpath=//input[@id="su"]





*** Variables ***
${url}   https://www.baidu.com