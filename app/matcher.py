import json

with open("jobs/jobs.json") as f:
    JOB_DB = json.load(f)


def match_jobs(skills):
    matches = []
    for job in JOB_DB:
        match_score = len(set(job["skills"]) & set(skills))
        if match_score > 0:
            matches.append({"title": job["title"], "score": match_score})
    return sorted(matches, key=lambda x: x["score"], reverse=True)
