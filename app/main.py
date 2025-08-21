from fastapi import FastAPI
import os
from app.fetcher import Dal
from app.manager import JsonBuilder
import uvicorn
#uri = os.environ.get("URI")

# db = os.environ.get("DATABASE")

data = Dal(uri, db)
df = data.get_all_data()
my_json = JsonBuilder(df, "data/weapon_list.txt" ).get_json()

app = FastAPI()

@app.get("/")
def read_data():
    return my_json


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8080)
