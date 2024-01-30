import type { Metadata } from 'next'
import './globals.css'
import React from 'react';
import { Inder } from 'next/font/google'
import { Providers } from './components/providers';
import ThemeSwitcher from './components/ThemeSwitcher';


const inder = Inder ({ 
  subsets: ['latin'],
  weight: ['400']
 })

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark" style={{ colorScheme: "dark"}}>
      <body className={inder.className}>
        <Providers> 
        <header>
          <ThemeSwitcher></ThemeSwitcher>

        
        <p>Placeholder Header</p>
        </header>

        <main>
        {children}
        </main>
        <footer>  
        <p>
          Placeholder Footer
        </p>

        </footer>
        </Providers>
        </body>
        
    </html>
  );
}

