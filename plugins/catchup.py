"""
Catchup 插件 - 关键词触发回复
触发方式: 在群组中发送 /关键词
"""

import contextlib
import json
import random
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


# 模板数据
TEMPLATES_DATA = {
    "templates": [
        # 单人模板
        {"id": 1, "mode": "single", "content": "{name} 正在看着你"},
        {"id": 2, "mode": "single", "content": "{name} 收到了一条神秘消息"},
        {"id": 3, "mode": "single", "content": "有人在呼唤 {name}"},
        {"id": 4, "mode": "single", "content": "{name} 的名字被提及了"},
        {"id": 5, "mode": "single", "content": "{name} 突然感觉背后一凉"},
        # 双人模板
        {"id": 101, "mode": "dual", "content": "{trigger_user} 向 {target_user} 发送了信号"},
        {"id": 102, "mode": "dual", "content": "{trigger_user} 正在寻找 {target_user}"},
        {"id": 103, "mode": "dual", "content": "{target_user} 收到 {trigger_user} 的消息"},
        {"id": 104, "mode": "dual", "content": "{trigger_user} 呼唤了 {target_user}"},
        {"id": 105, "mode": "dual", "content": "{trigger_user} 对 {target_user} 说：在吗"},
    ]
}


class TemplateGenerator:
    """模板生成器"""

    def __init__(self):
        self.single_templates: List[str] = []
        self.dual_templates: List[str] = []
        self.load_templates()

    def load_templates(self):
        """加载模板"""
        for template in TEMPLATES_DATA["templates"]:
            if template["mode"] == "single":
                self.single_templates.append(template["content"])
            else:
                self.dual_templates.append(template["content"])
        logs.info(f"已加载 {len(self.single_templates)} 个单人模板和 {len(self.dual_templates)} 个双人模板")

    def generate_single(self, name: str) -> str:
        """生成单人回复"""
        if not self.single_templates:
            return f"{name} 收到了消息"
        template = random.choice(self.single_templates)
        return template.replace("{name}", name).replace("{target_user}", name)

    def generate_dual(self, trigger_user: str, target_user: str) -> str:
        """生成双人回复"""
        if not self.dual_templates:
            return f"{trigger_user} 向 {target_user} 发送了消息"
        template = random.choice(self.dual_templates)
        return template.replace("{trigger_user}", trigger_user).replace("{target_user}", target_user)
