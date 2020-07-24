import { useState, useEffect } from 'react'

export default function Home() {
  const [word, setWord] = useState()
  const [userWord, setUserWord] = useState()
  const [anagrams, setAnagrams] = useState([])
  const handleSubmit = async event => {
    event.preventDefault()
    let data = await fetch('http://127.0.0.1:5000/check', {
      mode: 'cors',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ word, candidate: userWord })
    }).then(res => res.json())

    if (data.correct && !anagrams.includes(userWord)) {
      setAnagrams(anagrams.concat(userWord))
    }

    setUserWord('')
  }

  useEffect(() => {
    fetch('http://127.0.0.1:5000/reader')
      .then(response => response.json())
      .then(data => setWord(data[0]))
  }, [])
  return (
    <div id="main">
      <h1 style={{ textAlign: "right" }}>
        {word}
      </h1>
      {/* <h1 style={{ textAlign: "left" }}>60</h1> */}
      <form onSubmit={handleSubmit}>
        <input value={userWord} onChange={event => setUserWord(event.target.value)} />
      </form>
      <div>
        {anagrams.map(a => <div key={a}>{a}</div>)}
      </div>
    </div>
  )
}