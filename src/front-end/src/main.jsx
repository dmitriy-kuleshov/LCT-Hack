import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import 'react-chat-elements/dist/main.css'
import { createGlobalStyle } from 'styled-components'

const GlobalCss = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');


  *{
    box-sizing: border-box;
    font-family: "Montserrat", sans-serif;
  }
`

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <GlobalCss />
  </React.StrictMode>
)
