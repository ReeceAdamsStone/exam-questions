import React, { useState, useEffect } from "react";
import { Autocomplete, AutocompleteItem } from "@nextui-org/react";

interface Question {
  id: number;
  question_string: string;
  // Add other properties if needed
}

export default function AutoCompleteQuestions() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await fetch("http://127.0.0.1:5000/api/questions");
      const data = await response.json();
      setQuestions(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []); // This effect will run once when the component mounts

  return (
    <Autocomplete
      defaultItems={questions}
      label="Search for any quesition here"
      placeholder="Want to search for a specific question?"
      description="Try key words like Scrooge, Power or Memory!"
      isLoading={isLoading}
      onOpenChange={(isOpen) => {
        if (isOpen && questions.length === 0) {
          fetchData(); // Fetch data when the user opens the autocomplete and data is not loaded
        }
      }}
    >
      {(question) => (
        <AutocompleteItem key={question.id}>{question.question_string}</AutocompleteItem>
      )}
    </Autocomplete>
  );
}