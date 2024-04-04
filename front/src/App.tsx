import './App.css'
import BookSection from './components/BookSection'
import NavBar from './components/NavBar'
import { Container } from '@mui/material'
import UserSection from './components/UserSection'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <NavBar/>
      <Container>
        <BookSection/>
        <UserSection/>
      </Container>
    </>
  )
}

export default App
