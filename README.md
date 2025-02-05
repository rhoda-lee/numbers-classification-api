# Number Classification API

A FastAPI-based web service that classifies numbers based on their mathematical properties and provides a fun fact about them

## Features
- Determines if a number is **prime** or **perfect**
- Identifies **Armstrong numbers**
- Checks if a number is **odd or even**
- Computes the **digit sum**
- Fetches a **fun fact** about the number from the Numbers API

## Technology Stack
- **FastAPI** (Backend Framework)
- **Uvicorn** (ASGI Server)
- **Requests** (For fetching fun facts)
- **Postman** (For API testing)

---

## Project Structure
```yaml
/number-classification-api<br>
│── app.py               # Main application file 
│── utils.py             # Utility functions for number classification
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── LICENSE              # License of the repository
```

---

## Installation & Setup

### Clone the Repository
```sh
git clone https://github.com/rhoda-lee/numbers-classification-api.git
cd numbers-classification-api
```

### Create & Activate a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the FastAPI Server
```bash
uvicorn app:app --reload
Your API will be live at: http://127.0.0.1:8000
```

## Usage
### Classify a Number
Send a GET request to:
```bash
http://127.0.0.1:8000/api/classify-number?number=371
```
- Example Response (200 OK)
```json

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
- Example Response (400 Bad Request)
```json

{
    "detail": {
        "number": "abc",
        "error": true,
        "message": "value is not a valid integer"
    }
}
```

## Deployment
### Deploy to Railway
- Push your code to GitHub
- Create a new FastAPI service on Render
- Set the Start Command as
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

- Deploy and get your public API URL

## Running Tests
- Use Postman or cURL to test the API.
```bash
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

## Security & CORS Handling
- CORS is enabled using FastAPI's built-in middleware.
>Ensure that your deployment service allows CORS.

## Contributing
- Fork the repository.
- Create a new branch.
- Make your changes and commit.
- Open a Pull Request


## 👩🏽‍💻 Author
- [Rhoda Oduro-Nyarko](https://www.linkedin.com/in/rhoda-oduro-nyarko/)
- [GitHub Profile](https://github.com/rhoda-lee)