# 权限

小可内置了以下权限组：

- `superuser`：全域机器人管理员，被开发者使用
- `group_adminuser`：机器人管理员，群内管理员或私聊默认拥有此权限
- `user`：普通用户

在本文档中的权限标识对应关系如下：

| 标识                            | 对应的权限                       |
| ------------------------------- | -------------------------------- |
| :octicons-lock-24: 仅管理员     | `superuser` 和 `group_adminuser` |
| :octicons-lock-24: 仅超级管理员 | `superuser`                      |
| :octicons-unlock-24: 公开       | `user`                           |
