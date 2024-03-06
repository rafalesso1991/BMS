import { useState, useEffect } from "react"
function App() {
  const [users, setUsers] = useState([])    
  const url = "http://localhost:8000/users/";
  const options = {
    method: "GET",
    mode: "cors",
    credentials: "omit",
    headers: {
      "Content-Type": "application/json",
    }
  }
  const getUsers = async () => {

    const allBooks = await fetch(url, options)
    const usersJSON = await allBooks.json()
    setUsers(usersJSON)
    console.log(usersJSON)
  }
  useEffect(() => {
    getUsers()
  })
  return (
    <>
      <h1 className="text-3xl font-bold underline">Hola mundo</h1>
    </>
  )
}

export default App
