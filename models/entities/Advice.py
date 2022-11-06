class Advice():

    def __init__(self, topic, description, id_subject, date, start_time, end_time, id_teacher) -> None:
        self.topic = topic
        self.description = description
        self.id_subject = id_subject
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.id_teacher = id_teacher

    def to_JSON(self):
        return {
            'topic': self.topic,
            'description': self.description,
            'id_subject': self.id_subject,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'id_teacher': self.id_teacher
        }


class AdviceJoin():

    def __init__(self, topic, description, id_subject, date, start_time, end_time, id_teacher) -> None:
        self.topic = topic
        self.description = description
        self.id_subject = id_subject
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.id_teacher = id_teacher

    def to_JSON(self):
        return {
            'topic': self.topic,
            'description': self.description,
            'id_subject': self.id_subject,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'id_teacher': self.id_teacher
        }


class AdviceEdit():

    def __init__(self, topic, description, id_subject, date, start_time, end_time) -> None:
        self.topic = topic
        self.description = description
        self.id_subject = id_subject
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        
    def to_JSON(self):
        return {
            'topic': self.topic,
            'description': self.description,
            'id_subject': self.id_subject,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
        }


class AdviceList():

    def __init__(self, id, topic, subjectName, description,  date, start_time, end_time, teacherName) -> None:
        self.id = id
        self.topic = topic
        self.subjectName = subjectName
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.teacherName = teacherName

    def to_JSON(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'subjectName': self.subjectName,
            'description': self.description,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'teacherName': self.teacherName
        }

class AdviceSchedule():

    def __init__(self, id_advice, id_student, time_advice) -> None:
        self.id_advice = id_advice
        self.id_student = id_student
        self.time_advice = time_advice

    def to_JSON(self):
        return {
            'id_advice': self.id_advice,
            'id_student': self.id_student,
            'time_advice': self.time_advice
        }

# class AdviceTimesTaken():

#     def __init__(self) -> None:
#         self.time_advice = []

#     def add_new_arrival(self, time_advice):
#         self.time_advice.append(time_advice)

#     def to_JSON(self):
#         return {
#             'time_advice': self.time_advice
#         }
#     def to_String(self):
#         return self.time_advice