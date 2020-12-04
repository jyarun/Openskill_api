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
    # It is a better idea to get the uuid from the request here
    # and pass it to the service, the service should not care about the
    # the request that much but should get only its uuid and the error handling should
    # be done here then
    if 'uuid' in request.args:
        uuid = str(request.args['uuid'])
        results = jobs_service.get_job(uuid)
    else:
        results = "Error: No uuid field provided. Please specify a valid id."

    return jsonify(results)
