from flask import request

from ..app import app
from .controllers import *

@app.route("/projects", methods=['GET', 'POST'])
def get_create_projects():
    if request.method == 'GET': return get_all_projects()
    if request.method == 'POST': return create_project()
    else: return 'Method is Not Allowed'

@app.route("/projects/<project_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_projects(project_id):
    if request.method == 'GET': return find_project_by_id(project_id)
    if request.method == 'PUT': return update_project_by_id(project_id)
    if request.method == 'DELETE': return delete_project(project_id)
    else: return 'Method is Not Allowed'
