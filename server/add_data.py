from classes import *
from flask_sqlalchemy import SQLAlchemy
from models import *
from app import app
from typing import List
from question_strings import *


def get_paper_component_topic_ids(session, paper_name, component_name, topic_name, marks):
    # Check if the Paper_Name already exists
    existing_paper = session.query(Paper_Name).filter_by(Paper_Name=paper_name).first()

    if not existing_paper:
        # If it doesn't exist, add it to the database
        new_paper = Paper_Name(Paper_Name=paper_name)
        session.add(new_paper)
        session.flush()  # Ensure the new paper gets an ID
        paper_id = new_paper.Paper_ID
    else:
        # If it exists, use its ID
        paper_id = existing_paper.Paper_ID

    # Check if the Component_of_Paper already exists for this paper
    existing_component = session.query(Component_of_Paper).filter_by(
        Component_Name=component_name,
        Marks=marks,
        Paper_ID=paper_id
    ).first()

    if not existing_component:
        # If it doesn't exist, add it to the database
        new_component = Component_of_Paper(
            Component_Name=component_name,
            Marks=marks,
            Paper_ID=paper_id
        )
        session.add(new_component)
        session.flush()  # Ensure the new component gets an ID
        component_id = new_component.Component_of_Paper_ID
    else:
        # If it exists, use its ID
        component_id = existing_component.Component_of_Paper_ID

    # Check if the Topic already exists for this component
    existing_topic = session.query(Topics).filter_by(
        Topic_Name=topic_name,
        Component_of_Paper_ID=component_id
    ).first()

    if not existing_topic:
        # If it doesn't exist, add it to the database
        new_topic = Topics(
            Topic_Name=topic_name,
            Component_of_Paper_ID=component_id
        )
        session.add(new_topic)
        session.flush()  # Ensure the new topic gets an ID
        topic_id = new_topic.Topic_ID
    else:
        # If it exists, use its ID
        topic_id = existing_topic.Topic_ID

    return paper_id, component_id, topic_id


with app.app_context():
    for question_string in LP1Q5Strings:
        lp1q5_instance = LP1Q5(question_string)

        # Use the function to get paper_id, component_id, and topic_id
        paper_id, component_id, topic_id = get_paper_component_topic_ids(
            db.session,
            lp1q5_instance.paper_name,
            lp1q5_instance.paper_component,
            lp1q5_instance.topic,
            lp1q5_instance.marks
        )

        db.session.add(Questions(Question_String=lp1q5_instance.question_string, Topic_ID=1, Supporting_Material=lp1q5_instance.supporting_material))


    for af_string in AFStrings:
        lit_animal_farm_instance = LitAnimalFarm(af_string)

        # Use the function to get paper_id, component_id, and topic_id for LitAnimalFarm
        af_paper_id, af_component_id, af_topic_id = get_paper_component_topic_ids(
            db.session,
            lit_animal_farm_instance.paper_name,
            lit_animal_farm_instance.paper_component,
            lit_animal_farm_instance.topic,
            lit_animal_farm_instance.marks
        )

        db.session.add(Questions(Question_String=lit_animal_farm_instance.question_string, Topic_ID=2, Supporting_Material=lit_animal_farm_instance.supporting_material))



    for question2_string in LP2Q5Strings:
        lp2q5_instance = LP2Q5(question2_string)
        paper_id, component_id, topic_id = get_paper_component_topic_ids(
            db.session,
            lp2q5_instance.paper_name,
            lp2q5_instance.paper_component,
            lp2q5_instance.topic,
            lp2q5_instance.marks
        )

        db.session.add(Questions(Question_String=lp2q5_instance.question_string, Topic_ID=3, Supporting_Material=lp2q5_instance.supporting_material))


    for acc_string in ACCQuestions:
        lit_acc_instance = LitACC(acc_string)
        paper_id, component_id, topic_id = get_paper_component_topic_ids(
            db.session,
            lit_acc_instance.paper_name,
            lit_acc_instance.paper_component,
            lit_acc_instance.topic,
            lit_acc_instance.marks
        )

        db.session.add(Questions(Question_String=lit_acc_instance.question_string, Topic_ID=4, Supporting_Material=lit_acc_instance.supporting_material))

    for shakespeare_string in ShakespeareQuestions:
        shakespeare_instance = LitShakespeare(shakespeare_string)
        paper_id, component_id, topic_id = get_paper_component_topic_ids(
            db.session,
            shakespeare_instance.paper_name,
            shakespeare_instance.paper_component,
            shakespeare_instance.topic,
            shakespeare_instance.marks
        )

        db.session.add(Questions(Question_String=shakespeare_instance.question_string, Topic_ID=5, Supporting_Material=shakespeare_instance.supporting_material))


    for anthology_string in AnthologyPoetryQuestions:
        anthology_instance = LitSeenPoetry(anthology_string)
        paper_id, component_id, topic_id = get_paper_component_topic_ids(
            db.session,
            anthology_instance.paper_name,
            anthology_instance.paper_component,
            anthology_instance.topic,
            anthology_instance.marks
        )

        db.session.add(Questions(Question_String=anthology_instance.question_string, Topic_ID=6, Supporting_Material=anthology_instance.supporting_material))


    db.session.commit()


    
	
# Assessment Objectives Table - 

# Currently;
# 	14 instances of each assessment objective [5, 6]
# 	28 individual IDs (1-28)

# Should be; 
# 	One instance of AO5
# 	One instance of AO6
# 	AO5 ID
# 	AO6 ID

# Task --> Prepopulate the AO ID column with the 1-6 numbers (however many there are)


# Component of Papter Table - 

# Currently;
# 	Component ID - 14 instances incrementing
# 	Component Name - Repeated for every instance of the ID

# Should be; 
# 	One instance of ID and Name for each component

	

# Topics Talble -

# Also auto incrementing when there should be unique IDs

# Questions Table - 

# Supporting Material is value 1 (for true?); need to be able to source the supporting material somehow 


# AOs By Paper is empty
    


        # # Add Assessment Objectives
        # ao_id_1 = add_assessment_objective(lp1q5_instance.ao_id[0])
        # db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=ao_id_1))

        # ao_id_2 = add_assessment_objective(lp1q5_instance.ao_id[1])
        # db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=ao_id_2))

        # db.session.add(Questions(Question_String=lp1q5_instance.question_string, Topic_ID=1, Supporting_Material=lp1q5_instance.supporting_material))

        # Only add AO relationships if the AO_ID exists

        # result_ao_1 = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[0]}').first()
        # if result_ao_1:
        #     db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=result_ao_1.AO_ID))

        # result_ao_2 = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[1]}').first()
        # if result_ao_2:
        #     db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=result_ao_2.AO_ID))
    



    
# def add_assessment_objective(ao_name: str) -> int:
#     # Check if the Assessment Objective already exists
#     existing_ao = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Assessment Objective {ao_name}').first()

#     if not existing_ao:
#         # If it doesn't exist, add it to the database
#         new_ao = Assessment_Objectives(AO_Int_Name=f'Assessment Objective {ao_name}')
#         db.session.add(new_ao)
#         db.session.flush()
#         return new_ao.AO_ID

#     return existing_ao.AO_ID