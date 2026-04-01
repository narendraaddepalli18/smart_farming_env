from pydantic import BaseModel

class Observation(BaseModel):
    crop: str
    price_today: int
    predicted_price: int
    weather: str

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    value: float