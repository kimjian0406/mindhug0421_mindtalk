from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()
    print("✅ 웹훅 수신 성공!")
    print(data)
    return {"ok": True}

