import requests
import time
import random
from fake_useragent import UserAgent  # 新增：随机UA库

# 要保活的项目 + 它们的静态资源路径（伪装真实访问）
TARGETS = {
    "https://qklm.xyz": ["/css/main.css", "/js/app.js"],
    "https://wyb.qklm.xyz": ["/img/logo.png", "/css/theme.css"]
}

ua = UserAgent()  # 随机UA生成器

while True:
    for url, assets in TARGETS.items():
        try:
            # 1. 模拟真实浏览器请求头
            headers = {
                "User-Agent": ua.random,  # 随机UA，避免固定标识
                "Referer": "https://www.google.com/search?q=qklm",  # 模拟从搜索页跳转
                "Accept": "text/html,application/xhtml+xml"
            }
            
            # 2. 访问主页（模拟用户进入网站）
            response = requests.get(url, headers=headers, timeout=10)
            print(f"访问 {url} 成功，状态码: {response.status_code}")
            
            # 3. 随机加载1-2个静态资源（模拟用户浏览时加载CSS/JS/图片）
            if assets:
                asset_url = random.choice(assets)
                requests.get(url + asset_url, headers=headers, timeout=5)
                print(f"  - 加载静态资源 {asset_url} 成功")
            
            # 4. 随机延迟（1-3秒，模拟用户阅读内容的时间）
            time.sleep(random.uniform(1, 3))
            
        except Exception as e:
            print(f"访问 {url} 失败: {str(e)}")
    
    # 每10-12分钟重复（增加随机间隔，避免机械定时）
    time.sleep(random.randint(600, 720))
