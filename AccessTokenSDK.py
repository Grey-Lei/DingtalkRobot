# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import json
import sys

from typing import List

from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkoauth2_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoauth2_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key='ding5uvywdvb1ncedb7v',
            app_secret='_oNkE0RstwQOx8-CuhVbhkdxOjQflfz8gZJLGtHz9PalR2z58Vb5oaH7lvdvYWp8'
        )
        try:
            resp = client.get_access_token(get_access_token_request)
            print('resp:%s' % resp)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key='ding5uvywdvb1ncedb7v',
            app_secret='_oNkE0RstwQOx8-CuhVbhkdxOjQflfz8gZJLGtHz9PalR2z58Vb5oaH7lvdvYWp8'
        )
        try:
            await client.get_access_token_async(get_access_token_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass


if __name__ == '__main__':
    Sample.main(sys.argv[1:])



