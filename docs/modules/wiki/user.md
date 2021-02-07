# `user`
:octicons-file-code-24: 开源

此模块可以查询某个 MediaWiki 网站中的用户信息。

## `user`
<figure style="float: right;">
  <img src="/assets/user-example.jpg" width="300px" alt="例子" />
  <figcaption>图片返回结果示例</figcaption>
</figure>

此命令可以查询某个 MediaWiki 网站中的用户信息。

用法：`user [-<p|r>] [~<Gamepedia 网站域名>] [<interwiki>:]<用户名>`

- `-p`：返回一张在 Gamepedia 的用户的详情图片。
- `-r`：返回更多信息。

!!! bug
    本功能已知问题有：

    1. 不能正确翻译 Fandom 等农场和其他的自定义用户组。若您有发现更多未翻译的用户组，欢迎进行[汇报](https://github.com/Teahouse-Studios/bot/)。
    2. 强制支持 `~<Gamepedia 网站域名>`
    3. 图片返回不支持自定义 interwiki，只支持 [`wiki_start_site`](/modules/wiki/wiki_start_site/) 指定的起始网站定义的 interwiki。
    4. 参数只能放在用户名和“interwiki”前。

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的信息。即使网站不在黑名单内，返回的图像和内容仍将经过小可云智能过滤，请不要作死。
