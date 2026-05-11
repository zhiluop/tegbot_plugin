# PagerMaid-Pyro 插件集合

本仓库包含 PagerMaid-Pyro Telegram 人形机器人的自定义插件。

## 开发者

本项目所有插件由 **Vibe Coding** 全权开发。

## 快速开始

### 使用 apt_source 安装（推荐）

在 PagerMaid-Pyro 中添加插件源：

```
,apt_source add https://raw.githubusercontent.com/zhiluop/tegbot_plugin/main/
```

> **重要**: URL 末尾必须带 `/`，否则无法正常获取插件列表。

安装插件：

```
,apt install <插件名>
```

可用插件：
- `cai` - 自动点踩插件
- `euth` - 共享 bot 队列的 inline 自动签到/每日老婆助手
- `fudu` - 随机自动复读插件（支持每日目标）
- `gi2` - 图片生成与改图插件（支持直接生图、回复图片改图、GI2 结果图原地继续编辑）
- `jpm` - 关键词触发回复插件
- `jpmai` - AI 生成艳情文案插件
- `ais` - AI 查询插件（支持联网搜索增强、参考网址追加、实体查询图片预览与 API URL/base url 快速切换）
- `minimaximg` - MiniMax 生图插件（输入 `,mmimg <提示词>` 直接生图，并同步附带 Prompt、比例、尺寸和模型信息）
- `pixivshow` - Pixiv 美少女推图插件（支持普通图 / R18 / 数量控制）
- `qunshui` - 群水助手插件（指定群组进度统计、AI 群聊、自动接话、今日收工与风险拦截）
- `redpack` - 口令红包插件（默认文字红包，支持 `img` 数学题图片口令、内置字体资源和自动结算榜单）
- `get_reactions` - 表情获取辅助命令
- `share_plugins` - 分享插件
- `sfl` - 贴纸跟随插件
- `sar` - 贴纸自动回复插件
- `luckydraw` - 自动抽奖插件（支持中奖庆祝贴纸）

### 手动安装

1. 下载插件文件夹
2. 将插件文件夹复制到 PagerMaid-Pyro 的 `plugins/` 目录
3. 重新加载插件：`,reload` 或 `/reload`
4. 查看插件帮助：`,<插件名>`

## 插件列表

| 插件 | 说明 | 文档 |
|------|------|------|
| CAI | 自动点踩插件 - 自动对目标用户的发言进行点踩 | [cai/DES.md](./cai/DES.md) |
| EUTH | Inline Bot 自动助手 - 支持共享 bot 队列的定时签到、定时刷新每日老婆图片、目标聊天绑定与标题匹配 | [docs/euth.md](./docs/euth.md) |
| FuDu | 随机自动复读插件 - 支持群组独立开关、复读概率、冷却时间与每日目标控制，复读时直接发送普通消息 | [docs/fudu.md](./docs/fudu.md) |
| GI2 | 图片生成与改图插件 - 支持 `,gi2 <提示词>` 直接生图、回复照片/图片文档/静态贴纸改图，以及对 GI2 自己发出的结果图原地继续编辑 | [gi2/DES.md](./gi2/DES.md) |
| JPM | 关键词触发回复插件 - 支持多关键词、频率限制、锚点消息系统 | [jpm/DES.md](./jpm/DES.md) |
| JPMAI | AI 生成艳情文案插件 - 调用 AI 模型实时生成仿明清艳情小说风格的回复，支持仅主人触发模式、完整 API URL 兼容与连通性测试 | [jpmai/DES.md](./jpmai/DES.md) |
| AIS | AI 查询插件 - 支持 OpenAI 格式 API、自定义模型切换、API URL/base url 快速切换、MCP 工具接入，以及由模型决策是否联网搜索、自动附参考网址并补发实体图片预览的增强问答 | [docs/ais.md](./docs/ais.md) |
| MiniMaxImg | MiniMax 生图插件 - 输入 `,mmimg <提示词>` 直接调用 MiniMax Image-01 生成图片，发送时同步附带 Prompt、比例、尺寸和模型信息 | [docs/minimaximg.md](./docs/minimaximg.md) |
| PixivShow | Pixiv 美少女推图插件 - 支持普通图、R18 图、Telegram 原生遮罩与单次推送数量控制 | [docs/pixivshow.md](./docs/pixivshow.md) |
| QunShui | 群水助手插件 - 支持指定群组的每日发言计数、目标进度查看、最近 10 条上下文 AI 群聊回复、自动接话、今日收工与高风险诱导消息拦截 | [docs/qunshui.md](./docs/qunshui.md) |
| RedPack | 口令红包插件 - 默认发送可复制的文字红包，支持 `img` 数学题 + 图片验证码口令、自定义总额和个数，内置中文字体资源，在同一条图片消息里给出全部数学题并自动识别答案口令随机发放红包，领完后自动发送结算榜单 | [docs/redpack.md](./docs/redpack.md) |
| Get Reactions | 表情获取辅助命令 - 用于测试环境是否支持自定义表情反应 | [get_reactions/DES.md](./get_reactions/DES.md) |
| Share Plugins | 分享插件 - 将插件以文件形式分享，支持列表查看和序号选择 | [share_plugins/DES.md](./share_plugins/DES.md) |
| SFL | 贴纸跟随插件 - 在特定群组中自动跟随发送特定贴纸，管理命令自动撤回 | [sfl/DES.md](./sfl/DES.md) |
| SAR | 贴纸自动回复插件 - 当有人用贴纸回复你的消息时，自动回复相同的贴纸，管理命令自动撤回 | [sar/DES.md](./sar/DES.md) |
| LuckyDraw | 自动抽奖插件 - 在指定群组中自动识别红包/抽奖活动并发送口令参与，支持机器人白名单、群组延时与中奖庆祝贴纸 | [luckydraw/DES.md](./luckydraw/DES.md) |

## 项目结构

```
tegbot_plugin/
├── cai/                     # 自动点踩插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── euth/                    # Inline Bot 自动助手
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── fudu/                    # 随机自动复读插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── gi2/                     # 图片生成与改图插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── jpm/                     # 关键词触发回复插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── jpmai/                   # AI 生成艳情文案插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── ais/                     # AI 查询插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── minimaximg/             # MiniMax 生图插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── pixivshow/              # Pixiv 美少女推图插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── qunshui/                # 群水助手插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件简述
├── redpack/                # 口令红包插件
│   ├── main.py             # 插件主文件
│   ├── assets/             # 图片红包资源目录
│   │   └── font.ttf        # 图片口令使用的内置中文字体
│   └── DES.md              # 插件描述
├── get_reactions/           # 表情获取辅助命令
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── share_plugins/           # 分享插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── sfl/                    # 贴纸跟随插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── sar/                    # 贴纸自动回复插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── luckydraw/              # 自动抽奖插件
│   ├── main.py             # 插件主文件
│   └── DES.md              # 插件描述
├── docs/                   # 项目文档
│   ├── ais.md             # AIS 插件文档
│   ├── euth.md            # Euth Inline 助手文档
│   ├── fudu.md            # FuDu 插件文档
│   ├── minimaximg.md      # MiniMaxImg 生图插件文档
│   ├── pixivshow.md       # PixivShow 插件文档
│   ├── qunshui.md         # QunShui 插件文档
│   └── redpack.md         # RedPack 插件文档
├── list.json               # 插件列表（apt_source 使用）
├── index.html              # 插件展示页面
├── scripts/                # 维护脚本
│   └── update_list.py      # 自动更新插件列表
└── README.md               # 本文件
```

## 开发说明

本项目遵循严格的开发流程，详见 [`.claude/CLAUDE.md`](.claude/CLAUDE.md)。

### 添加新插件

1. 创建插件文件夹：`mkdir your_plugin`
2. 创建 `main.py` 文件：插件主代码
3. 创建 `DES.md` 文件：插件描述
4. 运行 `python scripts/update_list.py`：自动更新插件列表

## 许可证

MIT License
