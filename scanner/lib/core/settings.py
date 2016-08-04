#!/usr/bin/env python
#-*-encoding:UTF-8-*-

import os

################## mysql setting ##################
MYSQL_HOST = "xxxxxx"
MYSQL_PORT = 3306
MYSQL_USERNAME = "test"
MYSQL_PASSWD = "test"
MYSQL_DATABASE = "kehan"

################## rule setting ##################
TASK_TABLE = 'task'           #任务表名
RULE_TABLE = "rule"           #规则表名
URL_TABLE = "url"
RESULT_TABLE = "result"
RUN_URL_DEFAULT_FUN = "run_url"
RUN_DOMAIN_DEFAULT_FUN = "run_domain"

################## path setting ##################
SCRIPTS_NAME = "scripts"     #规则目录
SCRIPTS_DIC_NAME = "dic" #字典目录
#TEMP_NAME = "temp"  #缓存文件
TEMP_NAME = "temp"
LOG_NAME = "toplog.log"

################## gloabl default setting ##################
DEFAULT_PAGE_ENCODING = "utf8"
HEADER_BODY_BOUNDRY = ""

################## cmdline default setting ##################
# may change by cmdline
CONNECTION_TIMEOUT = 10
NETWORK_TIMEOUT = 10

################## crawler default setting ##################
IGNORE_DEFAULT_FILE_SUFFIX = ('jpg','png','jpeg','png','jpg','gif','bmp','svg',
                            'exe','rar','zip',
                            'js','css')


################## dic name setting ##################
WEBSHELL_DIC_NAME = "web_shell.dic"

