"""
Catchup 插件 - 关键词触发回复
触发方式: 在群组中发送 /关键词
"""

import contextlib
import json
import re
import time
from pathlib import Path
from typing import Optional, Dict, List

from pagermaid.listener import listener
from pagermaid.hook import Hook
from pagermaid.enums import Message, Client
from pagermaid.utils import logs


# 配置文件路径
plugin_dir = Path(__file__).parent
config_file = plugin_dir / "catchup_config.json"
trigger_log_file = plugin_dir / "catchup_trigger_log.json"
data_file = plugin_dir / "catchup_data.json"

# 默认频率限制（秒）
DEFAULT_RATE_LIMIT = 3600


@Hook.on_startup()
async def plugin_startup():
    """插件初始化"""
    logs.info("Catchup 插件已加载")


@Hook.on_shutdown()
async def plugin_shutdown():
    """插件关闭"""
    logs.info("Catchup 插件已卸载")
