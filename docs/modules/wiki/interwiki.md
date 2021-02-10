# `interwiki`

:octicons-file-code-24: 开源 ·
:octicons-package-dependencies-24: 依赖：[`wiki`](/modules/wiki/wiki/) 或 [`wiki_regex`](/modules/wiki/wiki_regex/)

此模块可以让你查询一个基于 MediaWiki 的网站的指定页面的详情。

## `interwiki`
:octicons-unlock-24: 公开

用法：

 - 添加新的 interwiki：`interwiki add <interwiki 名称> <wiki 域名/脚本路径>`
 - 删除现有的 interwiki：`interwiki del <interwiki 名称>`


此指令可以设置使用 [`wiki`](/modules/wiki/wiki/) 指令时的 interwiki。设置完毕后，可以在使用 `wiki` 时在前面加上 interwiki 的名称加<strong>英文</strong>冒号（`:`）以获取此 wiki 的内容。

可以设置多个 interwiki。

!!! faq "脚本路径"
    “脚本路径”指的是 wiki 的 index.php、api.php 所在的目录。

    - 在 WMF 所属的网站（维基百科、维基词典等）和 Miraheze 农场，此目录在 `<域名>/w/`。
    - 在 Fandom 农场的英文 wiki 上，此目录在 `<域名>/wiki/`。
    - 在 Fandom 农场的其他语言 wiki 上，此目录在 `<域名>/<语言代码>/wiki/`。
    - 在 Gamepedia 农场上，此目录在 `<域名>`。

    如果您的 wiki 是自行搭建的，或您的农场没有在此列出，下面是获取脚本路径的方法。
    
    1. 在搜索框内输入：`Special:Version`。
    2. 打开页面后，向下滑，找到第二个表格。对于中文 wiki 来说，此表格的名称为“接入点URL”。
    3. 找到此表格的第二行（对于中文 wiki 来说，这一行的表头为“脚本路径”）第二列（对于中文 wiki 来说，这一列的表头为“URL”）内容。右键此字符并复制链接，即为此 wiki 的脚本路径。

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的某些信息，请不要作死。
