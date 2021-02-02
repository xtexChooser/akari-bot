# 技术实现

基于[Graia](https://github.com/GraiaProject/Application)和[Mirai](https://github.com/mamoe/mirai)。

## 运行原理

1. 机器人接受到新消息。
2. 进入 `bot.py` 进行初步分类。
3. 进入 `core.parser` 解析消息。
4. 二次处理消息。
5. 分类至各个模块进行精确消息处理。
6. 返回结果。
