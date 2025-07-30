from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas

# Create a new document
async def create_document(db: AsyncSession, doc: schemas.DocumentCreate) -> models.Document:
    new_doc = models.Document(**doc.dict())
    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)
    return new_doc

# Retrieve a document by ID
async def get_document(db: AsyncSession, doc_id: int) -> models.Document | None:
    result = await db.execute(select(models.Document).where(models.Document.id == doc_id))
    return result.scalar_one_or_none()

# Create a new question linked to a document
async def create_question(db: AsyncSession, doc_id: int, question_text: str) -> models.Question:
    new_q = models.Question(document_id=doc_id, question=question_text)
    db.add(new_q)
    await db.commit()
    await db.refresh(new_q)
    return new_q

# Retrieve a question by ID
async def get_question(db: AsyncSession, q_id: int) -> models.Question | None:
    result = await db.execute(select(models.Question).where(models.Question.id == q_id))
    return result.scalar_one_or_none()

# Update the answer and status of a question
async def update_answer(db: AsyncSession, q_id: int, answer: str) -> None:
    result = await db.execute(select(models.Question).where(models.Question.id == q_id))
    question = result.scalar_one_or_none()
    if question is None:
        raise ValueError(f"Question with id {q_id} not found")  # or return a 404 response
    question.answer = answer
    question.status = "answered"
    await db.commit()