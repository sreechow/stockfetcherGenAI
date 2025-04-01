import requests
import json
import sys
sys.path.append('.')
from api.utils.savedata import save_to_json

def test_getstocks():
    response = requests.get("http://127.0.0.1:5000/stocks/google")
    print(response.text, response.status_code)
    #save_to_json(response.text)
    data = json.loads(response.text)
    print(data)
    assert response.status_code == 200
    # Add more assertions to check response data

def test_top10projections():
    sector = "healthcare"
    response = requests.get("http://127.0.0.1:5000/stocks/top10projections?sector=Healthcare") #http://localhost:5000/top10projections?sector=Healthcare

    print(response.text, response.status_code)
    save_to_json(response.text)
    data = json.loads(response.text)
    print(data)

    assert response.status_code == 200

def test_post_endpoint():
    data = {"key": "value"}
    response = requests.post("http://your-idx-url:your-port/your-endpoint", json=data)
    assert response.status_code == 201  # Or 200, depending on your API
    # Add more assertions to check response data


def test_upload_vectors():
    data = {"file_path": "https://s201.q4cdn.com/141608511/files/doc_financials/2024/ar/NVIDIA-2024-Annual-Report.pdf"}
    response = requests.post("http://127.0.0.1:5000/stocks/create_vector_store", json=data)
    assert response.status_code == 201  # Or 200, depending on your API


test_upload_vectors()
