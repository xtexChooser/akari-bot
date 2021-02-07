# Web Render

在此对```infobox_render```设置项进行说明。

本文假定您有基础NodeJS操作技能。配置过程中需要yarn。

```
git clone https://github.com/Teahouse-Studios/oa-web-render
yarn install
yarn build
```

前往 https://github.com/adieuadieu/serverless-chrome/releases 下载任意版本chromium(linux)，或前往chromium官方地址进行下载。

放置于某一位置，配置好执行权限。

在上方clone的仓库目录中新建```.env```文件，内容如下

```
CHROMIUM_PATH=chromium可执行文件位置
```

运行```dist/index.js```，API监听端口位15551，您可自行选择配置反代，```infobox_render```配置项中填写访问地址，如```http://127.0.0.1:15551/```