# Openskill_api


openskill is a full REST API built with flask to manage an application to complete and standard data store for canonical and emerging skills, knowledge, abilities, tools, technolgies, and how they relate to jobs..
It is the first test version developed for the BACKEND-DEVELOPMENT course taught by [REDI](https://www.redi-school.org/career-program-munich).







### Endpoints

|HTTP Verb|  Url Path                                 | Description                     |
|:------- |:------------------------------------------|:-------------------------------
|  GET    | /api/jobs/all | URL to fetch all jobs|
|  GET    | /api/jobs?uuid={job_uuid} | URL to fetch job information given uuid|
|  GET    | /api/skills/all | URL to fetch all skills from database|
|  GET    | /api/skills?uuid={skill_uuid} | URL to fetch skill information given uuid|




