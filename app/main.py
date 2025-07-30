from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from app import schemas, crud, database, services as background


app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # This will create all tables at startup
    await database.init_db()


@app.post("/documents/", response_model=schemas.DocumentOut)
async def upload_document(doc: schemas.DocumentCreate, db: database.AsyncSession = Depends(database.get_db)):
    return await crud.create_document(db, doc)

@app.get("/documents/{id}", response_model=schemas.DocumentOut)
async def get_document(id: int, db: database.AsyncSession = Depends(database.get_db)):
    doc = await crud.get_document(db, id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@app.post("/documents/{id}/question", response_model=schemas.QuestionOut)
async def submit_question(id: int, q: schemas.QuestionCreate, background_tasks: BackgroundTasks, db: database.AsyncSession = Depends(database.get_db)):
    doc = await crud.get_document(db, id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    question = await crud.create_question(db, id, q.question)
    background_tasks.add_task(background.process_question, db, question.id, q.question)
    return question

@app.get("/questions/{id}", response_model=schemas.QuestionOut)
async def get_question(id: int, db: database.AsyncSession = Depends(database.get_db)):
    q = await crud.get_question(db, id)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q