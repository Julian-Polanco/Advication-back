from flask import jsonify
from database.db import get_connection
from .entities.Advice import AdviceJoin, AdviceEdit, AdviceList
from werkzeug.security import check_password_hash
import numpy as np
import json

class AdviceModel():

    @classmethod
    def create_advice(self, advice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO public.advices(
	                    topic, description, id_subject, date, start_time, end_time, id_teacher)
	                    VALUES (%s, %s, %s, %s, %s, %s, %s); """, (advice.topic, advice.description, advice.id_subject, advice.date, advice.start_time, advice.end_time, advice.id_teacher))
                affected_rows = cursor.rowcount
                connection.commit()
                connection.close()
                response = jsonify(
                    status = 409, message='Advice not created'), 409
                if affected_rows != None:
                    response = jsonify(
                    status = 200, message='Advice created successfully'), 200
                return response
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_all_advices(self):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ SELECT a.id, a.topic, s.name, a.description, CAST(a.date AS TEXT), CAST(a.start_time AS TEXT), CAST(a.end_time AS TEXT), (u.first_name ||' '||u.last_name)as teacher
	                    FROM public.advices a
	                    inner join users u on a.id_teacher = u.id 
	                    inner join subjects s on a.id_subject = s.id
                        WHERE CAST((date || ' ' || start_time) AS TIMESTAMP)  >= current_timestamp;
	                    """)
                result = cursor.fetchall()
            advices = []
            for advice in result:
                advices.append(
                    AdviceList(advice[0], advice[1], advice[2], advice[3], advice[4], advice[5], advice[6], advice[7]).to_JSON()
                )
            response = jsonify(
                    status = 409, message='There are not advices availables'), 409
            if advices != []:
                response = jsonify(
                status = 200, message='list of advices',data=advices), 200
            connection.close()
            return response
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def set_advice(self, advice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO public."AdviceSchedule"(
	                    id_advice, id_student, time_advice)
	                    VALUES (%s, %s, %s); """, (advice.id_advice, advice.id_student, advice.time_advice))
                affected_rows = cursor.rowcount
                connection.commit()
                connection.close()
                response = jsonify(
                    status = 409, message='Advice not set'), 409
                if affected_rows != None:
                    response = jsonify(
                    status = 200, message='Advice setted successfully'), 200
                return response
        except Exception as ex:
            raise Exception(ex)
   
    @classmethod
    def get_advice_schedule(self, id_advice):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """	SELECT CAST(time_advice AS TEXT) FROM public."AdviceSchedule"
	                    WHERE id_advice = %s;""", (id_advice,))
                resultSchedule = cursor.fetchall()
            timeTaken = []
            for time1 in resultSchedule:
                x = str(time1)
                x = x.replace("(", "")
                x = x.replace(")", "")
                x = x.replace(",", "")
                x = x.replace("'", "")
                timeTaken.append(x)
            with connection.cursor() as cursor2:
                cursor2.execute(
                    """	SELECT CAST(start_time AS TEXT), CAST(end_time AS TEXT) from advices
	                    WHERE id = %s;""", (id_advice,))
                resultAdvice = cursor2.fetchall()
            timeAdvice = []
            for time2 in resultAdvice:
                timeAdvice.append(
                    time2
                )
            hours = AdviceModel.hourInterval(timeAdvice[0][0], timeAdvice[0][1], timeTaken)
            if hours == []:
                hours.append("No hay horarios disponibles")
            response = jsonify(
                    status = 200, message='list of hours',data=hours), 200
            connection.close()
            return response
        except Exception as ex:
            raise Exception(ex)
        
    def hourInterval(start_time, end_time, timeTaken):
        start_time = start_time.split(":")
        end_time = end_time.split(":")
        start_time = int(start_time[0]) * 60 + int(start_time[1])
        end_time = int(end_time[0]) * 60 + int(end_time[1])
        hours = []
        for i in range(start_time, end_time, 15):
            hour = i // 60
            minutes = i % 60
            if minutes == 0:
                minutes = "00"
            if hour < 10:
                hour = "0" + str(hour)
            completeHour = str(hour) + ":" + str(minutes) + ":00"
            if completeHour not in timeTaken:
                hours.append(completeHour)
        return hours
   
    @classmethod
    def get_all_advices_teacher(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ SELECT a.id, a.topic, s.name, a.description, CAST(a.date AS TEXT), CAST(a.start_time AS TEXT), CAST(a.end_time AS TEXT), (u.first_name ||' '||u.last_name)as teacher
	                    FROM public.advices a
	                    inner join users u on a.id_teacher = u.id 
	                    inner join subjects s on a.id_subject = s.id
                        WHERE u.id=%s;
	                    """, (id,))
                result = cursor.fetchall()
            advices = []
            for advice in result:
                advices.append(
                    AdviceList(advice[0], advice[1], advice[2], advice[3], advice[4], advice[5], advice[6], advice[7]).to_JSON()
                )
            response = jsonify(
                    status = 409, message='There are not advices availables'), 409
            if advices != []:
                response = jsonify(
                status = 200, message='list of advices',data=advices), 200
            connection.close()
            return response
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_advice(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ DELETE FROM public.advices
                        WHERE id=%s;""", (id,))
                affected_rows = cursor.rowcount
            connection.commit()
            connection.close()
            response = jsonify(
                status = 409, message='Advice not deleted'), 409
            if affected_rows != None:
                response = jsonify(
                status = 200, message='Advice deleted successfully'), 200
            return response
        except Exception as ex:
            raise Exception(ex)