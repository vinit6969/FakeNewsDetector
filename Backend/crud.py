from sqlalchemy.orm import Session
import models

def create_headline(db: Session, headline, classification, explanation):
    db_headline = models.Headline(
        headline=headline,
        classification=classification,
        explanation=explanation
    )
    db.add(db_headline)
    db.commit()
    db.refresh(db_headline)
    return db_headline


def get_headlines(db: Session):
    return db.query(models.Headline).order_by(models.Headline.id.desc()).all()