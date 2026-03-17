from pydantic import BaseModel

class HeadlineCreate(BaseModel):
    headline: str

class HeadlineResponse(BaseModel):
    headline: str
    classification: str
    explanation: str

    class Config:
        from_attributes = True