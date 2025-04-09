from pydantic import BaseModel
class Claim(BaseModel):
    wind:float
    rain:float
    area:float