# 目录
-   [简介](#简介)
-   [文件位置](#文件位置)
-   [语言文件格式](#语言文件格式)
-   [示例](#示例)
-   [排版规范](#排版规范)
    -   [空格](#空格)
        - [中英文之间需要增加空格](#中英文之间需要增加空格)
        - [中文与数字之间需要增加空格](#中文与数字之间需要增加空格)
        - [中文与半角符号之间需要增加空格](#中文与半角符号之间需要增加空格)
        - [数字与单位之间不加空格](#数字与单位之间不加空格)
        - [变量与中文之间需要增加空格](#变量与中文之间需要增加空格)
        - [全角标点与其他字符之间不加空格](#全角标点与其他字符之间不加空格)
        - [半角标点相关的空格](#半角标点相关的空格)
        - [字符串开头和结尾不应出现空白字符](#字符串开头和结尾不应出现空白字符)
        - [除特殊情况外，不应有多个空格连续出现](#除特殊情况外，不应有多个空格连续出现)
    -   [标点符号](#标点符号)
        -   [不要连用标点符号](#不要连用标点符号)
        -   [中文使用全角中文标点](#使用全角中文标点)
        -   [简体中文不要使用直角引号](#简体中文不要使用直角引号)
        -   [数字和英文使用半角字符](#数字和英文使用半角字符)
        -   [引用句内的标点按照其语境使用](#引用句内的标点按照其语境使用)
        -   [英文不要使用弯引号](#英文不要使用弯引号)
        -   [英文省略号使用三个点](#英文省略号使用三个点)
    -   [语句](#语句)
        -   [使用“你”而不是“您”](#使用“你”而不是“您”)
        -   [正确使用“的”“地”“得”](#正确使用“的”“地”“得”)
        -   [避免使用“我”“我们”](#避免使用“我”“我们”)
        -   [专有名词使用正确的书写格式](#专有名词使用正确的书写格式)
        -   [不要使用非正式的缩写](#不要使用非正式的缩写)
        -   [不同地区的中文使用对应的地区词](#不同地区的中文使用对应的地区词)
        -   [慎用“发生错误”](#慎用“发生错误”)
-   [报告问题](#报告问题)

# 简介
本规范文件旨在确保项目中的多语言文本一致性和格式规范。请遵循以下内容以保持代码库中的多语言资源的统一性。

# 文件位置
请将语言文件放置在 `/locales` 目录中，并以语言代码命名为 JSON 文件。

根路径下的目录用于放置全局字符串，模块下的目录用于放置对应专用的模块字符串。

原则上，模块字符串和对应模块须对应，若模块之间存在关联则可以例外，否则请考虑转为全局字符串。

# 语言文件格式
请确保键名与字符串一一对应，不得嵌套。

**全局字符串的命名方式**：`字符串类别.用途`

**模块字符串的命名方式**：`模块名称.字符串类别.(命令名称.)用途`

使用 `${变量名}` 可表示变量，变量名须使用英文，不建议使用 Python 语句，禁止使用空格和特殊符号，如需分隔则请使用下划线代替。

# 示例
在模块帮助中调用多语言字符串的示例：
```python3
from core.component import module

test = module('test', desc='{test.help.desc}')

@test.command('say <word> {{test.help.say}}')
...
```
在代码中调用多语言字符串的示例：
```python3
from core.builtins import Bot

async def test(msg: Bot.MessageSession):
...
    await msg.send_message(msg.locale.t("test.message.say.prompt"))
# 没有变量时可直接输出
    await msg.send_message(msg.locale.t("test.message.say.reply", sender=msg.target.sender_id))
# 若存在变量，则须将变量赋值后输出
# 如此处在字符串内的变量为 ${sender}，并被赋值为 Bot.MessageSession.target.sender_id
```

# 排版规范
> 本文部分参照[中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)，内容可能有出入。

太长不看：半角符号和全角符号（标点除外）之间用空格隔开，正确使用对应语言的标点符号
和用词习惯。

## 空格
### 中英文之间需要增加空格
正确：
> 在 IBM 的研究中，他们利用 AI 技术开发了一种先进的语音识别系统。

错误：
> 在IBM的研究中，他们利用AI技术开发了一种先进的语音识别系统。

例外：专有名词、商品名等词语，按照约定俗成的格式书写。

### 中文与数字之间需要增加空格
正确：
  > 今年的全球汽车销售量达到了 8000 万辆。

错误：
  > 今年的全球汽车销售量达到了8000万辆。

### 中文与半角符号之间需要增加空格
正确：
> 很多人都在学习 C++ 这门语言。

错误：
> 很多人都在学习C++这门语言。

### 数字与单位之间不加空格
正确：
> 我家的光纤入户宽带有 10Gbps，SSD 一共有 10TB。
>
> 这个城市每年平均降雨量为 1200mm。
>
> 角度为 90° 的角，就是直角。

错误：
>我家的光纤入户宽带有 10 Gbps，SSD 一共有 20 TB。
>
> 这个城市每年平均降雨量为 1200 mm。
>
> 角度为 90 ° 的角，就是直角。

### 变量与中文之间需要增加空格
变量的输入一般为英文或数字，故变量与中文之间须加入空格。

正确：
> 你扔了一块石头，漂了 ${count} 下。

错误：
> 你扔了一块石头，漂了${count}下。

例外：如果变量的输入确保为中文，则可以不加空格。

### 全角标点与其他字符之间不加空格
正确：
> 刚刚买了一部 iPhone，好开心！

错误：
> 刚刚买了一部 iPhone ，好开心！

### 半角标点相关的空格
在半角标点（左引号、左括号等引用标点除外）之后如果有其他字符，请增加空格隔开。

左引号、左括号等引用标点如果其之前有其他字符，请增加空格隔开。

撇号和连接号（hyphen）前后不加空格。破折号（dash）前后需增加空格。

多个半角标点连在一起需看成一个标点，不要用空格将它们分开。

正确：
> The sun set over the horizon, casting a warm glow on the city. As night fell, the lights began to twinkle, creating a captivating skyline.
> 
> The storm — with its strong winds, torrential rain, and relentless thunder — lasted for hours, leaving behind a trail of destruction.
> 
> The mysterious treasure was said to be hidden deep within the ancient cavern... guarded by mythical creatures and protected by an ancient spell.
> 
> "Life is what happens when you're busy making other plans." people always said.
> 
> I went to the bookstore yesterday and bought a new novel (the one I've been wanting to read for months).

错误：
> The sun set over the horizon,casting a warm glow on the city.As night fell,the lights began to twinkle,creating a captivating skyline.
> 
> The storm—with its strong winds,torrential rain,and relentless thunder—lasted for hours,leaving behind a trail of destruction.  
>
> The mysterious treasure was said to be hidden deep within the ancient cavern . . . guarded by mythical creatures and protected by an ancient spell. 
>
> " Life is what happens when you' re busy making other plans. " people always said. 
> 
> I went to the bookstore yesterday and bought a new novel( the one I' ve been wanting to read for months) . 

### 字符串开头和结尾不应出现空白字符
正确：
> 这是一行文字。

错误：
> ·这是一行文字。·
> 
>（使用“·”代替空格）

例外：英文句子的结尾可不遵守此标准。（在字符串需要拼接的情况下，英文句号后的空格是必要的。）

### 除特殊情况外，不应有多个空格连续出现
正确：
> 我喜欢 GitHub。

错误：
> 我喜欢··GitHub。
>
>（使用“·”代替空格）

## 标点符号
### 不要连用标点符号
虽然连用标点符号在规范中是被允许的行为，但是这样会破坏句子的规范性和美观性，请不要这样做。

正确：
> 德国队竟然战胜了巴西队！

错误：
> 德国队竟然战胜了巴西队！！！

例外：在表达同时包含疑惑和感叹的语气时，可连用“？！”。

### 中文使用全角中文标点
正确：
> 嗨！你知道嘛？今天前台的小妹跟我说“喵”了哎！

错误：
> 嗨! 你知道嘛? 今天前台的小妹跟我说 "喵" 了哎!
>
> 嗨!你知道嘛?今天前台的小妹跟我说"喵"了哎!

例外：数学运算符必须使用半角。

### 简体中文不要使用直角引号
直角引号并不符合简体中文使用者的使用习惯。

正确：
> “老师，‘有条不紊’的‘紊’是什么意思？”

错误：
> 「老师，『有条不紊』的『紊』是什么意思？」

### 数字和英文使用半角字符
正确：
> 这件蛋糕只卖 200 元。

错误：
> 这件蛋糕只卖 ２００ 元。

### 引用句内的标点按照其语境使用
引用符号本身仍然需要按照其外部语境决定。

正确：
> 乔布斯那句话是怎么说的？“Stay hungry, stay foolish.”

错误：
> 乔布斯那句话是怎么说的？“Stay hungry，stay foolish。”

### 英文不要使用弯引号
中文弯引号和英文弯引号属于同一个字符，如果使用弯引号反而会造成阅读问题。请使用直引号 `"`。

正确：
> "Success is not final, failure is not fatal: It is the courage to continue that counts."

错误：
> “Success is not final, failure is not fatal: It is the courage to continue that counts.”

### 英文省略号使用三个点
原因同上。请使用三个点 `...`。

正确：
> In the serene moonlit night, whispers of ancient tales lingered, echoing through the stillness of time...

错误：
> In the serene moonlit night, whispers of ancient tales lingered, echoing through the stillness of time…

## 语句
### 使用“你”而不是“您”
机器人、用户、开发者与维护者之间互为平级关系，无需使用“您”。

### 正确使用“的”“地”“得”
示例：
> 他是一个很高的人。
> 
> 他总能很快地解决问题。
> 
> 他跑得很快。

### 避免使用“我”“我们”
为了保持机器人的适用性，请尽可能不要使用第一人称代词，以避免涉及个人主观观点或情感。

### 专有名词使用正确的书写格式
正确：
> 使用 GitHub 登录

错误：
> 使用 Github 登录
> 
> 使用 gitHub 登录
> 
> 使用 github 登录
> 
> 使用 GITHUB 登录

### 不要使用非正式的缩写
正确：
> 我们需要一位熟悉 JavaScript、HTML5，至少理解一种框架（如 Backbone.js、AngularJS、React 等）的前端开发者。

错误：
> 我们需要一位熟悉 Js、h5，至少理解一种框架（如 backbone、angular、RJS 等）的 FED。

### 不同地区的中文使用对应的地区词
不要在繁体中文中使用“视频”等错误的地区词，这不是玩笑。

正确：
> 輸入影片編號取得對應資訊。

错误：
> 輸入視頻編號獲得相應信息。

例外：专有名词、商品名等词语，按照约定俗成的格式书写。

### 慎用“发生错误”
当命令出现可能的预料之外的情况下，输出的字符串可以使用“发生错误”前缀，刻意引起的意外（如输入不合要求）不宜使用。

# 报告问题
与简体中文相关的问题可直接使用 [Issue](https://github.com/Teahouse-Studios/akari-bot/issues/new) 报告。

简体中文以外的所有语言由机器人 @Hldbot 维护，相关问题请移步 [Crowdin](https://crowdin.com/project/akari-bot) 报告。
