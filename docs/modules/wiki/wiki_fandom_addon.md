# `wiki_fandom_addon`

:octicons-file-code-24: 开源 ·
:octicons-package-dependencies-24: 依赖：[`wiki_regex`](/modules/wiki/wiki_regex/)

此模块可以在行内查询（[`wiki_regex`](/modules/wiki/wiki_regex/)）wiki 时快速查询一个 Fandom 农场网站的指定页面的详情。

用法：`w:c:<网站域名>:[<interwiki>]:<页面名>`

!!! bug
    此功能目前有两个 bug：
    
    1. 实际支持的用法并不符合在 Fandom 实际使用的语法，应改为 `w:c:[<langcode>.]<sitename>:[<interwiki>]:<pagename>`。
    2. 不支持使用常规查询（[`wiki`](/modules/wiki/wiki/)）。

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的信息。即使网站不在黑名单内，返回的内容仍将经过小可云智能过滤，请不要作死。
