from fastapi import FastAPI, Query, HTTPException
import requests
from utils import NumberUtils

app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com"

@app.get('/api/classify-number')
def classify_number_api(number: int = Query(..., description='The number to classify')):
    try:
        # check the properties
        prime_status = NumberUtils.is_prime(number)
        perfect_status = NumberUtils.is_perfect(number)
        properties = NumberUtils.classify_number(number)

        # fetching fun fact from Numbers API
        response = requests.get(f'{NUMBERS_API_URL}/{number}/math')
        fun_fact = response.text if response.status_code == 200 else 'No fun fact found'

        # json response
        return {
            "number": number,
            "is_prime": prime_status,
            "is_perfect": perfect_status,
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(abs(number))),
            "fun_fact": fun_fact
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail={
            "number": number,
            "error": True,
            "message": str(e)
        })
