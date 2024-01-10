from app import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from models import dbtables

class QuestionData:
    def __init__(self, question_string, marks, ao_id, paper_component, paper_name, topic, supporting_material):
        self.question_string = question_string
        self.marks = marks
        self.ao_id = ao_id
        self.paper_component = paper_component
        self.paper_name = paper_name
        self.topic = topic
        self.supporting_material = supporting_material

        def __repr__(self):
            return f"QuestionData(question_string={self.question_string}, marks={self.marks}, ao_id={self.ao_id}, " \
               f"paper_component={self.paper_component}, paper_name={self.paper_name}, topic={self.topic}, " \
               f"supporting_material={self.supporting_material})"


class LP2Q5(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=40, ao_id=[5, 6], paper_component="Section B", paper_name="Language Paper 2", topic="Viewpoint Writing", supporting_material=None)


class LP1Q5(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=40, ao_id=[5, 6], paper_component="Section B", paper_name="Language Paper 1", topic="Creative Writing", supporting_material=True)

class LitShakespeare(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section A", paper_name="Literature Paper 1: Shakespeare and The 19th Century Novel", topic="Macbeth", supporting_material=True)


class LitACC(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section B", paper_name="Literature Paper 1: Shakespeare and The 19th Century Novel", topic="A Christmas Carol", supporting_material=True)


class LitAnimalFarm(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=34, ao_id=[1, 2, 3, 4], paper_component="Section A", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Animal Farm", supporting_material=False)


class LitSeenPoetry(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section B", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Anthology Poetry", supporting_material=True)
        

class LitUnseenPoetry(QuestionData):
    def __init__(self, question_string):
        super().__init__(question_string, marks=32, ao_id=[1, 2], paper_component="Section C", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Unseen Poetry", supporting_material=True)


LP1Q5Strings = [
    "Either: Write a description of a train station as suggested by this picture Or: Write the opening of a story that begins ‘When he left that day, I did not know I would not see him again for five years… '",

    "Either: Write a description of a harbour as suggested by this scene Or: Write the opening of a story that begins ‘I decided it was time to go out on my boat for the first time since the accident…'",

    "Either: Write a description of a street fruit-seller as suggested by this scene Or: Write the opening of a story that begins ‘Despite the woman’s poverty, she taught me so much that morning about life…'",

    "Either: Write a description of a countryside setting as suggested by this picture Or: Write the opening of a story that begins ‘After living here for three months, I realised I was not cut out for life in the country after all…'",

    "Either: Write a description of a hospital setting as suggested by this picture Or: Write the opening of a story that begins ‘The doctor’s first day on the job at the new hospital was certainly going to be challenging…'",

    "Either: Write a description of a fairground as suggested by this picture Or: Write the opening of a story that begins ‘The noise and bustle of the crowd did not distract the detective from the task to find the fairground killer…'",

    "Either: Write a description of a trek through the snow as suggested by this picture Or: Write the opening of a story that begins ‘As dawn broke across the snow-filled landscape, we faced the most gruelling trek of our lives…’",

    "Either: Write a description of a hot air balloon flight as suggested by this picture Or: Write the opening of a story that begins ‘As we ascended into the sky that warm, summer evening, I did not consider the danger…'",

    "Either: Write a description of a dark street as suggested by this picture OR Write a story about someone feeling unsure or challenged.",

    "Either: Write a description of a sunny day, based on this picture Or: Write the opening of a story about an adventure that starts in this place.",
      
    "Either: Write a story set during a festival as suggested by this picture. OR: Write a story about a celebration going wrong",

    "Either: Write the opening of a story based on this picture. OR: Write the opening part of a story when a character has just suffered defeat or loss",

    "Either: Write the opening of a story suggested by this picture. OR: Write the opening part of a story when a character is put in an unexpected situation.",
]


# lp2q5_instance = LP2Q5(question_string="Your specific question string for LP2Q5")

# print(lp2q5_instance.question_string)        # Output: Your specific question string for LP2Q5
# print(lp2q5_instance.marks, "marks total")   # Output: 40
# print(lp2q5_instance.ao_id)                  # Output: [5, 6]
# print(lp2q5_instance.paper_component)        # Output: Section B
# print(lp2q5_instance.paper_name)             # Output: Language Paper 2
# print(lp2q5_instance.topic)                  # Output: Viewpoint Writing
# print(lp2q5_instance.supporting_material)    # Output: None