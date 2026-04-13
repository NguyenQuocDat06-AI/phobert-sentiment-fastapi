# PhoBERT Sentiment Analysis API

API phân tích cảm xúc văn bản tiếng Việt sử dụng mô hình PhoBERT.

## Video Demo

[![Video Demo](https://img.youtube.com/vi/h_EUwWVAUfs/maxresdefault.jpg)](https://youtu.be/h_EUwWVAUfs)

---

## Thông tin sinh viên

- **MSSV**: 24120282
- **Họ tên**: Nguyễn Quốc Đạt
- **Lớp**: 24CTT3

---

## Tên mô hình và liên kết HF

- **Tên mô hình**: `phobert-base-vietnamese-sentiment`
- **Liên kết HF**: https://huggingface.co/wonrax/phobert-base-vietnamese-sentiment

---

## Mô tả mô hình

PhoBERT là một mô hình ngôn ngữ lớn được huấn luyện trên dữ liệu văn bản tiếng Việt. Nó được phát triển bởi Viện Nghiên cứu Trí tuệ Nhân tạo Quốc gia Việt Nam (VINAI) và là phiên bản tiếng Việt của mô hình RoBERTa.

---

### Yêu cầu

- Python 3.8+
- pip

### Cách 1: Cài đặt tự động bằng Makefile

Lệnh này sẽ tự động tạo môi trường ảo và cài đặt các thư viện cần thiết:
```bash
make setup
```

### Cách 2: Cài đặt thủ công

**Tạo và định dạng môi trường ảo:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Cài đặt thư viện:**
```bash
pip install -r requirements.txt
```

---

## Khởi động server

```bash
make run
```
*(Hoặc chạy thủ công: `py src/api.py`)*

## Chạy API

**1. GET /**

```bash
curl.exe http://localhost:8000/
```
**Response:**
```json
{
  "name_model": "PhoBERT Sentiment Analysis",
  "description": "API phân tích cảm xúc văn bản tiếng Việt sử dụng mô hình PhoBERT.",
  "version": "1.0.0",
  "author": "NguyenQuocDat"
}
```

**2. GET /health**

```bash
curl.exe http://localhost:8000/health
```
**Response:**
```json
{
  "status": "healthy",
  "message": "Hệ thống đang hoạt động bình thường!",
  "model_loaded": true
}
```

**3. POST /predict**

```bash
curl.exe -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"text\": \"Sản phẩm này rất tốt, dịch vụ cũng tuyệt vời. Tôi rất hài lòng.\"}"
```
**Response:**
```json
{
  "label": "POS",
  "score": 0.9929381012916565
}
```

**4. POST /generate**

```bash
curl.exe -X POST http://localhost:8000/generate -H "Content-Type: application/json" -d "{\"text\": \"Chất lượng quá kém, không đáng tiền mua.\"}"
```
**Response:**
```json
{
  "label": "NEG",
  "score": 0.9873239994049072
}
```

## TEST hệ thống

```bash
make test
```
*(Hoặc chạy thủ công: `python run_api/run.py`)*

---

## Cấu trúc dự án

```
phobert-sentiment-fastapi/
├── .venv/                   # Môi trường ảo
├── models/                  # Mô hình PhoBERT
│   ├── model.onnx
│   ├── tokenizer.json
│   ├── vocab.txt
│   └── config.json
├── src/                     # Code model
│   ├── api.py
│   └── main.py
├── run_api/                 # TEST API
│   └── run.py
├── requirements.txt         # Các thư viện cần thiết
└── README.md                # Tài liệu này
```

