from fastapi import Depends, HTTPException, status, Response, APIRouter
from .. import schemas, models
from ..database import get_db
from typing import List
from sqlalchemy.orm import Session
from .. import oauth2
from sqlalchemy import func

router = APIRouter(
    prefix="/deposits",
    tags=['deposits']
)

#@router.get("/", response_model=List[schemas.Deposit])
@router.get("/", response_model=List[schemas.DepositWithReports])
def get_deposits(db: Session = Depends(get_db), limit: int=5, offset: int=0, search: str = ""):
   
    deposit = db.query(models.Deposit, func.count(models.Report.deposit_id).label("reports")).join(models.Report, models.Deposit.id == models.Report.deposit_id, isouter=True).group_by(models.Deposit.id).filter(models.Deposit.receiver.contains(search)).limit(limit).all()
   
    return deposit

@router.get("/{id}", response_model = schemas.DepositWithReports)
def get_deposit(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    deposit = db.query(models.Deposit, func.count(models.Report.deposit_id).label("reports")).join(models.Report, models.Deposit.id == models.Report.deposit_id, isouter=True).group_by(models.Deposit.id).filter(models.Deposit.id == id).first()
   
    if not deposit:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, 
                             detail=f"Page with id: {id} was not found.")
    return deposit

@router.post("/", status_code=201, response_model=schemas.Deposit, )
def create_deposit(deposit: schemas.CreateDeposit, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    deposit = models.Deposit(**deposit.dict())
    deposit.owner_id = current_user.id
    db.add(deposit)
    db.commit()
    db.refresh(deposit)
  
    return deposit

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deposit(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    deposit = db.query(models.Deposit).filter(models.Deposit.id == id)

    if not deposit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"deposit with id: {id} doesn't exist")
    if deposit.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")

    deposit.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Deposit)
def update_deposit(id: int, deposit: schemas.CreateDeposit, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   

    deposit_query = db.query(models.Deposit).filter(models.Deposit.id == id)

    if not deposit_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"page with id: {id} doesn't exist.")
    if deposit_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")
    
    deposit_query.update(deposit.dict(), synchronize_session=False)
    db.commit()
    return deposit_query.first()