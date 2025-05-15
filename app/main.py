from fastapi import FastAPI, UploadFile, File
from parser import parse_resume
from matcher import match_jobs

app = FastAPI()


@app.post("/match")
async def match_resume(file: UploadFile = File(...)):
    content = await file.read()
    skills = parse_resume(content.decode())
    matched = match_jobs(skills)
    return {"skills": skills, "matched_jobs": matched}
