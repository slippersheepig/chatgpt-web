> **Warning**

> 我自己的API KEY免费限额已经用光了

请访问https://chat.sheepig.top 使用ChatGPT网页版
# chatgpt-web
### 使用GPT-3.5中的text-davinci-003模型，利用OpenAI API实现简单HTML网页版在线聊天（基于[此项目](https://github.com/AlliotTech/chatgpt-web)调整而来）
> 该版本基于OPENAI API KEY开发，想使用`ChatGPT`的请访问[chatgpt-html](https://github.com/slippersheepig/chatgpt-html)
#### ![G L%7VF I~{@83}SVRI_WPN](https://user-images.githubusercontent.com/58287293/207792987-a0a781df-8273-4148-a369-aa4a2379686a.png)（重要）ChatGPT与GPT-3.5（OpenAI API）的区别
- 在[OpenAI官方网页](https://openai.com/blog/chatgpt/)中，我们可以看到官方对ChatGPT的描述为“ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022. You can learn more about the 3.5 series [here](https://beta.openai.com/docs/model-index-for-researchers). ChatGPT and GPT 3.5 were trained on an Azure AI supercomputing infrastructure”，从而得知ChatGPT与GPT-3.5是两个不同产品
- 官方对GPT-3.5系列的[介绍](https://beta.openai.com/docs/model-index-for-researchers)里，`text-davinci-003`是其中的模型之一
- 我们再查阅官方对OpenAI API KEY的[介绍](https://beta.openai.com/docs/introduction/key-concepts)，其中有一句“The API is powered by a set of models with different capabilities and price points. Our base GPT-3 models are called Davinci, Curie, Babbage and Ada”，davinci赫然在列
#### ![I4{CU~ G( OH$WR_ T_1JWF](https://user-images.githubusercontent.com/58287293/207798807-a4dce6d3-14a0-40af-8008-30de8a55d513.png) 至此，我们可以得出结论：现在所有使用OpenAI API KEY的项目，`都不是基于ChatGPT开发的项目`，官方并未发布ChatGPT的API接口
- 事实上，ChatGPT最近发生过登录认证风波，想了解详细过程的可以查看这个[issue](https://github.com/acheong08/ChatGPT/issues/261)
- 如果你自己有分别使用过ChatGPT的官方chat和OpenAI的API接口chat，你会发现API接口chat比ChatGPT的官方chat“笨”得多
## 部署
### 获取OpenAI API KEY
- 建议参考[此教程](https://blog.csdn.net/hekaiyou/article/details/128303729)获取
### 配置
#### 从源码配置
- 请参考原作者[github](https://github.com/AlliotTech/chatgpt-web)
#### 使用Docker Compose
- 新建`chat.html`网页文件，粘贴以下代码并保存（UI很丑，建议各自美化）
```html
<!DOCTYPE html>
<html lang="en">

<!--自适应屏幕大小-->
<meta name="viewport" content="width=device-width,initial-scale=1" />

<head>
    <!-- <link rel="shortcut icon" href="" type="image/x-icon" /> -->
    <meta charset="UTF-8">
    <title>OpenAI</title>
    <style>
      body {
        color: #333;
        background-color: #eee;
      }
    @media (prefers-color-scheme: dark) {
      body {
        background: black;
        color: white;
      }
    }
    </style>
</head>

<body>
    <div align="center">
        <h2>Fake ChatGPT</h2>
        <div>注意：接口返回可能比较慢（服务在国外，并且OpenAI返回速度也比较慢），提交后需要等待处理完成，请勿重复提交！！！</div>
        <div>~接口返回有长度限制~</div>
        <hr />
        {% if message %} {{ message }} {% endif %}
        <form method="post" onsubmit="submit.disabled=true">
            <textarea style="width:35%;" name="question" placeholder="点击这里输入问题" rows="11" id="form"></textarea>
            <br>
            <input type="submit" style="width:150px;height:50px;background-color:green;font-size:30px" value="提交" id="submit" />
        </form>
        <div id="loading" style="display:none; color:red"><b>后端正在处理，请稍等...</b></div>
        {% if question %}
        <div style="text-align: left"><b>人类:</b>
            <pre id="question">{{ question }}</pre>
        </div>
        <hr />
        <div style="text-align: left"><b>人工智障:</b>
            <pre style="text-align:left; white-space: pre-wrap;" id="res">{{ res }}</pre>
        </div>
        {% endif %}
    </div>
</body>
<script>
    let loading = document.getElementById('loading');
    let form = document.querySelector('form');
    form.addEventListener('submit', () => {
        loading.style.display = 'block';
    });
</script>
</html>
```
- 新建`docker-compose.yml`配置文件，粘贴以下内容并保存，放在与`chat.html`文件相同的目录下
```bash
version: '3'
services:
  chatgpt:
    image: sheepgreen/chatgpt-web #如果是arm架构，需要改成chatgpt-web:arm
    container_name: webchat
    environment:
      - OPENAI_API_KEY=前面你获取到的OpenAI API KEY
    volumes:
      - ./chat.html:/chatgpt-web/templates/chat.html
    ports:
      - "8888:80" #80为容器内部端口，不可更改；8888为外部映射端口，可自行更改
    restart: always
```
- 输入`docker-compose up -d`即启动成功
## 注意事项
- 访问地址为http://ip:port/chat
- 修改`chat.html`文件后，需要docker restart webchat才能生效
