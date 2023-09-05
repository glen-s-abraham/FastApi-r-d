from fastapi import FastAPI,HTTPException,status,Depends

dev_db = ["DB for development"]

def get_db_session():
    return dev_db


app = FastAPI()


@app.post("/items")
def add_item(item:str,db=Depends(get_db_session)):
    db.append(item)
    print(db)
    return {'message':f'added item {item}'}

#app.dependancy_overriders[get_db_session]=get_testung_db