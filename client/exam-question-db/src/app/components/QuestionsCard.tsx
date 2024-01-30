// QuestionsCard.jsx
import React from "react";

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

const QuestionsCard: React.FC<QuestionsCardProps> = ({ questions }) => {
  return (
    <div>
      <h2>Filtered Questions</h2>
      <ul>
        {questions.map((question: Question) => (
          <li key={question.id}>{question.question_string}</li>
        ))}
      </ul>
    </div>
  );
};

export default QuestionsCard;
