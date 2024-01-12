from classes import *
from flask_sqlalchemy import SQLAlchemy
from models import *


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

    "Either: Write a story in which a photograph plays a significant part. Or: Write a description suggested by this photograph:"
]

for question_string in LP1Q5Strings:
    lp1q5_instance = LP1Q5(question_string)

    # Note: Adjust the models and relationships based on your actual setup
    db.session.add(Assessment_Objectives(AO_Int_Name=f'Assessment Objective {lp1q5_instance.ao_id[0]}'))
    
    db.session.add(Assessment_Objectives(AO_Int_Name=f'Assessment Objective {lp1q5_instance.ao_id[1]}'))
    
    db.session.add(Paper_Name(Paper_Name=lp1q5_instance.paper_name))
    
    db.session.add(Component_of_Paper(Component_Name=lp1q5_instance.paper_component, Marks=lp1q5_instance.marks, Paper_ID=1))
    
    db.session.add(Topics(Topic_Name=lp1q5_instance.topic, Component_of_Paper_ID=1))
    
    db.session.add(Questions(Question_String=lp1q5_instance.question_string, Topic_ID=1, Supporting_Material=lp1q5_instance.supporting_material))
    
    db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[0]}').first().AO_ID))
    
    db.session.add(AOs_By_Paper(QID=db.session.query(Questions).filter_by(Question_String=lp1q5_instance.question_string).first().QiD, AO_ID=db.session.query(Assessment_Objectives).filter_by(AO_Int_Name=f'Objective {lp1q5_instance.ao_id[1]}').first().AO_ID))
    db.session.commit()

# Close the session
db.session.close()

# auto incremention of ids? db enginge? ao mapping to questions?