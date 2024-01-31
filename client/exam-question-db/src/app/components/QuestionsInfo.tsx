// QuestionsCard.jsx
import React from "react";
import QuestionContainer from "./QuestionContainer";

interface Question {
  id: number;
  question_string: string;
  topic: {
    id: number;
    name: string;
  };
}

interface QuestionsCardProps {
  questions: Question[];
}

const QuestionsInfo: React.FC<QuestionsCardProps> = ({ questions }) => {
  return (
    <div>
      <h2>Your Questions</h2>
      {questions.map((question: Question) => (
        <QuestionContainer key={question.id} question={question} />
      ))}
    </div>
  );
};

export default QuestionsInfo;
