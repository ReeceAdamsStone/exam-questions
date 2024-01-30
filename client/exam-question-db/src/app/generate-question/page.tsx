"use client"
// Home.jsx
import React, { useState } from 'react';
import AccordionSection from '../components/AccordionSection';
import AutoCompleteQuestions from '../components/AutocompleteQuestions';
import QuestionsCard from '../components/QuestionsCard';
import { Providers } from '../components/providers';

import { Inder } from 'next/font/google'

const inder = Inder ({ 
  subsets: ['latin'],
  weight: ['400']
 })



const Home = () => {
  const [questions, setQuestions] = useState([]);

  const handleFetchQuestions = (fetchedQuestions) => {
    setQuestions(fetchedQuestions);
  };

  return (
    <Providers>
    <div style={{ display: 'flex' }}>

<div>
  
        <AutoCompleteQuestions />
        <QuestionsCard questions={questions} />
      </div>
      <div>
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
