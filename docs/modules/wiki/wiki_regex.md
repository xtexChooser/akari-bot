# `wiki_regex`

:octicons-file-code-24: 开源

此模块可以让你无需机器人前缀查询一个基于 MediaWiki 的网站的指定页面的详情。

## `wiki_regex`
:octicons-unlock-24: 公开

用法：`[[[<interwiki>]:<页面名>]]`（无需前缀，可使用于消息的任何位置）

此指令可以让你无需机器人前缀查询一个基于 MediaWiki 的网站的指定页面的详情。

!!! faq "无法使用？"
    请检查是否开启 [`wiki_start_site`](/modules/wiki/wiki_start_site/) 和 [`interwiki`](/modules/wiki/interwiki/) 并进行了配置。

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的信息。即使网站不在黑名单内，返回的内容仍将经过小可云智能过滤，请不要作死。
