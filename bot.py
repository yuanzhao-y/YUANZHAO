import requests

# 替换成你自己的 DeepSeek API Key（去 platform.deepseek.com 注册免费拿）
API_KEY = "sk-0b8b4f8d54a441798849afe2540e8f34"
URL = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("机器人已启动，输入 quit 退出")
while True:
    user_input = input("你: ")
    if user_input.lower() == "quit":
        break
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_input}]
    }
    response = requests.post(URL, headers=headers, json=data)
    reply = response.json()["choices"][0]["message"]["content"]
    print(f"机器人: {reply}")