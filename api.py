from fastapi import FastAPI  # pyre-ignore
from pydantic import BaseModel # pyre-ignore
import uvicorn

# 1. 创建应用实例
app = FastAPI(title="ChenMing 的 AI 助手后端")

# 2. 定义一个简单的 GET 路由 (对应 Express 的 app.get)
@app.get("/")
async def root():
    return {"message": "Hello AI World", "status": "online"}

# 3. 定义一个带参数的路由 (还记得 Pydantic 吗？这里直接用类型提示)
@app.get("/hello/{name}")
async def asy_hello(name: str):
    return {"message": f"你好， {name}!准备好调 AI 了吗？"}

# 4. 启动逻辑 (虽然通常用命令行启动，但写在代码里也行)
if __name__ == "__api__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

# 1. 定义数据结构 (类似 TS Interface)
class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# 2. 按照规律写路由
@app.post("/chat")
async def chat(data: ChatRequest):  # FastAPI 看到 BaseModel 就会去解析 Request Body
    # 3. 逻辑处理
    print(f"收到用户提问: {data.prompt}")
    return {"reply": f"你刚才说的是：{data.prompt}吗？", "usage": data.max_tokens}