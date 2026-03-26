# --- 第 2 天：列表(List) 与 字典(Dict) 实战 ---

# 1. 列表 (对应 JS 的 Array)
from datetime import datetime
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # 对应 JS 的 push()
print(f"我的水果清单: {fruits}") # f-string 是 Python 的模板字符串 (类似 `...`)

# 2. 字典 (对应 JS 的 Object / JSON)
# 提示：Python 的字典 Key 必须加引号，且不支持 user.name 这种点语法
user = {
    "name": "ChenMing",
    "role": "Frontend Developer",
    "level": 4
}
print(f"用户姓名: {user["name"]}") # 必须用["key"]访问

# 3. 循环遍历 (非常直观)
print("\n--- 开始遍历数据 ---")
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

for item in users: 
    print(f"ID: {item["id"]}, 姓名: {item["name"]}")

# 4. Python 的“绝活”：列表推导式 (List Comprehension)
# 任务：把 [1, 2, 3] 变成 [2, 4, 6]

numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers] # 这行代码相当于 JS 的 numbers.map(x => x * 2)
print(f"翻倍后的数字: {doubled}")

# 1. 定义嵌套数据（模拟一个 AI 会话数据）
ai_session = {
    "user_id": 1024,
    "model": "gpt-4o",
    "is_active": True,  # 注意：首字母大写，对应 JS 的 true
    "history": [
        {"role": "user", "content": "你好，你是谁？"},
        {"role": "assistant", "content": "我是你的 AI 助手。"}
    ]
}

# 2. 查 (Access)
# 注意：Python 字典不支持 ai_session.user_id 这种点语法，必须用 ['key']
print(f"当前用户: {ai_session['user_id']}")
print(f"第一条对话: {ai_session['history'][0]['content']}")

# 3. 增 (Add)
ai_session["tokens"] = 500  # 直接赋值即新增
ai_session["history"].append({"role": "user", "content": "帮我写段代码"}) # append = push

# 4. 改 (Update)
ai_session["model"] = "claude-3.5"

# 5. 删 (Delete)
del ai_session["is_active"] # 或者用 .pop("is_active")

# 6. 遍历 (Loop)
print("\n--- 打印对话历史 ---")
for msg in ai_session["history"]:
    # 这里的 msg 相当于 JS 里的 item
    role = msg["role"].upper()
    content = msg["content"]
    print(f"[{role}]: {content}")

# 7. 一个前端会觉得很爽的特性：切片 (Slicing)
# 快速获取列表的前 2 个元素
first_two = ai_session["history"][:2]
print(f"\n前两条数据条数: {len(first_two)}")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{nums[3:7]}")

# 列表：可以变
my_list = ["Vue", "React"]
my_list[0] = "Next.js" # 没问题

# 元组：不可变
my_tuple = ("Vue", "React")
# my_tuple[0] = "Next.js"  # <--- 这里会直接报错：TypeError

# 模拟一个坐标
point = (120.1, 30.2)

# 解构赋值 (Destructuring)
longitude, latitude = point 

print(f"经度: {longitude}, 纬度: {latitude}")


# --- 元组 (Tuple) 练习 ---

# 1. 定义一个 AI 模型的配置 (只读)
model_config = ("gpt-4o", 0.7, 2000) # (模型名, 随机度, 最大长度)

# 2. 尝试修改 (取消下面这行的注释看看报错)
# model_config[1] = 0.5 

# 3. 巧妙用法：快速交换变量 (JS 里需要解构或者中间变量)
a = "User"
b = "AI"
a, b = b, a  # 这一行其实就是利用了元组
print(f"a 现在是: {a}, b 现在是: {b}")

# 4. 函数返回多个值 (其实返回的是一个元组)
def get_ai_status():
    return "Connected", "200ms"

status, latency = get_ai_status()
print(f"状态: {status}, 延迟: {latency}")

# 1. 模拟从 PDF 提取出的原始关键词 (有重复)
raw_keywords = ["AI", "RAG", "Python", "AI", "Vector"]

# 2. 去重 (利用 Set)
unique_keywords = list(set(raw_keywords))

# 3. 封装成字典 (Dict)
document_info = {
    "title": "我的 AI 学习笔记",
    "tags": unique_keywords,
    "version": (1, 0, 2)  # 版本号用元组，不允许修改
}

# 4. 打印最后两个标签 (利用切片)
print(f"最后的标签: {document_info['tags'][-2:]}")

def greet(name, role="User"):
    # 注意冒号 : 和 4个空格的缩进
    if name:
        return f"Hello, {name}"
    return "Hello, Guest" # 缩进结束，if 也就结束了

def send_msg(content, role, model="gpt-4"):
    print(f"[{model}] {role}: {content}")

# 1. 位置参数 (Positional): 必须按顺序
send_msg("你好", "user") 

# 2. 关键字参数 (Keyword): 顺序可以乱，可读性极强
send_msg(role="admin", content="重启系统", model="claude-3")

def ai_orchestrator(task, *tools, **config):
    print(f"任务: {task}")
    print(f"使用的工具列表: {tools}") # 这是一个元组
    print(f"模型配置: {config}")      # 这是一个字典

# 调用
ai_orchestrator(
    "解析文档", 
    "PDFLoader", "OCR-Tool", "TextSplitter", # 这三个会被 *tools 收集
    model="gpt-4o", temperature=0, stream=True # 这些会被 **config 收集
)

score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60: # 对应 JS 的 else if
    print("及格")
else:
    print("不及格")

def format_ai_response(content, status_code=200, **metadata):
    meta_str = ",".join([f"{k}: {v}" for k,v in metadata.items()])
    if status_code == 200:
        return f"内容: {content.upper()},元数据: [{meta_str}]"
    else: return "Error"

result = format_ai_response("Hello AI", model="gpt-4", usage=150, gender='man', age=25)
print(result)

# 1. 读取文本文件（对标 fs.readFile）
# 读取 txt / md 文件
# with open("test.txt", "r", encoding="utf-8") as f:
#     content = f.read()

print(content)

import json # 1. 必须先导入内置的 json 库

# 2. 写入文本文件（对标 fs.writeFile）
# 覆盖写入
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("我是写入的内容\n换行")

# 追加写入
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("追加内容")

# 准备一个典型的 AI 配置字典
config = {
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": True
}

# --- 任务 1: 把字典存进 json 文件 ---
with open("config.json", "w", encoding="utf-8") as f:
    # json.dump (没有 s) 是直接把对象“甩”进文件流
    # indent=4 让生成的 JSON 像 VSCode 格式化过一样漂亮
    json.dump(config, f, indent=4)
    print("✅ config.json 已创建！")

# --- 任务 2: 从 json 文件读回数据 ---
with open("config.json", "r", encoding="utf-8") as f:
    # json.load (没有 s) 是直接从文件流里解析出字典
    new_config = json.load(f)
    print(f"读取到的模型是: {new_config['model']}")
    
res_str = format_ai_response("Hello AI", model="a", usage=150, gender='man', age=25)

# 使用 "a" 模式（Append 追加），配合 f.write()
with open("chat.log", "a", encoding="utf-8") as f:
    # 记得加 \n，否则下一条日志会跟这一条连在一起
    f.write(res_str + "\n")
    print("✅ 日志已追加到 chat.log！")

# 1. 整体导入 (类似 const fs = require('fs'))
import json
json.dumps({})

# 2. 部分导入 (类似 import { readFile } from 'fs')
from os import path
if path.exists("chat.log"):
    print("日志文件存在")

# 3. 别名导入 (类似 import * as api from './api')
import datetime as dt
print(dt.datetime.now())

import json
import os

def load_ai_config(file_path):
    try:
        # 1.尝试读取
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # 2. 处理“文件找不到了”
        print(f"⚠️ 找不到 {file_path}，正在创建默认配置...")
        default_config = {"model": "gpt-4", "temp": 0.7}
        # 顺手创建一个默认的
        with open(file_path, "w") as f:
            json.dump(default_config, f)
        return default_config
    except json.JSONDecodeError:
        # 3. 处理“文件内容坏了”（比如你手抖在 JSON 里多写了个逗号）
        print(f"❌ {file_path} 格式损坏！请检查 JSON 语法。")
        return None
    except Exception as e:
        # 4. 兜底方案
        print(f"发生了意外错误: {e}")
        return None
    finally:
        # 无论如何都会执行
        print("运行结束")
# --- 调用测试 ---
config = load_ai_config("ai_config.json")
if config:
   print(f"🚀 准备就绪，当前模型: {config['model']}")

import datetime
import json
def save_log(message):
    try:
        now = datetime.datetime.now()
        # 格式化一下时间，不然默认格式太长了
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("app.log", 'a', encoding="utf-8") as f:
            f.write(f"[{time_str} {message}\n]")
        print(f"✅ 日志已记录: {message}")
    except FileNotFoundError:
        print("⚠️ 文件夹路径不存在")
    except json.JSONDecodeError:
      # 这里的 e 会抓住所有的错误（包括刚才的传参错误）
        print(f"发生了意外错误: {type(e).__name__} - {e}")
        return None
    except Exception as e:
          # 4. 兜底方案
        print(f"发生了意外错误: {e}")
        return None

# --- 测试一下 ---
save_log("用户陈明启动了 AI 助手")
save_log("正在连接 OpenAI 接口...")

# 第 2 周 类
class AIChat:
    # 1. 构造函数 (注意是双下划线)
    def __init__(self, mode_name, temp = 0.7):
        self.model = mode_name  # 相当于 this.model = model_name
        self.temp = temp
        self.history = []
    
    # 2. 类的方法 (第一个参数必须写 self)
    def ask(self, question):
        self.history.append(question)
        print(f"正在使用 {self.model} (温度:{self.temp}) 回答: {question}")

# --- 使用方式 ---
# 注意：不需要 new 关键字！
my_bot = AIChat("gpt-4o", temp=0.5)
my_bot.ask("什么是 RAG？")

# 基类 (Base Class)
class BaseBot:
    def greet(self):
        print("你好，我是 AI 助手")

# 派生类 (Subclass) - 继承 BaseBot
class ProBot(BaseBot):
    def __init__(self, name):
        self.name = name
    
    # 重写方法
    def greet(self):
        super().greet() # 调用父类方法
        print(f"我是高级版 {self.name}")

# --- 使用方式 ---
pro = ProBot("大圣")
pro.greet()

class AIRecorder:
    def __init__(self, user_name, log_file = "chat.log"):
        self.user_name = user_name
        self.log_file = log_file

    def add_log(self, msg):
        now = datetime.datetime.now()
        # 格式化一下时间，不然默认格式太长了
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a', encoding="utf-8") as f:
            f.write(f"[{time_str} {self.user_name} {msg}]\n")
        print(f"✅ 已记录")

    def read_logs(self):
        print(f"--- 正在读取 {self.log_file} ---")
        try:
            with open(self.log_file, 'r', encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("⚠️ 还没有任何日志记录。")
# --- 🚀 运行验证 ---
recorder = AIRecorder("ChenMing") # 使用默认的 chat.log

# 模拟记录两条对话
recorder.add_log("启动 AI 助手")
recorder.add_log("发送了一个 RAG 请求")

# 读取并展示结果
recorder.read_logs()

from typing import Optional

def get_ai_response(prompt: str, max_tokens: int = 100) -> str:
    # prompt: str 表示参数必须是字符串
    # -> str 表示返回值必须是字符串
    print(f"AI 对 {prompt} 的回答")
    return f"AI 对 {prompt} 的回答"

from pydantic import BaseModel, Field
# 1. 定义一个“数据模型”，就像 TS 的 interface
class AIMessage(BaseModel):
    role: str                       # 必须是字符串
    content: str                    # 必须是内容
    timestamp: float                # 必须是浮点数
    tags: list[str] = []            # 默认是空列表
    score: Optional[float] = None   # 可选字段

# 2. 实战：数据校验
# 假设这是从 API 收到的原始 JSON 字典
raw_data = {
    "role": "assistant",
    "content": "你好！",
    "timestamp": 1711395600.0
}

# 3. 实例化（会自动校验数据类型！）
msg = AIMessage(**raw_data) # 还记得 ** 展开字典吗？
# 如果 raw_data 里的 timestamp 传了个字符串 "abc"，Pydantic 会直接报错！
print(f"角色: {msg.role}, 内容: {msg.content}")

class AppConfig(BaseModel):
    app_name: str
    version: float
    api_key: str
    is_pro: bool = False

data = {
    "app_name": "MyAI", 
    "version": 1.0, 
    "api_key": "sk-xxx"
}

appData = AppConfig(**data)
print(f"应用: {appData.app_name}, 版本: {appData.version}")

import requests

url = "https://httpbin.org/get"

# 带参数
params = {
    "name": "chenming",
    "age": 25
}

resData = requests.get(url, params=params)
data = resData.json()  # 自动转字典 = resData.data
print(data)

url = "https://httpbin.org/post"

# 请求体
payload = {
    "username": "admin",
    "password": "123456"
}

# 发送 JSON
res = requests.post(url, json=payload)
data = res.json()

print(data)

# 带 Token 请求
url = "https://your-llm-api.com/chat"

headers = {
    "Authorization": "Bearer sk-xxxxxxxxxxxx",
    "Content-Type": "application/json"
}

payload = {
    "model": "qianfan",
    "messages": [{"role": "user", "content": "你好"}]
}

res = requests.post(url, headers=headers, json=payload)
print(res.json())

print(res.status_code)

def call_mock_ai_api(prompt: str):
    # 1. 准备请求地址 (这是个模拟地址)
    url = "https://httpbin.org/post"

    # 2. 准备 Headers (对应 axios 的 config.headers)
    headers = {
        "Authorization": "Bearer sk-your-token-123",
        "Content-Type": "application/json"
    }

    # 3. 准备 Body (对应 axios 的 data)
    # 💡 关键：用 json= 参数，requests 会自动帮你做 JSON.stringify()
    payload = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
           # 6. 解析数据 (对应 res.data)
            data = response.json()
            # httpbin 会把我们发过去的内容原样返回在 'json' 字段里
            print(f"✅ 成功连接 API，发送的内容是: {data['json']['messages'][0]['content']}")
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # 捕获网络超时、断网等错误
        print(f"📡 网络连接异常: {e}")

# --- 测试一下 ---
call_mock_ai_api("帮我写一个 Python 爬虫")
if result:
    print("\n--- API 返回结果 ---")
    print(result)

def call_ai_api(format: str):
    # 1. 准备请求地址 (这是个模拟地址)
    url = "https://api.ipify.org"
    params = {
        "format": format
    }
    try:
        # 加上 timeout 是好习惯，防止程序死等
        res = requests.get(url, params=params, timeout=5)
        
        # 2. 如果是 json 模式，直接返回解析后的字典
        if format == "json":
            return res.json()  # 相当于 JSON.parse(res.data)
        
        return res.text
    except Exception as e:
        return f"请求出错了: {e}"

# --- 调用 ---
data = call_ai_api("json")
# 像访问 JS 对象一样（只是改用方括号）
if isinstance(data, dict):
    print(f"🌍 你的公网 IP 是: {data['ip']}")
else:
    print(data)