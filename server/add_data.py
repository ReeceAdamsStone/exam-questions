from app import app, db
from models import PaperType, Component_of_Paper, Topic, Questions
from question_strings import LP1Q5Strings, AFStrings, LP2Q5Strings, ACCQuestions, ShakespeareQuestions, AnthologyPoetryQuestions
from classes import LP1Q5, LitAnimalFarm, LP2Q5, LitACC, LitShakespeare, LitSeenPoetry
from typing import List

def add_data():
    with app.app_context():
        for question_string in LP1Q5Strings:
            lp1q5_instance = LP1Q5(question_string)
            paper_id, component_id, topic_id = get_paper_component_topic_ids(
                db.session,
                lp1q5_instance.paper_name,
                lp1q5_instance.paper_component,
                lp1q5_instance.topic,
                lp1q5_instance.marks
            )
            db.session.add(Questions(
                Question_String=lp1q5_instance.question_string,
                Topic_ID=topic_id,
                Component_ID=component_id,
                Paper_ID=paper_id,
                Supporting_Material=lp1q5_instance.supporting_material
            ))

        for af_string in AFStrings:
            lit_animal_farm_instance = LitAnimalFarm(af_string)
            af_paper_id, af_component_id, af_topic_id = get_paper_component_topic_ids(
                db.session,
                lit_animal_farm_instance.paper_name,
                lit_animal_farm_instance.paper_component,
                lit_animal_farm_instance.topic,
                lit_animal_farm_instance.marks
            )
            db.session.add(Questions(
                Question_String=lit_animal_farm_instance.question_string,
                Topic_ID=af_topic_id,
                Component_ID=af_component_id,
                Paper_ID=af_paper_id,
                Supporting_Material=lit_animal_farm_instance.supporting_material
            ))

        for question2_string in LP2Q5Strings:
            lp2q5_instance = LP2Q5(question2_string)
            lp2q5_paper_id, lp2q5_component_id, lp2q5_topic_id = get_paper_component_topic_ids(
                db.session,
                lp2q5_instance.paper_name,
                lp2q5_instance.paper_component,
                lp2q5_instance.topic,
                lp2q5_instance.marks
            )
            db.session.add(Questions(
                Question_String=lp2q5_instance.question_string,
                Topic_ID=lp2q5_topic_id,
                Component_ID=lp2q5_component_id,
                Paper_ID=lp2q5_paper_id,
                Supporting_Material=lp2q5_instance.supporting_material
            ))

        for acc_string in ACCQuestions:
            lit_acc_instance = LitACC(acc_string)
            acc_paper_id, acc_component_id, acc_topic_id = get_paper_component_topic_ids(
                db.session,
                lit_acc_instance.paper_name,
                lit_acc_instance.paper_component,
                lit_acc_instance.topic,
                lit_acc_instance.marks
            )
            db.session.add(Questions(
                Question_String=lit_acc_instance.question_string,
                Topic_ID=acc_topic_id,
                Component_ID=acc_component_id,
                Paper_ID=acc_paper_id,
                Supporting_Material=lit_acc_instance.supporting_material
            ))

        for shakespeare_string in ShakespeareQuestions:
            shakespeare_instance = LitShakespeare(shakespeare_string)
            shakespeare_paper_id, shakespeare_component_id, shakespeare_topic_id = get_paper_component_topic_ids(
                db.session,
                shakespeare_instance.paper_name,
                shakespeare_instance.paper_component,
                shakespeare_instance.topic,
                shakespeare_instance.marks
            )
            db.session.add(Questions(
                Question_String=shakespeare_instance.question_string,
                Topic_ID=shakespeare_topic_id,
                Component_ID=shakespeare_component_id,
                Paper_ID=shakespeare_paper_id,
                Supporting_Material=shakespeare_instance.supporting_material
            ))

        for anthology_string in AnthologyPoetryQuestions:
            anthology_instance = LitSeenPoetry(anthology_string)
            anthology_paper_id, anthology_component_id, anthology_topic_id = get_paper_component_topic_ids(
                db.session,
                anthology_instance.paper_name,
                anthology_instance.paper_component,
                anthology_instance.topic,
                anthology_instance.marks
            )
            db.session.add(Questions(
                Question_String=anthology_instance.question_string,
                Topic_ID=anthology_topic_id,
                Component_ID=anthology_component_id,
                Paper_ID=anthology_paper_id,
                Supporting_Material=anthology_instance.supporting_material
            ))

        db.session.commit()

def get_paper_component_topic_ids(session, paper_name, component_name, topic_name, marks):
    existing_paper = session.query(PaperType).filter_by(Paper_Name=paper_name).first()

    if not existing_paper:
        new_paper = PaperType(Paper_Name=paper_name)
        session.add(new_paper)
        session.flush()
        paper_id = new_paper.PaperType_ID
    else:
        paper_id = existing_paper.PaperType_ID

    existing_component = session.query(Component_of_Paper).filter_by(
        Component_Name=component_name,
        Marks=marks,
        PaperType_ID=paper_id
    ).first()

    if not existing_component:
        new_component = Component_of_Paper(
            Component_Name=component_name,
            Marks=marks,
            PaperType_ID=paper_id
        )
        session.add(new_component)
        session.flush()
        component_id = new_component.Component_of_Paper_ID
    else:
        component_id = existing_component.Component_of_Paper_ID

    existing_topic = session.query(Topic).filter_by(
        Topic_Name=topic_name,
        Component_ID=component_id,
        Paper_ID=paper_id
    ).first()

    if not existing_topic:
        new_topic = Topic(
            Topic_Name=topic_name,
            Component_ID=component_id,
            Paper_ID=paper_id
        )
        session.add(new_topic)
        session.flush()
        topic_id = new_topic.Topic_ID
    else:
        topic_id = existing_topic.Topic_ID

    return paper_id, component_id, topic_id

# Run the function to add data to the database
add_data()
