from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to ["http://localhost:3000"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class ScrapeRequest(BaseModel):
    url: str
    identifier: str
    type: str  # "id" or "class"

@app.post("/scrape")
def scrape_website(request: ScrapeRequest):
    try:
        response = requests.get(request.url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        if request.type == "id":
            result = soup.find(id=request.identifier)
        elif request.type == "class":
            result = soup.find_all(class_=request.identifier)
        else:
            return {"error": "Invalid type. Use 'id' or 'class'."}

        if request.type == "class":
            if result:
                pretty_results = [item.prettify() for item in result]
                return {"data": pretty_results}
            else:
                return {"data": "No data found."}

        return {"data": result.prettify() if result else "No data found."}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
