from models.activity import Activity
from schemas.activity import ActivityCreate, ActivityUpdate
from sqlalchemy.orm import Session


class ActivityRepository:
    def get_activity(self, db: Session, activity_id: int) -> Activity:
        return db.query(Activity).filter(Activity.id == activity_id).first()

    def create_activity(self, db: Session, activity: ActivityCreate) -> Activity:
        db_activity = Activity(**activity.model_dump())
        db.add(db_activity)
        db.commit()
        db.refresh(db_activity)
        return db_activity

    def update_activity(self, db: Session, activity_id: int, activity: ActivityUpdate) -> Activity:
        db_activity = db.query(Activity).filter(Activity.id == activity_id)
        if db_activity:
            for key, value in activity.model_dump(exclude_unset=True).items():
                setattr(db_activity, key, value)
            db.commit()
            db.refresh(db_activity)
        return db_activity

    def delete_activity(self, db: Session, activity_id: int) -> Activity:
        db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if db_activity:
            db.delete(db_activity)
            db.commit()
        return db_activity

    def list_activities(self, db: Session, skip: int = 0, limit: int = 10) -> list[Activity]:
        return db.query(Activity).offset(skip).limit(limit).all()
