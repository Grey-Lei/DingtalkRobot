# -*- coding: utf-8 -*-

import time
import hmac
import json
import hashlib
import base64
import requests
import urllib.parse

# https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2&timestamp=XXX&sign=9qTr5VQ4f66zl%2FT1pfRvOg7IvIBNckzBgT%2BflKkfLKY%3D
# curl 'https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2&timestamp=1684912413186&sign=9qTr5VQ4f66zl%2FT1pfRvOg7IvIBNckzBgT%2BflKkfLKY%3D' -H 'Content-Type: application/json' -d '{"msgtype": "text","text": {"content":"我就是我, 是不一样的烟火"}}'

# headers={"Content-Type":"application/json;charset=UTF-8"}


class DingTalkBot:
    '''dingtalk 机器人类'''
    msgtype = "text"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    atMobiles = ["17538571127", ]
    atUserIds = []
    isAtAll = True
    verify = False

    def __init__(self, webhook, secret_key):
        self.webhook = webhook
        self.secret_key = secret_key

    def generate_url(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret_key.encode("utf-8")
        string_to_sign = '{}\n{}'.format(timestamp, self.secret_key)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = self.webhook + '&timestamp=' + timestamp + '&sign=' + sign
        return url

    def send_text(self, content):
        '''发送文本消息'''
        msg_body = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                # "atMobiles": self.atMobiles,
                # "atUserIds": self.atUserIds,
                "isAtAll": self.isAtAll
            }
        }
        try:
            res = requests.post(self.generate_url(), data=json.dumps(msg_body), headers=self.headers, verify=True)
            return res
        except Exception as e:
            return {"errmsg": repr(e)}

    def send_link(self):
        '''发送link类型消息'''
        msg_body = {
            "msgtype": "link",
            "link": {
                "text": "[test]link类型消息发送",
                "title": "新人学习手册",
                "picUrl": "",
                # "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "messageUrl": "https://alidocs.dingtalk.com/i/nodes/kDnRL6jAJMKbpEwbs1k1Gy9AWyMoPYe1"
            },
            "at": {
                # "atMobiles": self.atMobiles,
                # "atUserIds": self.atUserIds,
                "isAtAll": self.isAtAll
            }
        }
        try:
            res = requests.post(self.generate_url(), data=json.dumps(msg_body), headers=self.headers, verify=True)
            return res
        except Exception as e:
            return {"errmsg": repr(e)}

    def send_markdown(self):
        '''发送markdown类型消息'''
        msg_body = {
            "msgtype": "markdown",
            "markdown": {
             "title": "工作任务",
             "text": "#### 工作任务 \n > 本周任务计划测试\n > ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点30分发布 [工作项](https://alidocs.dingtalk.com/i/nodes/kDnRL6jAJMKbpEwbs1k1Gy9AWyMoPYe1) \n"
            },
            "at": {
                # "atMobiles": self.atMobiles,
                # "atUserIds": self.atUserIds,
                "isAtAll": self.isAtAll
            }
        }
        try:
            res = requests.post(self.generate_url(), data=json.dumps(msg_body), headers=self.headers, verify=True)
            return res
        except Exception as e:
            return {"errmsg": repr(e)}

    def send_action_card(self):
        '''发送action_card类型消息'''
        msg_body = {
            "actionCard": {
                "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
                "text": "![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png) \n ### 乔布斯 20 年前想打造的苹果咖啡厅 \n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
                "btnOrientation": "0",
                "singleTitle": "阅读全文",
                "singleURL": "https://alidocs.dingtalk.com/i/nodes/kDnRL6jAJMKbpEwbs1k1Gy9AWyMoPYe1"
            },
            "msgtype": "actionCard",
            "at": {
                # "atMobiles": self.atMobiles,
                # "atUserIds": self.atUserIds,
                "isAtAll": self.isAtAll
            }
        }
        try:
            res = requests.post(self.generate_url(), data=json.dumps(msg_body), headers=self.headers, verify=True)
            return res
        except Exception as e:
            return {"errmsg": repr(e)}


if __name__ == '__main__':
    url = "https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2"
    content = "我就是我，是颜色不一样的烟火--python请求"
    secret = 'SEC762bd9e547c7756e13a0330426bd2696c14d1de6ea1dc0e566c4c0b9efccd0e7'

    obj = DingTalkBot(url, secret)
    # print(obj.send_text(content))
    print(obj.send_link())
    # print(obj.send_markdown())
    # print(obj.send_action_card())



