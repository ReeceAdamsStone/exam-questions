import React, { useState } from "react";
import { motion } from "framer-motion";
import { Card, CardBody } from "@nextui-org/react";
import { HeartIcon } from "@heroicons/react/20/solid";
import { HeartIcon as OutlineHeart } from "@heroicons/react/24/outline";
import { StarIcon } from "@heroicons/react/20/solid";
import { StarIcon as OutlineStar } from "@heroicons/react/24/outline";
import { MagnifyingGlassCircleIcon } from "@heroicons/react/24/solid";
import { MagnifyingGlassCircleIcon as OutlineGlassCircle } from "@heroicons/react/24/outline";

interface Question {
  id: number;
  question_string: string;
  topic: {
    id: number;
    name: string;
  };
}

interface QuestionCardProps {
  question: Question;
}

const QuestionCard: React.FC<QuestionCardProps> = ({ question }) => {
  // Split the question string into an array of lines based on bullet points
  const questionLines = question.question_string.split("\n");

  interface IconState {
    isLiked: boolean;
    isStarred: boolean;
    isMagnified: boolean;
  }

  const [iconState, setIconState] = useState<IconState>({
    isLiked: false,
    isStarred: false,
    isMagnified: false,
  });

  const handleToggle = (icon: keyof IconState) => {
    setIconState((prev) => ({ ...prev, [icon]: !prev[icon] }));
  };

  return (
    <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 0, y: 0 }}
    transition={{ duration: 0.8 }}
    whileInView={{ opacity: 1 }}
    viewport={{ once: true }}
  >
    <Card
      className="border-none bg-background/60 dark:bg-default-100/50 max-w-[610px] mt-5 mb-5" // Adjust the margin as needed
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
          {/* Heart icon */}
          <button onClick={() => handleToggle("isLiked")} className="focus:outline-none mr-4">
            {iconState.isLiked ? (
              <HeartIcon className="h-6 w-6 fill-current" />
            ) : (
              <OutlineHeart className="h-6 w-6 stroke-current" />
            )}
          </button>

          {/* Star icon */}
          <button onClick={() => handleToggle("isStarred")} className="focus:outline-none mr-4">
            {iconState.isStarred ? (
              <StarIcon className="h-6 w-6 fill-current" />
            ) : (
              <OutlineStar className="h-6 w-6 stroke-current" />
            )}
          </button>

          {/* Magnifying glass icon */}
          <button onClick={() => handleToggle("isMagnified")} className="focus:outline-none">
            {iconState.isMagnified ? (
              <MagnifyingGlassCircleIcon className="h-6 w-6 fill-current" />
            ) : (
              <OutlineGlassCircle className="h-6 w-6 stroke-current" />
            )}
          </button>

         
        </div>
      </CardBody>
    </Card>
    </motion.div>
  );
};

export default QuestionCard;
