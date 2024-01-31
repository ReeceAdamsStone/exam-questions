import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import {
  Card,
  CardBody,
  useDisclosure,
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
} from "@nextui-org/react";
import {
  HeartIcon,
  StarIcon,
  MagnifyingGlassCircleIcon,
} from "@heroicons/react/20/solid";
import {
  HeartIcon as OutlineHeart,
  StarIcon as OutlineStar,
  MagnifyingGlassCircleIcon as OutlineGlassCircle,
} from "@heroicons/react/24/outline";

interface Topic {
  id: number;
  name: string;
}

interface Question {
  id: number;
  question_string: string;
  topic: Topic;
}

interface IconState {
  isLiked: boolean;
  isStarred: boolean;
  isMagnified: boolean;
}

interface ModalContentData {
  id: number;
  question_string: string;
  topic: Topic;
}

const QuestionCard: React.FC<{ question: Question }> = ({ question }) => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [modalContent, setModalContent] = useState<ModalContentData | null>(null);
  const [iconState, setIconState] = useState<IconState>({
    isLiked: false,
    isStarred: false,
    isMagnified: false,
  });

  const handleToggle = (icon: keyof IconState) => {
    setIconState((prev) => ({ ...prev, [icon]: !prev[icon] }));
  
    switch (icon) {
      case "isLiked":
        setModalContent(null); // Reset modal content when Liked icon is clicked
        break;
      case "isStarred":
        setModalContent(null); // Reset modal content when Starred icon is clicked
        break;
      case "isMagnified":
        onOpen();
        setModalContent(question);
        break;
      default:
        break;
    }
  };

  useEffect(() => {
    if (!isOpen) {
      setIconState((prev) => ({ ...prev, isMagnified: false }));
    }
  }, [isOpen]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 0, y: 0 }}
      transition={{ duration: 0.8 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true }}
    >
      <Card
        className="border-none bg-primary-300 dark:bg-default-100/50 max-w-[610px] mt-5 mb-5"
        shadow="sm"
      >
        <CardBody>
          <div className="flex flex-col items-start gap-1">
            <h3 className="font-semibold text-foreground/90">
              Topic: {question.topic.name}
            </h3>
            <p className="text-small text-foreground/80">{question.id}</p>
            {question.question_string.split("\n").map((line, index) => (
              <p
                key={index}
                className={`text-large font-medium${index === 0 ? "" : " ml-2"}`}
              >
                {index === 0 ? line : ` ${line}`}
              </p>
            ))}
          </div>

          <div className="flex flex-col mt-3 gap-1">
            {/* Add your custom content here */}
          </div>

          <div className="flex w-full items-center justify-center">
            {/* Heart icon */}
            <button
              onClick={() => handleToggle("isLiked")}
              className="focus:outline-none mr-4"
            >
              {iconState.isLiked ? (
                <HeartIcon className="h-6 w-6 fill-current" />
              ) : (
                <OutlineHeart className="h-6 w-6 stroke-current" />
              )}
            </button>

            {/* Star icon */}
            <button
              onClick={() => handleToggle("isStarred")}
              className="focus:outline-none mr-4"
            >
              {iconState.isStarred ? (
                <StarIcon className="h-6 w-6 fill-current" />
              ) : (
                <OutlineStar className="h-6 w-6 stroke-current" />
              )}
            </button>

            {/* Magnifying glass icon */}
            <button
              onClick={() => handleToggle("isMagnified")}
              className="focus:outline-none mr-4"
            >
              {iconState.isMagnified ? (
                <MagnifyingGlassCircleIcon className="h-6 w-6 fill-current" />
              ) : (
                <OutlineGlassCircle className="h-6 w-6 stroke-current" />
              )}
            </button>
          </div>
        </CardBody>
      </Card>

      {/* Modal */}
      <Modal isOpen={isOpen} onOpenChange={onClose} className="bg-primary-300" size="5xl">
        <ModalContent>
          <ModalHeader className="flex flex-col gap-1">{/*space for a title*/}</ModalHeader>
          <ModalBody>
            {modalContent && (
              <>
                <div className="flex flex-col items-start gap-1">
                  {modalContent.topic && (
                    <h3 className="font-semibold text-foreground/90">
                      Topic: {modalContent.topic.name}
                    </h3>
                  )}
                  {modalContent.id && (
                    <p className="text-small text-foreground/80">{modalContent.id}</p>
                  )}
                  {modalContent.question_string &&
                    modalContent.question_string.split("\n").map((line, index) => (
                      <p
                        key={index}
                        className={`text-large font-medium${index === 0 ? "" : " ml-2"}`}
                      >
                        {index === 0 ? line : ` ${line}`}
                      </p>
                    ))}
                </div>
                <div className="flex flex-col mt-3 gap-1">
                  {/* Add your custom content here. SPACE FOR MARKS + TIME LIMIT + AOs (can be showing further info on hover) */}
                </div>
              </>
            )}
          </ModalBody>
          <ModalFooter>
            <Button color="warning" onPress={onClose}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </motion.div>
  );
};

export default QuestionCard;
