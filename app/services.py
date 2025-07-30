import asyncio
from .crud import update_answer
from sqlalchemy.ext.asyncio import AsyncSession

async def process_question(db: AsyncSession, question_id: int, question_text: str) -> None:
    await asyncio.sleep(5)
    dummy_answer = f"This is a generated answer to your question: {question_text}"
    await update_answer(db, question_id, dummy_answer)