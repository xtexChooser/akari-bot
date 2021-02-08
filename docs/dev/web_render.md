# Web Render

在此对 `infobox_render` 设置项进行说明。

本文假定您有基础 Node.js 操作技能。配置过程中需要 yarn。

```powershell
$ git clone https://github.com/Teahouse-Studios/oa-web-render
$ cd oa-web-render
$ yarn install
$ yarn build
```

前往 <https://github.com/adieuadieu/serverless-chrome/releases> 下载任意版本 Chromium（Linux），或前往 Chromium 官方进行下载。

放置于某一位置，配置好执行权限。

在上方clone的仓库目录中新建 `.env` 文件，内容如下：

```python
CHROMIUM_PATH = # Chromium 可执行文件位置
```

之后，运行 `dist/index.js`。

```powershell
$ node dist/index.js
```

API 监听端口位于 15551。您可自行选择配置代理。`infobox_render` 配置项中填写访问地址，如`http://127.0.0.1:15551/`。
