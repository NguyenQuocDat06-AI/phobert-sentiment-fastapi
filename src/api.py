import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager
from main import Emoji

emoji_model = None
model_loaded = False

@asynccontextmanager
async def lifespan(app: FastAPI):
    global emoji_model, model_loaded
    try:
        emoji_model = Emoji("wonrax/phobert-base-vietnamese-sentiment")
        emoji_model.load_model()
        model_loaded = True
    except Exception as e:
        print(f"Lỗi khi load model: {e}")
        model_loaded = False
    yield
    # Giải phóng khi ứng dụng tắt
    emoji_model = None

app = FastAPI(lifespan=lifespan)

class PredictRequest(BaseModel):
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=2000, 
        description="Văn bản tiếng Việt phân tích cảm xúc (không được để trống)."
    )

@app.get("/")
def info():
    return {
        "name_model": "PhoBERT Sentiment Analysis", 
        "description": "API phân tích cảm xúc văn bản tiếng Việt sử dụng mô hình PhoBERT.",
        "version": "1.0.0", 
        "author": "NguyenQuocDat"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy" if model_loaded else "unhealthy",
        "message": "Hệ thống đang hoạt động bình thường!" if model_loaded else "Mô hình chưa được load thành công!",
        "model_loaded": model_loaded
    }

@app.post("/predict")
def predict(request: PredictRequest):
    return emoji_model.predict(request.text)

@app.post("/generate")
def generate(request: PredictRequest):
    return emoji_model.predict(request.text)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)