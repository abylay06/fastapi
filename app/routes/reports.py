from fastapi import Depends, HTTPException, status, Response, APIRouter
from .. import database, models, oauth2, schemas
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['REPORTS'],
    prefix="/report"
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def report(report: schemas.Report, db: Session = Depends(database.get_db), current_user: id = 
Depends(oauth2.get_current_user)):
    
    if not db.query(models.Deposit).filter(models.Deposit.id == report.deposit_id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deposit not found")

    query = db.query(models.Report).filter(models.Report.user_id == current_user.id,
                                          models.Report.deposit_id == report.deposit_id)
    if report.dir == 1:
        if query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Cannot make the same report")
        db.add(models.Report(deposit_id=report.deposit_id, user_id = current_user.id))
        db.commit()
        return {"message": "successfully reported"}
    
    else:
        if not query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report does not exist")
        query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deletesd report"}
        
        
    



