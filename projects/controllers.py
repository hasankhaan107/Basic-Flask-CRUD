from flask import request, jsonify
import uuid

from .. import db
from .model import Project

def get_all_projects():
    projects = Project.query.all()
    # covert all the projects to dictionary
    all_projects = [project.toDict() for project in projects]
    # return the json response and status code
    return jsonify({'message': 'Projects retrieved successfully', 'projects': all_projects}), 200

def create_project():
    # Get the form input data from the request.
    request_data = request.form.to_dict()
    if request_data and request_data['title'] != None:
        try:
             # generate the random string id
            id = str(uuid.uuid4())
            # Instantiatethe project record.
            new_project = Project(id= id, title = request_data.get('title', ''), description = request_data.get('description', ''), completed = request_data.get('completed', False))
            db.session.add(new_project)
            # store the project details to database
            db.session.commit()
            # Retrieve the newly created project and return as JSON
            project = Project.query.get(id).toDict()
            return jsonify({'message': 'Project created successfully', 'project': project}), 200
        except Exception as e:
            return jsonify({'Error': str(e)}), 500

    else:
        return jsonify({'message': 'Project title cannot be empty'}), 400

def find_project_by_id(project_id):
    project = Project.query.get(project_id)
    if project:
        return jsonify(project.toDict())

    return jsonify({'message': 'Project not found. Invalid project id.'}), 404

def update_project_by_id(project_id):
    project = Project.query.get(project_id)
    if project:
        try:
            request_data = request.form.to_dict()
            if request_data.get('title') == None and request_data.get('description') == None and request_data.get('completed') == None:
                return jsonify({'message': 'Did not find anything to update the project.'}), 400

            if request_data.get('title'):
                project.title = request_data['title']
            
            if request_data.get('description'):
                project.description = request_data['description']
            
            if request_data.get('completed'):
                project.completed = bool(request_data['completed'])

            db.session.commit()
        except Exception as e:
            return jsonify({'message': 'Something went wrong, could not update the project. Error: {str(e)}'}), 500
        updated_project = Project.query.get(project_id).toDict()
        return jsonify({'message': 'Project updated successfully', 'project': updated_project}), 200
    else:
        return jsonify({'message': 'Project not found. Invalid project id.'}), 404

def delete_project(project_id):
    project = Project.query.get(project_id)
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': ('Project with Id "{}" deleted successfully!').format(project_id)}), 200
    else:
        return jsonify({'message': 'Project not found. Invalid project id.'}), 404