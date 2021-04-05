# `wiki_start_site`

!!! warning "注意"
    此命令已被整合至[`wiki`](/modules/wiki/wiki/)模块，可使用`~wiki set <wiki 的脚本路径>`来设置默认 wiki 而非打开本模块设置。

:octicons-file-code-24: 开源 ·
:octicons-package-dependencies-24: 依赖：[`wiki`](/modules/wiki/wiki/) 或 [`wiki_regex`](/modules/wiki/wiki_regex/)

此模块可以让你查询一个基于 MediaWiki 的网站的指定页面的详情。

## `wiki_start_site`
:octicons-unlock-24: 公开

用法：`~wiki_start_site <wiki 的脚本路径>`

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

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的某些信息。即使网站不在黑名单内，返回的内容仍将经过小可云智能过滤，请不要作死。
