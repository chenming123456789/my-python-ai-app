# --- 第 2 天：列表(List) 与 字典(Dict) 实战 ---

# 1. 列表 (对应 JS 的 Array)
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