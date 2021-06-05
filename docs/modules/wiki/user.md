# `user`
:octicons-file-code-24: 开源

此模块可以查询某个 MediaWiki 网站中的用户信息。

## `user`
<figure style="float: right;">
  <img src="/assets/user-example.png" width="300px" alt="例子" />
  <figcaption>图片返回结果示例</figcaption>
</figure>

此命令可以查询某个 MediaWiki 网站中的用户信息。

用法：`~user [-<p|r>] [~<Gamepedia 网站域名>] [<interwiki>:]<用户名>`

快捷使用前缀：`~u`

- `-p`：返回一张在 Gamepedia 的用户的详情图片，若非 Gamepedia 用户，则图片中只会展示编辑数。
- `-r`：返回 Gamepedia 取得的更多信息。

!!! bug
    本功能已知问题有：

    1. 强制支持 `~<Gamepedia 网站域名>`

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的某些信息，请不要作死。
