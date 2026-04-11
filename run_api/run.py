import requests

BASE_URL = "http://localhost:8000"

def test_info():
    print("------------ Testing GET / ------------")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")

def test_health():
    print("------------ Testing GET /health ------------")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")

def test_predict(text):
    print("------------ Testing POST /predict ------------")
    print(f"Input text: '{text}'")
    try:
        payload = {"text": text}
        response = requests.post(f"{BASE_URL}/predict", json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}\n")
        else:
            print(f"Error Response: {response.text}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")

def test_generate(text):
    print("------------ Testing POST /generate ------------")
    print(f"Input text: '{text}'")
    try:
        payload = {"text": text}
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}\n")
        else:
            print(f"Error Response: {response.text}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")

if __name__ == "__main__":
    print("Vui lòng bật API Server trước khi chạy.\n")
    test_info()
    test_health()
    
    test_text_positive = "Sản phẩm này rất tốt, dịch vụ cũng tuyệt vời. Tôi rất hài lòng."
    test_predict(test_text_positive)
    
    test_text_negative = "Chất lượng quá kém, không đáng tiền mua."
    test_generate(test_text_negative)