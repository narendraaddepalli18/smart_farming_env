from fastapi import FastAPI
from env import FarmEnv
from grader import grade

app = FastAPI()

env = FarmEnv()

@app.get("/")
def home():
    return {"message": "Smart Farming API is running 🚀"}

@app.get("/reset")
def reset():
    return env.reset()

@app.get("/state")
def get_state():
    return env.state()

@app.get("/step/{action}")
def step(action: str):
    state, reward, done, _ = env.step(action)
    score = grade(env)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "score": score
    }