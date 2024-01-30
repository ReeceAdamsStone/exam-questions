'use client'

import { useEffect, useState } from 'react'
import { useTheme } from 'next-themes'
import { Button } from '@nextui-org/button'
import { SunIcon, MoonIcon, SparklesIcon } from '@heroicons/react/20/solid'

export default function ThemeSwitcher() {
  const [mounted, setMounted] = useState(false)
  const { theme, setTheme } = useTheme()

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) return null

  return (
    <div className='flex gap-4'>
        
      <Button size='sm' variant='flat' onClick={() => setTheme('light')}>
       <SunIcon>
       </SunIcon>
      </Button>
      <Button size='sm' variant='flat' onClick={() => setTheme('dark')}>
        <MoonIcon>
        </MoonIcon>
      </Button>
      <Button size='sm' variant='flat' onClick={() => setTheme('modern')}>
        <SparklesIcon>
        </SparklesIcon>
      </Button>
    </div>
  )
}