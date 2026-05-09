from fastapi import FastAPI

app = FastAPI()

users = {}

@app.get("/")
def home():
    return {"message": "Crowdsourcing Platform Active"}

@app.post("/reward/{username}")
def reward_user(username: str):
    if username not in users:
        users[username] = 0

    users[username] += 5

    return {
        "user": username,
        "points": users[username]
    }