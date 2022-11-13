from flask import Blueprint, jsonify, request

# Entities
from models.entities.User import User
# Models
from models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)


#@main.route('/get-user/<userId>', methods=['GET'])
#def get_user(userId):
#    return jsonify(status=200, message='Get user', data=UserModel.get_user(userId)), 200
#
#
#@main.route('/delete-user', methods=['POST'])
#def delete_user():
#    try:
#        id = request.json['id']
#
#        affected_rows = UserModel.delete_user(id)
#
#        if affected_rows == 1:
#            return jsonify(status=200, data=id), 200
#        else:
#            return jsonify(status=500, message='Failed to delete user', method='delete_user'), 500
#
#    except Exception as ex:
#        return jsonify(status=500, message=str(ex), method='delete-user'), 500


@main.route('/get-all-users', methods=['GET'])
def get_all_users():
    return jsonify(status=200, message='Get users success', data=UserModel.get_all_users()), 200


#@main.route('/get-all-users-from-superadmin', methods=['GET'])
#def get_all_users_from_superadmin():
#    return jsonify(status=200, message='Get users success superadmin', data=UserModel.get_all_users_from_superadmin()), 200
#
#
@main.route('/update-rol', methods=['POST'])
def update_user_rol():
    try:
        id = request.json['id']
        id_rol = request.json['id_rol']

        affected_rows = UserModel.update_user_rol(id,id_rol)

        if affected_rows == 1:
            return jsonify(status=200, data=id, message='Updated rol successfully'), 200
        else:
            return jsonify(status=500, message='Failed to update rol', method='update-rol'), 500

    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='update-rol'), 500
