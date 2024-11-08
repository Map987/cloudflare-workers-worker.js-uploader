
``` 
addEventListener('fetch', event => {
  event.respondWith(handleFetch(event.request));
});

async function handleFetch(request) {
  const url = new URL(request.url);
  if (url.pathname === '/ok') {
    // 对于路径 /ok，返回 https://api.gamer.com.tw/anime/v1/anime_list.php 的内容
    const response = await fetch('https://api.gamer.com.tw/anime/v1/anime_list.php');
    const formattedResponse = await formatResponse(response);
    return new Response(JSON.stringify(formattedResponse), {
      headers: { 'Content-Type': 'application/json' }
    });
  } else {
    // 对于其他路径，继续正常的fetch请求
 //   return fetch(request);
    return new Response('访问https://域名….com/ok目录', {
      headers: { 'Content-Type': 'text/plain' }
      });
      // https://bahamut..workers.dev/显示 ： 璁块棶https://鍩熷悕鈥�.com/ok鐩綍
      
      
//    return new Response(JSON.stringify({
//      message: "This is the response for /ok path"
//    }), {
//      headers: { 'content-type': 'application/json' }

  }
}

async function formatResponse(response) {
  const text = await response.text(); // 获取原始文本响应
  const decodedText = decodeURIComponent(text); // 对整个文本进行解码
  const data = JSON.parse(decodedText); // 解析解码后的文本为JSON
  // 现在data是一个对象或数组，您可以根据需要进行进一步的处理
  return data;
}

```
## 主要api 
response = requests.put(
    f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/services/{workers_id}/environments/production/content",
    headers=headers,
    data=body.encode()
)
    
https://dash.cloudflare.com/f9dda5fd18bd0122b4c46f878e11b001/workers/services/view/dawn-sky-f8a8/production

# 对于在
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/IMG_20240609_232414.jpg)
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/IMG_20240609_232451.jpg)
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/IMG_20240609_232517.jpg)

# https://dash.cloudflare.com/?to=/:account/workers-and-pages/  
# 中，左侧菜单栏，打开worker之后，长按 或右键一个worker，链接长这样
https://dash.cloudflare.com/f9dda5fd18bd0122b4c46f878e11b001/workers/services/view/dawn-sky-f8a8/production

account_identifier = ''
service_name = ''

cf_token = ''
# f9dda5fd18bd0122b4c46f878e11b001 填写到 account_identifier
# dawn-sky-f8a8 填写到 service_name
 # token 填写到cf_token https://dash.cloudflare.com/profile/api-tokens 
# 申请
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_214722.jpg)
选择 编辑cloudflare workers类型 ，按默认，下面的选择自己邮箱即可
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/IMG_20240609_234128.jpg)
生成完

_________________________________________________________________________
## 1. 其中f9dda5fd18bd0122b4c46f878e11b001 是用户id，而这个id，其实只要在
## https://dash.cloudflare.com/?to=/:account/workers-and-pages/
## 页，网页链接中就一直跟着 dash.cloudflare.com/f9dda5fd18bd0122b4c46f878e11b001 
这个就是所有网页的前缀，所以直接访问 dash.cloudflare.com ，然后复制后半这串数字字母就可以了

# 2. worker的名字 dawn-sky-f8a8
在workers主页面内，访问 
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_223255.jpg)
https://dash.cloudflare.com/?to=/:account/workers-and-pages/ 左侧栏点击workers，就可以看到
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_223832.jpg)
同时创建worker时候，也看得到

# 3. api token 同样在worker主页面，下滑，
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_223818.jpg)
# 这里有一个管理API令牌的按钮
同时可以看到，用户id就写明了是之前提到的，dash.cloudflare.com主页面后跟着的那一串
## 也可以直接在
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_223300.jpg)
## 主页dash.cloudflare.com  右上角头像，点击个人简介，第一个，带邮箱那个按钮，然后也是这个api token申请页面
选择申请workers的
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/Screenshot_20240609_233817.jpg)
![Image text](https://raw.githubusercontent.com/Map987/cloudflare-workers-worker.js-uploader/main/Screenshot_20240609_214722.jpg) 即可

## 查看worker网站地址
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/IMG_20240609_232517.jpg)
workers 页面，点击一个进去。
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/Screenshot_20240609_235553.jpg)
点击设置 ，点击第二个 trigger 触发器
![Image text](https://github.com/Map987/cloudflare-workers-worker.js-uploader/raw/main/Screenshot_20240609_234403.jpg)
同时在创建worker的时候也有，步骤2. 中点击create即是这个页面

