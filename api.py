from fastapi import FastAPI, Query  # pyre-ignore
from pydantic import BaseModel, Field # pyre-ignore
from typing import Optional # pyre-ignore
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

app = FastAPI()

# 1. 定义 Request Body (对应 TS Interface)
class ChatRequest(BaseModel):
    # Field 可以设置校验规则，比如字符串长度、示例等
    message: str = Field(..., min_length=1, max_length=500, description="用户的提问内容")
    model: str = Field(default="gpt-4o", description="使用的 AI 模型")
    temperature: float = Field(default=0.7, ge=0, le=2.0) # ge: >=, le: <=

# 编写POST接口
@app.post('/chat')
async def chat_endpoint(data: ChatRequest):
    # FastAPI 已经帮你校验好了：
    # - data.message 绝不会为空
    # - data.temperature 绝不会大于 2.0
    print(f"使用模型{data.model} 处理: {data.message}")
    
    return {
        "reply": f"你刚才说的是：{data.message}吗？",
        "config": {"temp": data.temperature}
    }

# 编写带 Query 参数的接口 (查询历史记录)
@app.get("/history")
async def get_history(user_id: int, limit: int = Query(default=10, lt=100) ): # limit 默认 10，必须小于 100
    return {
        "user_id": user_id,
        "limit": limit,
        "data": ["msg1", "msg2"]
    }
    
# 4. 启动逻辑 (虽然通常用命令行启动，但写在代码里也行)
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)


# 跨域 + 登录 + 鉴权拦截
import time
import jwt # pyre-ignore
from fastapi import fastapi, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware # pyre-ignore
from pydantic import BaseModel
# 下面这两个是为了让 Swagger UI 右上角出现“Authorize 小锁”的魔法包
from fastapi.security import OAuth2PasswordBearer # pyre-ignore
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

app = FastAPI(title="ChenMing 的 AI 助手后端")

# ==========================================
# 1. 跨域配置 (平替 Express 的 app.use(cors()))
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], # 前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# 2. JWT 配置区
# ==========================================
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# 开启 Swagger 的 HTTP Bearer 认证 (小锁魔法)
security = HTTPException()

# ==========================================
# 3. 登录接口 (平替 jwt.sign)
# ==========================================
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post('/login', tag=["认证"])
async def login(data: LoginRequest):
    # 模拟数据库校验
    if data.username == "chenming" and data.password == "123456":
        # 签发 Token
        payload = {
            "sub": data.username,
            "exp": int(time.time()) + 3600 # 1小时后过期
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"code": 200, "token":token, "msg":"登录成功"}
    return HTTPException(status_code=401, detail="账号或密码错误")

# ==========================================
# 4. 鉴权中间件 / 拦截器 (平替 jwt.verify)
# ==========================================
async def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # 这里的 credentials.credentials 已经自动帮你去掉了 "Bearer " 前缀
    token = credentials.credentials

    try:
        # 解析 Token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload #成功则返回用户信息
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token 已过期")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token 无效")

# ==========================================
# 5. 受保护的接口 (平替 router.get('/xxx', authMiddleware, ...))
# ==========================================