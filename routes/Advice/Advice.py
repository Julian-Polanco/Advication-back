from flask import Blueprint, jsonify, request

# Entities
from models.entities.Advice import Advice, AdviceSchedule
# Models
from models.AdviceModel import AdviceModel

main = Blueprint('advice_blueprint', __name__)


@main.route('/add-advice', methods=['POST'])
def add_advice():
    try:

        topic = request.json['topic'] 
        description = request.json['description'] 
        id_subject = request.json['id_subject'] 
        date = request.json['date'] 
        start_time = request.json['start_time'] 
        end_time = request.json['end_time'] 
        id_teacher = request.json['id_teacher'] 
        advice = Advice(topic, description, id_subject, date, start_time, end_time, id_teacher)

        response = AdviceModel.create_advice(advice)
        
        return response

    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='add-advice'), 500

@main.route('/get-all-advices', methods=['GET'])
def get_all_advices():
    try:
        response = AdviceModel.get_all_advices()
        
        return response

    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='get-all-advices'), 500

@main.route('/set-advice', methods=['POST'])
def set_advice():
    try:

        id_advice = request.json['id_advice'] 
        id_student = request.json['id_student'] 
        time_advice = request.json['time_advice'] 
        advice = AdviceSchedule(id_advice, id_student, time_advice)

        response = AdviceModel.set_advice(advice)
        
        return response

    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='set-advice'), 500

@main.route('/get-advice-schedule', methods=['POST'])
def get_advice_schedule():
    try:

        id_advice = request.json['id_advice']

        response = AdviceModel.get_advice_schedule(id_advice)
        
        return response

    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='get-advice-schedule'), 500




@main.route('/get-all-advices-teacher/<id>', methods=['GET'])
def get_all_advices_teacher(id):
    try:
        response = AdviceModel.get_all_advices_teacher(id)
        return response
    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='get-all-advices-teacher'), 500


@main.route('/delete-advice', methods=['POST'])
def delete_advice():
    try:
        id_advice = request.json['id_advice']
        response = AdviceModel.delete_advice(id_advice)
        return response
    except Exception as ex:
        return jsonify(status=500, message=str(ex), method='delete-advice'), 500
