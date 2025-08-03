import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";

function App() {
  return (
    <>
      <Btn />
      <Header />
      <Main />
    </>
  )
}

function Header() {
  return (
    <header>
      <div className='head_container'>
        <div className='h_cotainer'>
          <img className='header_img' src="https://i.postimg.cc/nzV4mFTY/icon12.png" alt="logotip" />
          <h1 class='title_text'>| Подземная сеть геймдева</h1>
        </div>
        <div>
          <ul className='header_btns'>
            <li><a>Кнопка 1</a></li>
            <li><a>Кнопка 2</a></li>
            <li><a>Кнопка 3</a></li>
            <li><a>Кнопка 4</a></li>
          </ul>
        </div>
      </div>
    </header>
  )
}

function Main() {
  return (
    <main>
      <Welcome />
      <Games />
    </main>
  )
}

function Welcome() {
  return (
    <section className='welcome'>
      <div className='main_container'>
        <div className=''>

        </div>
      </div>
    </section>
  )
}

function Games() {
  return (
    <section className='games'>
      <div className='main_container'>
        <div>

        </div>
      </div>
    </section>
  )
}

function Btn() {
  return (
      <button onClick={sendRequest}>Кнопка</button>
  )
}

async function sendRequest() {
  axios.get('http://localhost:8000')
  .then(resp => {
      console.log(resp.data);
  })
  .catch(error => {
      console.error('блин', error);
  });
}

export default App
