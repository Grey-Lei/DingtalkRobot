import json
import requests
# import config
from config import *


def once_called(func):
    '''函数只调用一次，二次调用时，返回首次调用时的返回值'''
    is_called = False
    result = None

    def wrapper(*args, **kwargs):
        nonlocal is_called, result
        if not is_called:
            result = func(*args, **kwargs)
            is_called = True
        return result

    return wrapper


class DingTalkDoc:
    """获取钉钉文档类"""
    def __init__(self):
        self.headers = {"Host": "api.dingtalk.com", "Content-Type": "application/json"}
        # self.headers = {"Host": "api.dingtalk.com", "Content-Type": "application/json", "x-acs-dingtalk-access-token": "14649578ac8d36dd9cae57a14a8aad41"}

    @staticmethod
    def send_requests(method, url, data=None, headers=None, params=None):
        """发动requests请求"""
        data = json.dumps(data) if data else data
        resp = requests.request(method=method, url=url, data=data, headers=headers, params=params)
        # print(resp.text)
        # print(type(resp))
        return json.loads(resp.text)

    def get_access_token(self):
        """获取accessToken"""
        # POST /v1.0/oauth2/accessToken
        data = {
            "appKey": appKey,
            "appSecret": appSecret
        }
        resp = DingTalkDoc.send_requests("post", ak_url, data=data, headers=self.headers)
        accessToken = resp["accessToken"]
        print("accessToken: %s" % accessToken)
        self.headers["x-acs-dingtalk-access-token"] = accessToken

    @once_called
    def get_space_id(self):
        """获取指定space的spaceId"""
        # GET /v1.0/doc/workspaces?operatorId=String&includeRecent=Boolean
        params = {
            "operatorId": self.get_operator_id,
            # "operatorId": "pMwTvN3Z2OrUhIPDR79TNwiEiE",
            "includeRecent": False
        }
        resp = DingTalkDoc.send_requests('get', space_url, headers=self.headers, params=params)
        workspace_list = resp.get("workspaces")

        workspaceId = None
        for i in workspace_list:
            if i.get("name") == space_name:
                print("workspaceId: %s" % i.get("workspaceId"))
                workspaceId = i.get("workspaceId")
        return workspaceId

    @property
    @once_called
    def get_operator_id(self):
        """获取operatorId,企业内部应用，调用查询用户详情接口获取unionid参数值"""
        # post https://oapi.dingtalk.com/topapi/v2/user/get?access_token=ACCESS_TOKEN
        data = {
            "userid": userid,
            "language": language
        }
        params = {"access_token": self.headers.get("x-acs-dingtalk-access-token")}
        resp = DingTalkDoc.send_requests("post", operator_url, data=data, params=params)
        operatorId = resp.get("result").get("unionid")
        print("operator: %s" % operatorId)
        return operatorId

    def get_dentry_id(self, dentryid=None):
        """获取dentryId"""
        # GET /v2.0/doc/spaces/{spaceId}/directories?dentryId=String&operatorId=String&nextToken=String&maxResults=Integer
        params = {
            "operatorId": self.get_operator_id,
            # "operatorId": "pMwTvN3Z2OrUhIPDR79TNwiEiE",
            "maxResults": maxResults,
            # "dentryId": "r98zndQPoDkgLmLx"
            "dentryId": dentryid
        }
        resp = DingTalkDoc.send_requests('get', dentry_url.format(self.get_space_id()), headers=self.headers, params=params)
        # resp = DingTalkDoc.send_requests('get', dentry_url.format("r98zne6Jdn0naGLx"), headers=self.headers, params=params)
        return resp

    def main(self):
        """获取知识库下指定目录列表"""
        # 获取授权access_token,并设置到headers中
        self.get_access_token()
        # 获取dentryId
        resp = self.get_dentry_id()
        # 获取指定目录的dentryID
        dentryId = str()
        for i in resp.get("children"):
            if i.get("name") == dir_name:
                dentryId = i.get("dentryId")
        print("dentryId: %s" % dentryId)
        # 发送请求，获取指定目录下文档列表
        resp = self.get_dentry_id(dentryId)
        # 获取指定目录下最新工作表
        doc_info_list = resp.get("children")
        # 假设url地址为列表第一个元素的url值
        last_doc_url = doc_info_list[0].get("url")
        # 假设列表第一个createTime为最大值
        last_doc = int(doc_info_list[0].get("createdTime"))
        # 获取最新创建的文档连接
        for i in doc_info_list:
            if int(i.get("createdTime")) > last_doc:
                last_doc_url = i.get("url")
        return last_doc_url


obj = DingTalkDoc()


if __name__ == '__main__':
    obj = DingTalkDoc()
    # obj.get_access_token()  # 14649578ac8d36dd9cae57a14a8aad41
    # obj.get_operator_id     # pMwTvN3Z2OrUhIPDR79TNwiEiE
    # obj.get_space_id("一个云测试")      # r98zne6Jdn0naGLx(一个云测试)
    # obj.get_dentry_id()     # r98zndQPoDkgLmLx(测试用例库)  # r98zndQ9oEnPvmLx(工作计划)
    # dir_name = "工作计划"
    obj.main()
