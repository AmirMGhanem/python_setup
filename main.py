import hashlib
import os
from fastapi import FastAPI, Depends, Request, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session


from sql_app.database import get_db, User, TODO

app = FastAPI()

class Example(BaseModel):
    id: int
    comment: str


class UserModel(BaseModel):
    id: int
    email: str
    is_active: int

class RegisterModel(BaseModel):
    id: int
    email: str
    password: str



@app.get("/")
async def root(db: Session = Depends(get_db)):
    print ("connecting to mysql")
    user= db.query(User).filter(User.id==1).first()
    return f"user email{user.email} and todos left {len(user.todos)} titles are {[todo.title for todo in user.todos]}"


@app.post("/add_user")
async def root2(user:UserModel,db: Session = Depends(get_db)):
    print ("connecting to mysql")
    user = User(id=user.id, email=user.email, is_active=user.is_active)
    db.add(user)
    db.commit()
    return user.email

@app.post("/add_todo")
async def todoAdd(payload: dict = Body(...),db: Session = Depends(get_db)):
    user_id=payload["user_id"]
    title=payload["title"]
    description=payload["description"]
    user1 = db.query(User).filter(User.id==user_id).first()
    user1.todos.append(TODO(title=title,description=description))
    db.commit()
    return "ok"

@app.post("/register")
async def register(regestier:RegisterModel,db: Session = Depends(get_db)):

    hashed_password= hashlib.md5(regestier.password.encode("utf-8")).hexdigest()
    user = User(id=regestier.id, email=regestier.email,password=hashed_password)
    db.add(user)
    db.commit()
    return "ok"


@app.post("/salloum")
async def root2(boddy:Example):
    # save the example to a file

    with open(os.path.join(os.getcwd(), "example.json"), "w") as f:
        f.write(str(boddy))
    return {"message": "Hello World2"}

@app.post("/mark_done")
def mark_done(payload: dict = Body(...),db: Session = Depends(get_db)):
    todo_id=payload["todo_id"]
    todo = db.query(TODO).filter(TODO.id==todo_id).first()

    todo.done =0 if todo.done == 1 else 1
    # todo.done=not todo.done
    db.commit()
    return "ok"




@app.get("/salloum")
async def root3():
    with open(os.path.join(os.getcwd(), "example.json"), "r") as f:
        data = f.read()

    return {"message": data}





