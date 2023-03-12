# Update
- 2023.3.12 进入稳定期，降低更新频率
  + 出于玩玩bing的chatgpt心态，按[waylaidwanderer](https://github.com/waylaidwanderer/PandoraAI)搞了一套[测试站](https://ms.sheepig.top/)，由于功能比较丰富，打开时加载稍慢。另外此项目代码也有bug需要完善（如果你去体验会发现的），不做详细介绍。
- 2023.3.7 小改代码，实现多用户独立会话互不干扰，并且不影响每个用户的连续对话（临时性方案，等作者重写核心代码）
- 2023.3.3-2 十分感谢[minguncle](https://github.com/minguncle)提交PR，现支持按回车发送问题请求，按shift+回车可换行输入文本
- 2023.3.3-1 切换[acheong08](https://github.com/acheong08/ChatGPT)的V3对接官方API，实现上下文关联
- 2023.3.2 切换到官方ChatGPT API（注：API收费）
- 2023.2.28 关于OPENAI允许问题的最大长度
  + 根据OPENAI官方[问答](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)"Depending on the [model](https://platform.openai.com/docs/models/gpt-3) used, requests can use up to 4097 tokens shared between prompt and completion. If your prompt is 4000 tokens, your completion can be 97 tokens at most"，问题和回答加起来的总长度无法超过4097个token，如果你不清楚自己问题的长度，可以使用[官方计数器](https://platform.openai.com/tokenizer)
- 2023.2.20 `支持markdown语法`
> ~~感谢某爱心人士捐助，https://gpt.sheepig.top/chat 已恢复使用~~再次被干爆，没次数了，请访问 https://chat.sheepig.top 使用网页代理ChatGPT版本

# chatgpt-web
### 使用官方ChatGPT API实现简单HTML网页版在线聊天（支持markdown语法及连续对话）（基于[此项目](https://github.com/AlliotTech/chatgpt-web)调整而来）
> 该版本基于OPENAI ChatGPT API开发（付费），想使用`ChatGPT`（免费）的请访问[chatgpt-html](https://github.com/slippersheepig/chatgpt-html)
## 部署
### 获取OpenAI API KEY
- 建议参考[此教程](https://blog.csdn.net/hekaiyou/article/details/128303729)获取
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
    image: sheepgreen/chatgpt-web #如果是arm架构，需要改成chatgpt-web:arm
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
