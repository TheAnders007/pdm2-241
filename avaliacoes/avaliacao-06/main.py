from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import sqlite3
from sqlite3 import Connection

app = FastAPI()

DATABASE_URL = "alunos.db"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()

class AlunoCreate(BaseModel):
    aluno_nome: str
    endereco: str

class AlunoUpdate(BaseModel):
    aluno_nome: str
    endereco: str

class AlunoResponse(BaseModel):
    id: int
    aluno_nome: str
    endereco: str

    class Config:
        orm_mode = True

@app.post("/criar_aluno/", response_model=AlunoResponse)
def criar_aluno(aluno: AlunoCreate, db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO tb_aluno (aluno_nome, endereco) VALUES (?, ?)",
        (aluno.aluno_nome, aluno.endereco)
    )
    db.commit()
    aluno_id = cursor.lastrowid
    return AlunoResponse(id=aluno_id, aluno_nome=aluno.aluno_nome, endereco=aluno.endereco)

@app.get("/listar_alunos/", response_model=List[AlunoResponse])
def listar_alunos(db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_aluno")
    rows = cursor.fetchall()
    return [AlunoResponse(id=row[0], aluno_nome=row[1], endereco=row[2]) for row in rows]

@app.get("/listar_um_aluno/{aluno_id}", response_model=AlunoResponse)
def listar_um_aluno(aluno_id: int, db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_aluno WHERE id = ?", (aluno_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return AlunoResponse(id=row[0], aluno_nome=row[1], endereco=row[2])

@app.put("/atualizar_aluno/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: int, aluno_update: AlunoUpdate, db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE tb_aluno SET aluno_nome = ?, endereco = ? WHERE id = ?",
        (aluno_update.aluno_nome, aluno_update.endereco, aluno_id)
    )
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return AlunoResponse(id=aluno_id, aluno_nome=aluno_update.aluno_nome, endereco=aluno_update.endereco)

@app.delete("/excluir_aluno/{aluno_id}", response_model=AlunoResponse)
def excluir_aluno(aluno_id: int, db: Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_aluno WHERE id = ?", (aluno_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    cursor.execute("DELETE FROM tb_aluno WHERE id = ?", (aluno_id,))
    db.commit()
    return AlunoResponse(id=row[0], aluno_nome=row[1], endereco=row[2])
