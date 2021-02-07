# `core`

:octicons-file-code-24: 开源 ·
:octicons-issue-opened-24: 强制

**`core`** 模块是小可最基础的模块。此模块集可以让你启用或禁用模块、查看帮助以及使用管理员设置。

## `help`
:octicons-reply-24: 一分钟后撤回 ·
:octicons-unlock-24: 公开 ·
:octicons-issue-opened-24: 强制

使用此指令会得到所有或选定的指令以及其对应的帮助信息。

用法：`help [<指令>]`

!!! example "示例帮助信息"
    这是一份开启全部模块后得到的帮助信息。
    ```
    基础命令：
    ~enable <模块名> - 开启一个模块
    ~disable <模块名> - 关闭一个模块
    ~ping - PongPongPong
    模块扩展命令：
    wiki：查询Wiki内容。
    wiki_start_site：设置起始查询Wiki。
    interwiki：设置自定义Interwiki。
    wiki_regex：启用正则Wikitext查询。
    wiki_infobox：当被查询的页面包含Infobox时自动提取并渲染为图片发送。
    Infobox渲染已开启：当被查询的页面包含Infobox时自动提取并渲染为图片发送。（群聊默认开启且不可全局关闭，个人可使用~disable self wiki_infobox关闭）
    wiki_fandom_addon：启用为Fandom定制的Wiki查询功能。（仅群聊）
    wiki_gamepedia_addon：启用为Gamepedia定制的Wiki查询功能。（仅群聊）
    user：获取一个Gamepedia用户的信息。
    bug：查询Mojira上的漏洞编号。
    bug_regex：正则自动查询Mojira上的漏洞编号。
    mcv_rss：订阅Minecraft Java版游戏版本检测。（仅群聊）
    mcv_jira_rss：订阅Minecraft Java版游戏版本检测（Jira记录，仅作预览用）。（仅群聊）
    server：获取Minecraft Java/基岩版服务器motd。
    mcv：查询当前Minecraft Java版启动器内最新版本。
    mcbv：查询当前Minecraft基岩版Jira上记录的最新版本。
    mcdv：查询当前Minecraft Dungeons Jira上记录的最新版本。
    b30：查询Arcaea B30结果。
    rc：查询Wiki最近更改。
    ab：查询Wiki滥用过滤器日志。
    newbie：查询Wiki用户注册日志。
    使用~help <模块名>查看详细信息。
    [本消息将在一分钟后撤回]
    ```

## `modules`
:octicons-reply-24: 一分钟后撤回 ·
:octicons-unlock-24: 公开

使用此命令来查看所有模块及其功能。

!!! example "所有模块"
    这是一份使用此命令后返回的信息。
    ```
    当前可用的模块有：
    wiki：查询Wiki内容。
    wiki_start_site：设置起始查询Wiki。
    interwiki：设置自定义Interwiki。
    wiki_regex：启用正则Wikitext查询。
    wiki_infobox：当被查询的页面包含Infobox时自动提取并渲染为图片发送。
    wiki_fandom_addon：启用为Fandom定制的Wiki查询功能。（仅群聊）
    wiki_gamepedia_addon：启用为Gamepedia定制的Wiki查询功能。（仅群聊）
    user：获取一个Gamepedia用户的信息。
    bug：查询Mojira上的漏洞编号。
    bug_regex：正则自动查询Mojira上的漏洞编号。
    mcv_rss：订阅Minecraft Java版游戏版本检测。（仅群聊）
    mcv_jira_rss：订阅Minecraft Java版游戏版本检测（Jira记录，仅作预览用）。（仅群聊）
    server：获取Minecraft Java/基岩版服务器motd。
    mcv：查询当前Minecraft Java版启动器内最新版本。
    mcbv：查询当前Minecraft基岩版Jira上记录的最新版本。
    mcdv：查询当前Minecraft Dungeons Jira上记录的最新版本。
    enable：开启一个模块
    disable：关闭一个模块
    b30：查询Arcaea B30结果。
    rc：查询Wiki最近更改。
    ab：查询Wiki滥用过滤器日志。
    newbie：查询Wiki用户注册日志。
    ping：Pong
    使用~help <模块名>查看详细信息。
    [本消息将在一分钟后撤回]
    ```
