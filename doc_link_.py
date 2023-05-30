# -*- coding: utf-8 -*-

import time
import hmac
import json
import hashlib
import base64
import requests
import urllib.parse
import AccessTokenReq
from datetime import datetime
from config import *

# https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2&timestamp=XXX&sign=9qTr5VQ4f66zl%2FT1pfRvOg7IvIBNckzBgT%2BflKkfLKY%3D
# curl 'https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2&timestamp=1684912413186&sign=9qTr5VQ4f66zl%2FT1pfRvOg7IvIBNckzBgT%2BflKkfLKY%3D' -H 'Content-Type: application/json' -d '{"msgtype": "text","text": {"content":"我就是我, 是不一样的烟火"}}'

# headers={"Content-Type":"application/json;charset=UTF-8"}


class DingTalkBot:
    '''dingtalk 机器人类'''
    msgtype = "text"
    # alidocs_url = "https://alidocs.dingtalk.com/i/nodes/NZQYprEoWoQRD0qRUeoBgY9bJ1waOeDk?iframeQuery=sheet_range%3Dkgqie6hm_0_0_1_1"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    isAtAll = True
    verify = False

    def __init__(self, webhook, secret_key):
        self.webhook = webhook
        self.secret_key = secret_key
        self.time_format = datetime.now().strftime("%H:%M")

    def generate_url(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret_key.encode("utf-8")
        string_to_sign = '{}\n{}'.format(timestamp, self.secret_key)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = self.webhook + '&timestamp=' + timestamp + '&sign=' + sign
        return url

    def send_text(self, doc_url):
        '''发送文本消息'''
        msg_body = {
            "msgtype": "text",
            "text": {
                "content": doc_url
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
                "text": "本周工作任务安排 \n同步测试同学每天工作任务及计划排表，\n每天上午11点，自动发送通知，\n团队成员需在预期时间内完成工作任务，\n特殊情况除外，如有不可抗拒因素导致延期，\n要提前报备",
                # "text": "",
                "title": "工作计划",
                # "title": "",
                "picUrl": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png",
                # "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "messageUrl": "https://alidocs.dingtalk.com/i/nodes/NZQYprEoWoQRD0qRUePl9d0pJ1waOeDk?utm_scene=team_space"
            },
            "at": {
                # "atMobiles": atMobiles,
                # "atUserIds": atUserIds,
                "isAtAll": self.isAtAll
            }
        }
        try:
            res = requests.post(self.generate_url(), data=json.dumps(msg_body), headers=self.headers, verify=True)
            return res
        except Exception as e:
            return {"errmsg": repr(e)}

    def send_markdown(self, doc_url):
        '''发送markdown类型消息'''
        msg_body = {
            "msgtype": "markdown",
            "markdown": {
             "title": "工作任务",
             # "text": "#### 工作任务 \n > 本周任务计划 \n > [![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)](%s) \n > ###### %s 发布 [工作项](%s) \n" % (doc_url, self.time_format, doc_url)
             "text": "#### 工作任务 \n > 本周任务计划 \n > [![screenshot](https://gitee.com/gyh111/username/raw/master/work.png)](%s) \n > ###### %s 发布 [工作项](%s) \n" % (doc_url, self.time_format, doc_url)
             # "text": "%s" % doc_url
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
        # 发送action_card类型消息
        msg_body = {
            "actionCard": {
                "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
                "text": "![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png) \n ### 乔布斯 20 年前想打造的苹果咖啡厅 \n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
                "btnOrientation": "0",
                "singleTitle": "阅读全文",
                "singleURL": "%s" % webhook
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
    last_doc_url = AccessTokenReq.obj.main()
    obj = DingTalkBot(webhook, secret)
    print("last_doc_url: %s" % last_doc_url)
    # print(obj.send_text(last_doc_url))
    # print(obj.send_link())
    obj.send_markdown(last_doc_url)
    # print(obj.send_action_card())



