# `cytoid`

:octicons-file-code-24: 开源

此模块可以让你查询 Cytoid 游戏中的信息。

!!! seealso "另见"
    本模块返回的是 Cytoid B30 结果。关于 Arcaea 的 B30 结果，[见此](./cytoid/#)。

## `cytoid profile`
:octicons-unlock-24: 公开

用法：`~cytoid profile <UID>`

此命令可以获取一个 Cytoid 用户的账号信息和头像。

!!! example "示例"
    这是返回的结果示例：
    ```
    UID: wdljt
    BasicExp: 200543
    LevelExp: 69519
    TotalExp: 270062
    CurrentLevel: 42
    NextLevelExp: 273000
    Rating: 8.5804466215000000
    Grade: A: 78, B: 45, C: 28, D: 15, F: 24, S: 87, SS: 8
    ```
    ![头像](/assets/wdljt.jfif)

## `cytoid b30`
:octicons-unlock-24: 公开

用法：`~cytoid b30 <UID>`

此命令可以获取一个 Cytoid 用户的 Best30 信息。

!!! example "示例"
    这是返回的结果示例：
    ![头像](/assets/b30.jfif)

## `cytoid r30`
:octicons-unlock-24: 公开

用法：`~cytoid r30 <UID>`

此命令可以获取一个 Cytoid 用户的 Recent30 信息。

!!! example "示例"
    这是返回的结果示例：
    ![头像](/assets/r30.jpg)

!!! warning "警告"
    返回的文字和图像将经过小可云智能过滤，请不要作死。
