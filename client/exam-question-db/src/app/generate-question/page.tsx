"use client"
// Home.jsx
import React, { useState } from 'react';
import AccordionSection from '../components/AccordionSection';
import AutoCompleteQuestions from '../components/AutocompleteQuestions';
import QuestionsCard from '../components/QuestionsInfo';
import { Providers } from '../components/providers';

const Home = () => {
  const [questions, setQuestions] = useState([]);

  const handleFetchQuestions = (fetchedQuestions) => {
    setQuestions(fetchedQuestions);
  };

  return (
    <Providers>
      <div className="flex h-screen">
        {/* Left Column */}
        <div className="flex-1 flex flex-col">
          {/* AutoCompleteQuestions component */}
          <div className="flex items-center justify-center bg-background/60 dark:bg-default-100/50 p-4">
            <AutoCompleteQuestions />
          </div>

          {/* QuestionsCard component in two columns */}
          <div className="flex flex-1">
            <div className="flex-1 p-2">
              <QuestionsCard questions={questions.slice(0, Math.ceil(questions.length / 2))} />
            </div>
            <div className="flex-1 p-2">
              <QuestionsCard questions={questions.slice(Math.ceil(questions.length / 2))} />
            </div>
          </div>
        </div>

        {/* Right Column */}
        <div className="w-72 p-4">
          <AccordionSection
            endpoint="http://127.0.0.1:5000/api/components"
            sectionName="Components"
            keyField="component_id"
            onFetchQuestions={handleFetchQuestions}
          />

          <AccordionSection
            endpoint="http://127.0.0.1:5000/api/papers"
            sectionName="Papers"
            keyField="paper_id"
            onFetchQuestions={handleFetchQuestions}
          />

          <AccordionSection
            endpoint="http://127.0.0.1:5000/api/topics"
            sectionName="Topics"
            keyField="component_id"
            onFetchQuestions={handleFetchQuestions}
          />
        </div>
      </div>
    </Providers>
  );
};

export default Home;
