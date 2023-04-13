#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_all_plugins
#nonebot.load_plugin("nonebot_plugin_remake")  
#已在pyproject。toml里导入
nonebot.load_plugin("nonebot_plugin_code")
nonebot.load_plugin('nonebot_plugin_picstatus')
#nonebot.load_plugin('nonebot_plugin_status')
#nonebot.load_plugin('nonebot_plugin_abbrreply')
nonebot.load_plugin('nonebot_plugin_withdraw')
nonebot.load_plugin('nonebot_plugin_biliav')
nonebot.load_plugin('nonebot_plugin_chatgpt')
nonebot.load_plugin('nonebot_plugin_exchangerate')
#nonebot.load_plugin('youthstudy')

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
