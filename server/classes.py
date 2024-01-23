from app import db

# from models import dbtables

class QuestionData:
    """
    A class representing the data structure for question data

    Properties:
    - question_string = a string containing question
    - marks = how many marks a question should have 
    - ao_id = the ID for the assessment objective (ranges from 1 to 6)
    - paper_component = the part of the paper (Section A, B, C)
    - paper_name = title of the paper (Lit, Lang etc)
    - topic - focus of that question (Poetry, Creative Writing, Animal farm etc)
    - supporting_material = boolean value to show whether the question should be accompanied by other material

    """
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

    """
    A subclass representing the data structure for a Language Paper 2, Section B, Question 5.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (40 for LP2Q5)
    - ao_id: the ID for the assessment objectives (ranges from 5 to 6)
    - paper_component: the part of the paper (Section B)
    - paper_name: title of the paper (Language Paper 2)
    - topic: focus of that question (Viewpoint Writing)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (False for LP2Q5)
    """
    def __init__(self, question_string):
        super().__init__(question_string, marks=40, ao_id=[5, 6], paper_component="Section B", paper_name="Language Paper 2", topic="Viewpoint Writing", supporting_material=False)


class LP1Q5(QuestionData):
    """
    A subclass representing the data structure for a Language Paper 1, Section B, Question 5.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (40 for LP1Q5)
    - ao_id: the ID for the assessment objectives (ranges from 5 to 6)
    - paper_component: the part of the paper (Section B)
    - paper_name: title of the paper (Language Paper 1)
    - topic: focus of that question (Creative Writing)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (True for LP1Q5)
    """

    def __init__(self, question_string):
        super().__init__(question_string, marks=40, ao_id=[5, 6], paper_component="Section B", paper_name="Language Paper 1", topic="Creative Writing", supporting_material=True)

class LitShakespeare(QuestionData):

    """
    A subclass representing the data structure for a Literature Paper 1, Section A, Shakespeare question.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (30 for LitShakespeare)
    - ao_id: the ID for the assessment objectives (ranges from 1 to 3)
    - paper_component: the part of the paper (Section A)
    - paper_name: title of the paper (Literature Paper 1: Shakespeare and The 19th Century Novel)
    - topic: focus of that question (Macbeth)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (True for LitShakespeare)
    """    
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section A", paper_name="Literature Paper 1: Shakespeare and The 19th Century Novel", topic="Macbeth", supporting_material=True)


class LitACC(QuestionData):
    """
    A subclass representing the data structure for a Literature Paper 1, Section B, A Christmas Carol question.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (30 for LitACC)
    - ao_id: the ID for the assessment objectives (ranges from 1 to 3)
    - paper_component: the part of the paper (Section B)
    - paper_name: title of the paper (Literature Paper 1: Shakespeare and The 19th Century Novel)
    - topic: focus of that question (A Christmas Carol)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (True for LitACC)
    """
    
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section B", paper_name="Literature Paper 1: Shakespeare and The 19th Century Novel", topic="A Christmas Carol", supporting_material=True)


class LitAnimalFarm(QuestionData):

    """
    A subclass representing the data structure for a Literature Paper 2, Section A, Animal Farm question.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (34 for LitAnimalFarm)
    - ao_id: the ID for the assessment objectives (ranges from 1 to 4)
    - paper_component: the part of the paper (Section A)
    - paper_name: title of the paper (Literature Paper 2: Modern Texts and poetry)
    - topic: focus of that question (Animal Farm)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (False for LitAnimalFarm)
    """    
    def __init__(self, question_string):
        super().__init__(question_string, marks=34, ao_id=[1, 2, 3, 4], paper_component="Section A", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Animal Farm", supporting_material=False)


class LitSeenPoetry(QuestionData):

    """
    A subclass representing the data structure for a Literature Paper 2, Section B, Anthology Poetry question.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (30 for LitSeenPoetry)
    - ao_id: the ID for the assessment objectives (ranges from 1 to 3)
    - paper_component: the part of the paper (Section B)
    - paper_name: title of the paper (Literature Paper 2: Modern Texts and poetry)
    - topic: focus of that question (Anthology Poetry)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (True for LitSeenPoetry)
    """    
    def __init__(self, question_string):
        super().__init__(question_string, marks=30, ao_id=[1, 2, 3], paper_component="Section B", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Anthology Poetry", supporting_material=True)
        

class LitUnseenPoetry(QuestionData):

    """
    A subclass representing the data structure for a Literature Paper 2, Section C, Unseen Poetry question.

    Properties:
    - question_string: a string containing the question
    - marks: how many marks the question should have (32 for LitUnseenPoetry)
    - ao_id: the ID for the assessment objectives (ranges from 1 to 2)
    - paper_component: the part of the paper (Section C)
    - paper_name: title of the paper (Literature Paper 2: Modern Texts and poetry)
    - topic: focus of that question (Unseen Poetry)
    - supporting_material: boolean value to show whether the question should be accompanied by other material (True for LitUnseenPoetry)
    """    
    def __init__(self, question_string):
        super().__init__(question_string, marks=32, ao_id=[1, 2], paper_component="Section C", paper_name="Literature Paper 2: Modern Texts and poetry", topic="Unseen Poetry", supporting_material=True)


# lp2q5_instance = LP2Q5(question_string="Your specific question string for LP2Q5")

# print(lp2q5_instance.question_string)        # Output: Your specific question string for LP2Q5
# print(lp2q5_instance.marks, "marks total")   # Output: 40
# print(lp2q5_instance.ao_id)                  # Output: [5, 6]
# print(lp2q5_instance.paper_component)        # Output: Section B
# print(lp2q5_instance.paper_name)             # Output: Language Paper 2
# print(lp2q5_instance.topic)                  # Output: Viewpoint Writing
# print(lp2q5_instance.supporting_material)    # Output: None