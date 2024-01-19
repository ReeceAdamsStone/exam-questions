from classes import *
from flask_sqlalchemy import SQLAlchemy
from models import *
from app import app
from typing import List


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

    "Either: Write a story in which a photograph plays a significant part. Or: Write a description suggested by this photograph:",
]

def add_assessment_objective(ao_name: str) -> int:
    # Check if the Assessment Objective already exists
    existing_ao = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Assessment Objective {ao_name}').first()

    if not existing_ao:
        # If it doesn't exist, add it to the database
        new_ao = Assessment_Objectives(AO_Int_Name=f'Assessment Objective {ao_name}')
        db.session.add(new_ao)
        db.session.flush()
        return new_ao.AO_ID

    return existing_ao.AO_ID


with app.app_context():
    for question_string in LP1Q5Strings:
        lp1q5_instance = LP1Q5(question_string)

        # # Add Assessment Objectives
        # ao_id_1 = add_assessment_objective(lp1q5_instance.ao_id[0])
        # db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=ao_id_1))

        # ao_id_2 = add_assessment_objective(lp1q5_instance.ao_id[1])
        # db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=ao_id_2))

    # Create a variable of the paper name by queryingthe db in the Paper Name table, filtering by the first paper name property of the lp1q5 class 
        paper_name_instance = db.session.query(Paper_Name).filter_by(Paper_Name=lp1q5_instance.paper_name).first()
    # If the paper name doesn't exist, add a new record
        if not paper_name_instance:
            paper_name_instance = Paper_Name(Paper_Name=lp1q5_instance.paper_name)
        db.session.add(paper_name_instance)
        
        # Check if the Paper_Name already exists
        existing_paper = db.session.query(Paper_Name).filter_by(Paper_Name=lp1q5_instance.paper_name).first()

        if not existing_paper:
            # If it doesn't exist, add it to the database
            new_paper = Paper_Name(Paper_Name=lp1q5_instance.paper_name)
            db.session.add(new_paper)
            db.session.flush()  # Ensure the new paper gets an ID

            paper_id = new_paper.Paper_ID
        else:
            # If it exists, use its ID
            paper_id = existing_paper.Paper_ID

        # Check if the Component_of_Paper already exists for this paper
        existing_component = db.session.query(Component_of_Paper).filter_by(
            Component_Name=lp1q5_instance.paper_component,
            Marks=lp1q5_instance.marks,
            Paper_ID=paper_id
        ).first()

        if not existing_component:
            # If it doesn't exist, add it to the database
            new_component = Component_of_Paper(
                Component_Name=lp1q5_instance.paper_component,
                Marks=lp1q5_instance.marks,
                Paper_ID=paper_id
            )
            db.session.add(new_component)
            db.session.flush()  # Ensure the new component gets an ID

            component_id = new_component.Component_of_Paper_ID
        else:
            # If it exists, use its ID
            component_id = existing_component.Component_of_Paper_ID

        # Now you can use paper_id and component_id in your subsequent code for this question




        db.session.add(Topics(Topic_Name=lp1q5_instance.topic, Component_of_Paper_ID=1))
        db.session.add(Questions(Question_String=lp1q5_instance.question_string, Topic_ID=1, Supporting_Material=lp1q5_instance.supporting_material))

        # Only add AO relationships if the AO_ID exists
        result_ao_1 = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[0]}').first()
        if result_ao_1:
            db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=result_ao_1.AO_ID))

        result_ao_2 = db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[1]}').first()
        if result_ao_2:
            db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=result_ao_2.AO_ID))

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
    



