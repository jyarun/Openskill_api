from flask import request, jsonify

from dal.jobs_dal import JobsDAL


def get_all_jobs():
    jobs_dal = JobsDAL()
    jobs = jobs_dal.get_all_jobs()
    return jobs


def get_job(uuid):
    jobs_dal = JobsDAL()
    job = jobs_dal.get_job(uuid)
    if not job:
        return "Error: No job with given uuid found. Please specify a valid id."
    else:
        return job
