# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "MiharoCo/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "MiharoNico Wiki"
site_logo = "${static_prefix}gugusanyuan.jpg"
site_build_date = "2019-12-18T16:51+08:00"
author = "MiharoNico"
email = "admin@咕咕三原.wang"
author_homepage = "https://咕咕三原.wang"
description = "记录美好，赠与未来。"
key_words = ['Maverick', '咕咕三原',  'wiki']
language = 'zh-CN'
template="Kepler"
external_links = [
    {
        "name": "Blog",
        "url": "https://咕咕三原.wang",
        "brief": "MiharoNico Blog."
    },
    {
        "name": "Diary",
        "url": "https://diary.咕咕三原.wang",
        "brief": "MiharoNico Diary"
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/MiharoCo",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/MiharoCo",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/6339337866/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
