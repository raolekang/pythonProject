import time
import unittest

from selenium.webdriver.common.by import By

from DXWeb.pageObject.apiApplyAimUrl import ApiApplyAimUrl
from DXWeb.pageObject.login import Login
from DXWeb.pageObject.searchTemplate import SearchTemplate
from DXWeb.pageObject.createTemplate import CreateTemplate
from DXWeb.pageObject.tmpCheckAndActive import TemplateCheckActive
from selenium import webdriver
from DXWeb.data.read_write_relevance import  YamlUtil
import pytest
from DXWeb.data.read_data import ReadYaml

class TestDXWeb():


    #登录EC
    @pytest.mark.parametrize("data",ReadYaml().readYamlFile(file='../data/data.yaml'))
    def test_login(self,data,manage_brower):
        self.loginPage = Login(manage_brower)
        self.loginPage.login(ecUrl=data["ecUrl"],ecUserName=data["ecAccount"], ecPassWord=data["ecPwd"],osUrl=data["osUrl"], osUserName=data["osAccount"], osPassWord=data["osPwd"])
        assert  "cszh0120" in self.loginPage.getAssertValue()

    #创建模板
    def test_createTemplate(self,manage_brower):
        createTemp= CreateTemplate(manage_brower)
        createTemp.create_template()

    # 查询模板
    def test_searchTemplate(self,manage_brower):
        # print("读取relevance.yaml文件中的数据",newTplId)
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId") #使用封装的方法读取
        searchTempObject = SearchTemplate(manage_brower)
        searchTempObject.search_template(tmpId)

    #模板审核激活
    def test_templateCheckActive(self,manage_brower):
        tmpCheckActive = TemplateCheckActive(manage_brower)
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        tmpCheckActive.tmpCheckActive(tmpId=tmpId)

    # 申请短链
    def test_apiApplyAimUrl(self,manage_brower):
        templateId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        print("templateId:", templateId)
        apiApplyAimUrl = ApiApplyAimUrl(manage_brower)
        apiApplyAimUrl.apiApplyAimUrl(templateId)

if __name__ == '__main__':
    pytest.main(['-vs'])