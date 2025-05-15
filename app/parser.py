import re


def parse_resume(text: str):
    tech_keywords = ["python", "aws", "docker",
                     "sql", "javascript", "fastapi", "django"]
    found = [kw for kw in tech_keywords if re.search(
        rf"\\b{kw}\\b", text, re.IGNORECASE)]
    return found
