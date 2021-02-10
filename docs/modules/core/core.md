# `core`

:octicons-file-code-24: 开源 ·
:octicons-issue-opened-24: 强制

**`core`** 模块是小可最基础的模块。此模块集可以让你启用或禁用模块、查看帮助以及使用管理员设置。

## `help`
:octicons-reply-24: 一分钟后撤回 ·
:octicons-unlock-24: 公开 ·
:octicons-issue-opened-24: 强制

使用此指令会得到所有或选定的指令以及其对应的帮助信息。

用法：`~help [<指令>]`

!!! example "示例帮助信息"
    这是一份开启全部模块后得到的帮助信息。
    ```
    基础命令：
    enable | disable | ping
    模块扩展命令：
    wiki | wiki_start_site | interwiki | wiki_regex | wiki_infobox | wiki_fandom_addon | wiki_gamepedia_addon | user | bug | bug_regex | mcv_rss | mcv_jira_rss | server | mcv | mcbv | mcdv | b30 | rc | ab | newbie
    使用~help <对应模块名>查看详细信息。
    [本消息将在一分钟后撤回]
    ```

## `modules`
:octicons-reply-24: 一分钟后撤回 ·
:octicons-unlock-24: 公开

使用此命令来查看所有模块及其功能。

用法：`~modules [<指令>]`

!!! example "所有模块"
    这是一份使用此命令后返回的信息。
    ```
    当前可用的模块有：
    wiki | wiki_start_site | interwiki | wiki_regex | wiki_infobox | wiki_fandom_addon | wiki_gamepedia_addon | user | bug | bug_regex | mcv_rss | mcv_jira_rss | server | mcv | mcbv | mcdv | enable | disable | module | b30 | rc | ab | newbie | ping
    使用~help <模块名>查看详细信息。
    [本消息将在一分钟后撤回]
    ```
