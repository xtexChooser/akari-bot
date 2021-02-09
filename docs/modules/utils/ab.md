
# `ab`

:octicons-file-code-24: 开源

此模块可以让你查询中文 Minecraft Wiki 的滥用日志。

## `ab`
:octicons-unlock-24: 公开 ·
:octicons-reply-24: 一分钟后撤回

用法：`ab`

此指令可以让你查询中文 Minecraft Wiki 的滥用日志。

!!! bug
    本指令已知无法进行中文 Minecraft Wiki 之外的滥用日志查询。

!!! example "示例"
    本指令返回的结果示例：
    ```
    •Minecraft Wiki:沙盒/Sculk Sensor - Zollo757347于18时33分
    过滤器名：插入零宽字符
    处理结果：tag•Minecraft Wiki:沙盒/Sculk Sensor - Zollo757347于18时27分
    过滤器名：插入零宽字符
    处理结果：warn•User:HLDoramon/Msgbox/Potato - 36.157.70.134于18时19分
    过滤器名：新用户和IP用户编辑他人用户页
    处理结果：disallow•MinecraftEdu - DSDlonDTX于17时28分
    过滤器名：创建未翻译的页面
    处理结果：warn•Minecraft Wiki:管理员告示板 - Ff98sha于22时36分
    过滤器名：未替换应当替换使用的模板
    处理结果：warn
    ...仅显示前5条内容
    [一分钟后撤回本消息]
    ```

!!! warning "警告"
    某些网站已经被列入黑名单，使用此命令无法获取某些网站的信息。即使网站不在黑名单内，返回的内容仍将经过小可云智能过滤，请不要作死。
