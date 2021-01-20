import React from 'react'
import { BrowserRouter as Router } from  'react-router-dom';
import BaseRouter from "./components/routes"

function App() {
  return (
    <div className="App">
      <Router>
        <BaseRouter />
      </Router>
    </div>
  )
}

export default App
