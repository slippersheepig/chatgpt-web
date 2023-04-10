# chatgpt-web
### 使用官方ChatGPT API实现简单HTML网页版在线聊天（基于[此项目](https://github.com/AlliotTech/chatgpt-web)调整而来）
> 该版本基于OPENAI ChatGPT API开发（付费），想使用`ChatGPT`（免费）的请访问[chatgpt-html](https://github.com/slippersheepig/chatgpt-html)
## 特性
- 文件结构简单，主要面向小白用户
- 功能不多，但核心的连续对话、多用户会话隔离、markdown格式输出都具备
## 部署
### 获取OpenAI API KEY
- 建议官方渠道获取https://platform.openai.com/account/api-keys
### 配置
#### 从源码配置
- 请参考原作者[github](https://github.com/AlliotTech/chatgpt-web)
#### 使用Docker Compose
> 以下所有文件放同一目录
- 新建`.env`配置文件，粘贴以下内容并保存
```bash
OPENAI_API_KEY="前面你获取到的OpenAI API KEY"
```
- 新建`docker-compose.yml`配置文件，粘贴以下内容并保存
```bash
services:
  chatgpt:
    image: sheepgreen/chatgpt-web
    container_name: webchat
    volumes:
      - ./.env:/chatgpt-web/.env
#      - ./chat.html:/chatgpt-web/templates/chat.html #默认内置我的UI，如需替换自用网页请取消注释，需与docker-compose.yml文件在同一目录
    ports:
      - "8888:8088" #8088为容器内部端口，不可更改；8888为外部映射端口，可自行更改
    restart: always
```
- 输入`docker-compose up -d`即启动成功
## 注意事项
- 访问地址为http://ip:port/chat
- 修改`chat.html`文件后，需要docker restart webchat才能生效
## 其他相关
- [ChatGPT电报机器人](https://github.com/slippersheepig/chatgpt-telegram-bot)，[ChatGPT企业微信应用机器人](https://github.com/slippersheepig/chatgpt-bizwechat-bot)，[ChatGPT的QQ频道机器人DOCKER版](https://github.com/slippersheepig/QQChannelChatGPT)，[微软BING电报机器人DOCKER版](https://github.com/slippersheepig/BingChatBot)，[谷歌BARD网页版](https://github.com/slippersheepig/bard-web)，[谷歌BARD电报机器人](https://github.com/slippersheepig/bard-telegram-bot)
- 出于玩玩bing的chatgpt心态，按[danny-avila](https://github.com/danny-avila/chatgpt-clone)搞了一套[测试站](https://ms.sheepig.top)（需要先点击聊天框左边的图标切换模型，默认模型是API，我的KEY没额度了），`BingAI`就是GPT-4，`Sydney`是“破解”过的BingAI（没有每轮对话最多15次和每天对话最多150次的限制，但是智商差一点）。另外此项目代码也有bug需要完善（如果你去体验会发现的），不做详细介绍。
![image](https://user-images.githubusercontent.com/58287293/225885666-ff56fb90-13ac-46a4-b685-d4188c3fee36.png#pic_center)
