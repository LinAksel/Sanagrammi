import { useState, useEffect } from 'react'

const API_URL = process.env.NEXT_PUBLIC_API_URL

export default function Home() {
  const [word, setWord] = useState()
  const [userWord, setUserWord] = useState()
  const [anagrams, setAnagrams] = useState([])
  const [time, setTime] = useState(60)
  const getWord = () => {
    fetch(`${API_URL}/reader`)
      .then(response => response.json())
      .then(data => setWord(data[0]))
  }
  const handleSubmit = async event => {
    event.preventDefault()
    let data = await fetch(`${API_URL}/check`, {
      mode: 'cors',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ word, candidate: userWord })
    }).then(res => res.json())

    if (data.correct && !anagrams.includes(userWord) && word !== userWord) {
      setAnagrams(anagrams.concat(userWord))
    }

    setUserWord('')
  }

  useEffect(() => {
    getWord()
  }, [])

  useEffect(() => {
    if (time >= 0) {
      setTimeout(() => setTime(time - 1), 1000)
    } else {
      setTime(60)
      setAnagrams([])
      getWord()
    }
  }, [time])

  return (
    <div id="main">
      <h1 style={{ fontSize: 100 }}>{time}</h1>
      <h1>
        {word}
      </h1>
      <form onSubmit={handleSubmit}>
        <input value={userWord} onChange={event => setUserWord(event.target.value)} />
      </form>
      <div>
        {anagrams.map(a => <div key={a}>{a}</div>)}
      </div>
    </div>
  )
}