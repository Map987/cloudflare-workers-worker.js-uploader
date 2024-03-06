# cloudflare-workers-worker.js-uploader
api upload cloudflare worker.js from txt
cloudflare workers上传使用api 
前往 cloudflare 网站，然后在 workers 页面中复制链接 例如 https://dash.cloudflare.com/f……/workers/services/view/xxx-xxx-xxx-xxx/production 
将 f…… 放入 account_identifier 
将 xxx-xxx-xxx-xxx 放入 service_name 在 workers 页面创建 token 后，
将 token 如 Qj… 放入 cf_token


go the cloudflare website than copy the link when in the workers page
like
https://dash.cloudflare.com/f……/workers/services/view/xxx-xxx-xxx-xxx/production 
put f…… into account_identifier
put xxx-xxx-xxx-xxx into service_name
put token like Qj... into cf_token after create token in workers page


account_identifier = ''
service_name = ''
 cf_token = ''

https://community.cloudflare.com/t/how-to-update-worker-js-via-api/556768
https://community.cloudflare.com/t/example-how-to-api-upload-a-worker-script-no-wrangler/447660
