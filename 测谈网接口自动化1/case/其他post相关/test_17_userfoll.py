import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
import utils.gettoken as to
import utils.getid as ge

@de.prt
@de.posturl("关注取消关注接口",0)
def test_01_fellfollowtype0_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "关注成功！"#先关注
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消关注成功！"#再取消关注
    return res

@de.prt
@de.posturl("关注取消关注接口",1)
def test_02_fellfollowtype1_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "关注成功！"#先关注
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消关注成功！"#再取消关注
    return res

@de.prt
@de.posturl("关注取消关注接口",2)
def test_03_fellfollowtype3_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "关注成功！"#先关注
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消关注成功！"#再取消关注
    return res

@de.prt
@de.posturl("关注取消关注接口",3)
def test_05_fellfollowtypenull_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该ctype类型"
    return res

@de.prt
@de.posturl("关注取消关注接口",4)
def test_06_fellfollowtypewrong_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该ctype类型"
    return res

@de.prt
@de.posturl("关注取消关注接口",5)
def test_07_fellfollowtype0notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该教程"
    return res

@de.prt
@de.posturl("关注取消关注接口",6)
def test_08_fellfollowtype1notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该问题"
    return res

@de.prt
@de.posturl("关注取消关注接口",7)
def test_09_fellfollowtype3notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该文章"
    return res

