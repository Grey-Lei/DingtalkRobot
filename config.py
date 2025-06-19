"""公共变量配置文件"""

# url地址
ak_url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"  # post方式
space_url = "https://api.dingtalk.com/v1.0/doc/workspaces"  # get方式
operator_url = "https://oapi.dingtalk.com/topapi/v2/user/get"  # post方式
dentry_url = "https://oapi.dingtalk.com/v2.0/doc/spaces/{}/directories"  # get方式

# 路径参数
space_name = "一个云测试"
dir_name = "工作计划"

# 企业内部应用信息
appKey = "ding5uvywdvb1ncedb7v"
appSecret = "_oNkE0RstwQOx8-CuhVbhkdxOjQflfz8gZJLGtHz9PalR2z58Vb5oaH7lvdvYWp8"
userid = "285610060838650170"
language = "zh_CN"
maxResults = 10

# 钉钉机器人--测试工作同步群
webhook = "https://oapi.dingtalk.com/robot/send?access_token=c763c12c2060aa267e91ca61cf6d61050728c8fc9ada64d41d601d10b68b57d2"
secret = "SEC762bd9e547c7756e13a0330426bd2696c14d1de6ea1dc0e566c4c0b9efccd0e7"
atMobiles = ["17538571127", ]
atUserIds = []

# 钉钉机器人--每周工作提醒群
# webhook = "https://oapi.dingtalk.com/robot/send?access_token=ddb6e8a745b0efe683bcd46d2f582e5abc72dbbb03887aecd8f25016301135fc"
# secret = "SEC5cf2e157d10fdf09c5e4f4e475c80ba8d511874cfb945d455a9e4a459d2e50f3"
