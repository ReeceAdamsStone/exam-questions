import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

function PageHero() {
  return (
    <div className="w-screen h-screen text-white">
      <div className="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
        <Image
          className="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center"
          alt="hero"
          src="/ExamIcon.png" 
          width={300}
          height={200}
        />
        <div className="text-center lg:w-6/12 w-full">
          <h1 className="my-4 text-5xl font-bold leading-tight">
            Generate Exam Style Questions Based on YOUR revision topics!
          </h1>
          <p className="text-2xl mb-8">
            Created by teachers, for students &#10004;&#65039; <br /> In compliance with AQA expectations &#10004;&#65039; <br /> Dynamically Generated, Interactive Mark Schemes &#10004;&#65039; <br /> <br /> Click below to create new, up to date exam style questions! 
          </p>
          <div className="flex justify-center mx-auto">
  <Link href="generate-question">
    <div className="hover:underline text-xl bg-white text-gray-800 font-bold rounded-full py-4 px-8">
      Generate Questions
    </div>
  </Link>
  <Link href="mark-scheme">
    <div className="ml-4 hover:underline text-xl bg-white text-gray-800 font-bold rounded-full py-4 px-8">
      Mark Schemes!
    </div>
  </Link>
</div>
        </div>
      </div>
    </div>
  );
}

export default PageHero;
