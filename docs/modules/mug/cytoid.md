# `cytoid`

:octicons-file-code-24: 开源

此模块可以让你查询 Cytoid 游戏中的信息。

!!! seealso "另见"
    本模块返回的是 Arcaea B30 结果。关于 Cytoid 的 B30 结果，[见此](./cytoid/#)。

## `cytoid profile`
:octicons-unlock-24: 公开

用法：`~cytoid profile <UID>`

此命令可以获取一个 Cytoid 用户的账号信息。

!!! example "示例"
    这是返回的结果示例：
    ```
    获取结果
    B30: 11.114 | R10: 10.977
    B30倒5列表：
    [1] Heavensdoor (FTR)
    [1] 9805653 / 9.9 -> 10.9283
    [2] The Message (FTR)
    [2] 9844566 / 9.7 -> 10.9228
    [3] #1f1e33 (PRS)
    [3] 9944194 / 9.2 -> 10.921
    [4] Alexandrite (FTR)
    [4] 9770055 / 10 -> 10.9002
    [5] Cyaegha (FTR)
    [5] 9522271 / 10.8 -> 10.8742
    ```

!!! faq "无法使用？"
    请检查您是否输入的是 Cytoid 用户<strong>数字</strong> ID。

!!! warning "警告"
    返回的图像将经过小可云智能过滤，请不要作死。

!!! error "版权声明"
    数据通过 lowiro 的公共 API 获取。游戏内素材根据英国 *Copyright, Designs and Patents Act 1988* 中对于 *fair dealing* 之规定合理使用。
