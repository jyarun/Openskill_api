from flask import Blueprint
from service import jobs_service
from flask import request, jsonify

jobs_api = Blueprint('jobs_api', __name__)


@jobs_api.route('/api/jobs/all', methods=['GET'])
def get_job_all():
    results = jobs_service.get_all_jobs()
    return jsonify(results)


@jobs_api.route('/api/jobs', methods=['GET'])
def get_job():
    if 'uuid' in request.args:
        uuid = str(request.args['uuid'])
        results = jobs_service.get_job(uuid)
    else:
        results = "Error: No uuid field provided. Please specify a valid id."

    return jsonify(results)
