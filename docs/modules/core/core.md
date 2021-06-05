# `core`

:octicons-file-code-24: 开源 ·
:octicons-issue-opened-24: 强制

**`core`** 模块是小可最基础的模块。此模块集可以让你启用或禁用模块、查看帮助以及使用管理员设置。

## `enable` / `disable`

:octicons-lock-24: 仅管理员 ·
:octicons-issue-opened-24: 强制

用法：`~<enable|disable> [<self>] <模块名称|all>`

使用此指令以开关所有模块。

若在模块名称前加上 `self`，则此模块的开/关仅适用于此命令的运行者。

!!! seealso "另见"
    查看所有可用的模块，请见[modules](/modules/core/core/#modules)。

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

## `version`

:octicons-unlock-24: 公开 ·
:octicons-issue-opened-24: 强制

用法：`~version`

获得目前机器人运行的软件版本。应该是一个 Git commit hash 的前六位。

## `add_base_su`

:octicons-lock-24: 仅管理员 ·
:octicons-issue-opened-24: 强制 ·
:octicons-thumbsdown-24: 不推荐

用法：`~add_base_su`

让本机器人的拥有者成为群聊的管理员。

## `add_su`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~add_su <QQ 号>`

添加一个新的超级管理员。

## `del_su`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~del_su <QQ 号>`

撤销超级管理员权限。

## `set`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~set <self> <do> <id>`

操作数据库。详见[源码](https://github.com/Teahouse-Studios/bot/blob/master/database/__init__.py#L53)。

## `restart`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~restart`

重启机器人软件。

## `update`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~update`

从 GitHub 下载新版本小可并更新。

## `update&restart`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

从 GitHub 下载新版本小可并更新，之后重启机器人软件。

## `echo`

:octicons-lock-24: 仅超级管理员 ·
:octicons-issue-opened-24: 强制

用法：`~echo <信息>`

重复消息。
