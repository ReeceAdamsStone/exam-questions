// QuestionCard.jsx
import React from "react";
import { Card, CardBody } from "@nextui-org/react";

const QuestionCard = ({ question }) => {
  // Split the question string into an array of lines based on bullet points
  const questionLines = question.question_string.split("\n");

  return (
    <Card
      isBlurred
      className="border-none bg-background/60 dark:bg-default-100/50 max-w-[610px]"
      shadow="sm"
    >
      <CardBody>
        <div className="flex flex-col items-start gap-1">
          <h3 className="font-semibold text-foreground/90">Topic: {question.topic.name}</h3>
          <p className="text-small text-foreground/80">{question.id}</p>
          {questionLines.map((line, index) => (
            <p key={index} className={`text-large font-medium${index === 0 ? "" : " ml-2"}`}>
              {index === 0 ? line : ` ${line}`}
            </p>
          ))}
        </div>

        <div className="flex flex-col mt-3 gap-1">
          {/* Add your custom content here */}
        </div>

        <div className="flex w-full items-center justify-center">
          {/* Add your buttons/icons here */}
        </div>
      </CardBody>
    </Card>
  );
};

export default QuestionCard;