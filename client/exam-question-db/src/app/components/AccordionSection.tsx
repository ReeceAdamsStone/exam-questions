"use client"

import React, { useState, useEffect } from "react";
import { CheckboxGroup, Checkbox, Button } from "@nextui-org/react";
import QuestionsCard from "./QuestionsInfo";

interface AccordionSectionProps {
  endpoint: string;
  sectionName: string;
  keyField?: string;
  onFetchQuestions: (questions: Question[]) => void;
}

interface ComponentData {
  component_id: number;
  component_name: string;
  marks: number;
  paper_id: number;
  topic_id: number;
}

interface Paper {
  paper_id: number;
  paper_name: string;
}

interface Topic {
  topic_id: number;
  topic_name: string;
}

interface Question {
  id: number;
  question_string: string;
  topic: {
    id: number;
    name: string;
  };
}

const AccordionSection: React.FC<AccordionSectionProps> = ({
  endpoint,
  sectionName,
  keyField = "id",
  onFetchQuestions,
  
}) => {
  const [data, setData] = useState<any[]>([]);
  const [selectedItems, setSelectedItems] = useState<string[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [isSectionOpen, setIsSectionOpen] = useState(false);
  const [papersData, setPapersData] = useState<Paper[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        setData(data);
        // Fetch papers data
        const papersResponse = await fetch('http://127.0.0.1:5000/api/papers');
        const papersData = await papersResponse.json();
        setPapersData(papersData);
      } catch (error) {
        console.error(`Error fetching data from ${endpoint}:`, error);
      }
    };

    fetchData();
  }, [endpoint]);

  const getCheckboxLabel = (item: Paper | Topic | ComponentData) => {
    if ("component_id" in item && "paper_id" in item) {
      // If it's ComponentData, show component name and paper name (if available)
      const paperName = papersData.find((paper) => paper.paper_id === item.paper_id)?.paper_name || '';
      return `${item.component_name} - ${paperName}`;
    } else if ("paper_id" in item) {
      // If it's Paper, show paper name
      return ` ${item.paper_name}`;
    } else if ("topic_name" in item) {
      // If it's Topic, show topic name
      return `${item.topic_name}`;
    } else {
      return "Unable to source category data";
    }
  };
  
  const handleFetchQuestions = async () => {
    try {
      // Fetch questions associated with the selected items
      const questionsResponse = await fetch(
        `http://127.0.0.1:5000/api/questions?components=${selectedItems.join(",")}`
      );
      const questionsData = await questionsResponse.json();
      // Filter questions based on selected items
      const filteredQuestions = questionsData.filter((question: Question) => {
        return selectedItems.includes(String(question.topic.id));
      });
      
      // Update state with filtered questions
      setQuestions(filteredQuestions);
      onFetchQuestions(filteredQuestions);
      // Do something with the fetched questions data
      console.log(`Fetched Questions for ${sectionName}:`, filteredQuestions);
    } catch (error) {
      console.error(`Error fetching questions for ${sectionName}:`, error);
    }
  };

  return (
    <div className="border-none bg-primary-300 dark:bg-default-100/50 max-w-[610px] mt-5 mb-5 text-center text-lg font-semibold">
      <div
        onClick={() => setIsSectionOpen((prev) => !prev)}
      >
        {sectionName}
      </div>
      {isSectionOpen && (
        <div>
          <CheckboxGroup
          className="text-left font-normal bg-background"
            label={`Select the ${sectionName.toLowerCase()} you would like questions for`}
            orientation="vertical"
            onChange={(values) => setSelectedItems(values)}
          >
            {data.map((item) => (
              <Checkbox key={`${sectionName}-${item[keyField]}`} value={String(item[keyField])}>
                {getCheckboxLabel(item)}
              </Checkbox>
            ))}
          </CheckboxGroup>
          <Button onClick={handleFetchQuestions} className="align-middle px-unit-2 py-unit-1 min-w-unit-4xl ">Get Questions</Button>
        </div>
      )}
    </div>
  );
};

export default AccordionSection;

