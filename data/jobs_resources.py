from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.jobs import Jobs

parser_job = reqparse.RequestParser()
parser_job.add_argument('job', required=True)
parser_job.add_argument('work_size', required=True)
parser_job.add_argument('collaborators', required=True)
parser_job.add_argument('team_leader', required=True, type=int)


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Jobs {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('job', 'work_size', "collaborators", 'team_leader'))})

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'work_size', 'user.name')) for item in jobs]})

    def post(self):
        args = parser_job.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            team_leader=args['team_leader']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})
