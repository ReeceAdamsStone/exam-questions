"use client"

import React from 'react';
import AccordionSection from '../components/AccordionSection';

const Home = () => {
  return (
    <div style={{ display: 'flex' }}>
      <div style={{ width: '300px', padding: '10px', backgroundColor: '#f0f0f0' }}>
      <AccordionSection
  endpoint="http://127.0.0.1:5000/api/components"
  sectionName="Components"
  keyField="component_id"
  
  
/>

<AccordionSection
  endpoint="http://127.0.0.1:5000/api/papers"
  sectionName="Papers"
  keyField="paper_id"
  
/>

<AccordionSection
  endpoint="http://127.0.0.1:5000/api/topics"
  sectionName="Topics"
  keyField="component_id"
  
/>
      </div>
    </div>
  );
};

export default Home;