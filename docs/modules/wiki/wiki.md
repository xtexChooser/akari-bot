# `wiki`

:octicons-file-code-24: 开源

此模块可以让你查询一个基于 MediaWiki 的网站的指定页面的详情。

## `wiki`
:octicons-unlock-24: 公开

用法：`~wiki [<interwiki>:]<页面名>`

此指令可以让你查询一个基于 MediaWiki 的网站的指定页面的详情。

## `wiki random`

用法：`~wiki ramdom`

此指令会随机查询一个基于 MediaWiki 的网站的指定页面的详情。

## `wiki set`

用法：`~wiki set <wiki 的脚本路径>`

此指令可以设置使用 [`wiki`](/modules/wiki/wiki/) 指令时的默认 wiki。

每个群只能设置一个默认 wiki。

!!! faq "脚本路径"
    “脚本路径”指的是 wiki 的 index.php、api.php 所在的目录。

    - 在 WMF 所属的网站（维基百科、维基词典等）和 Miraheze 农场，此目录在 `<域名>/w/`。
    - 在 Fandom 农场的英文 wiki 上，此目录在 `<域名>`。
    - 在 Fandom 农场的其他语言 wiki 上，此目录在 `<域名>/<语言代码>/`。

    如果您的 wiki 是自行搭建的，或您的农场没有在此列出，下面是获取脚本路径的方法。
    
    1. 在搜索框内输入：`Special:Version`。
    2. 打开页面后，向下滑，找到第二个表格。对于中文 wiki 来说，此表格的名称为“接入点URL”。
    3. 找到此表格的第二行（对于中文 wiki 来说，这一行的表头为“脚本路径”）第二列（对于中文 wiki 来说，这一列的表头为“URL”）内容。右键此字符并复制链接，即为此 wiki 的脚本路径。
    
## `wiki iw add/del/list`

用法：

 - 添加新的 interwiki：`~wiki iw add <interwiki 名称> <wiki 域名/脚本路径>`
 - 删除现有的 interwiki：`~wiki iw del <interwiki 名称>`
 - 查看当前设置 interwiki 列表：`~wiki iw list`


此指令可以设置使用 [`wiki`](/modules/wiki/wiki/) 指令时的 interwiki。设置完毕后，可以在使用 `wiki` 时在前面加上 interwiki 的名称加<strong>英文</strong>冒号（`:`）以获取此 wiki 的内容。

此指令可以设置使用 wiki 指令时的 interwiki。设置完毕后，可以在使用 wiki 时在前面加上 interwiki 的名称加英文冒号（:）以获取此 wiki 的内容。

## `wiki headers set/reset/show`

用法：

 - 设置新的请求标头：`~wiki headers set <请求标头>`
 - 重置请求标头：`~wiki headers reset`
 - 查看当前设置请求标头：`~wiki headers show`

此指令用于设置使用 [`wiki`](/modules/wiki/wiki/) 指令时的请求标头。设置完毕后，每一次查询Wiki都会使其带上此标头查询。

不同标头之间使用换行隔开。

如果你不清楚这有什么用，那么请不要乱设置，否则可能导致返回结果异常。

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的某些信息，请不要作死。
