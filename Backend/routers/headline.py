from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas, crud
from ai_service import analyze_headline

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/analyze", response_model=schemas.HeadlineResponse)
def analyze(data: schemas.HeadlineCreate, db: Session = Depends(get_db)):

    classification, explanation = analyze_headline(data.headline)

    crud.create_headline(
        db,
        data.headline,
        classification,
        explanation
    )

    return {
        "headline": data.headline,
        "classification": classification,
        "explanation": explanation
    }


@router.get("/history")
def history(db: Session = Depends(get_db)):
    return crud.get_headlines(db)
