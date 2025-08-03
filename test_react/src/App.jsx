import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";

function App() {
  return (
    <>
      <Header />
      <Main />
      <Footer />
    </>
  )
}

function Header() {
  return (
    <>
    <header>
      <div className = 'head_container'>
          <div className="h_cotainer">
              <img className="header_img" src = 'https://i.postimg.cc/nzV4mFTY/icon12.png' alt ='Лего' />
              <h1 className="title_text">| Подземная сеть геймдева</h1>
          </div>
          <div>
          <ul className = 'header_btns'>
              <li><a className = 'SimpleBtn'>Каталог</a></li>
              <li><a className = 'SimpleBtn'>О нас</a></li>
              <li><a className = 'SimpleBtn'>Как попасть?</a></li>
              <li><a className = 'SimpleBtn'>Войти</a></li>
          </ul>
          </div>
      </div>
    </header>
    </>
  )
}

function Main() {
  return (
    <main>
      <Welcome />
      <Games />
      <Authors />
    </main>
  )
}

function Welcome() {
  return (
    <section className="welcome">
        <div style={{alignItems: "center"}} className="main_container">
            <div id ='header_text' style={{marginRight:"auto",marginTop:"auto",marginBottom:"auto",alignItems:"center",maxWidth:60+"%"}}>
                <h1 className="MainHeading" style={{color: "antiquewhite"}}>Подземная сеть геймдева</h1>
                <h1 style={{color: "antiquewhite"}}>Сообщество независимых разработчиков игр из СНГ.</h1>
                <p style={{color: "antiquewhite"}}>Мы - независимые разработчики из России, Беларуси, Казахстана, Украины и других стран бывшего Советского Союза. Среди нас уже больше 5 различных студий, создающих игры для вас! В творениях участников сообщества представлены игры различных жанров - от приключений до vampyrelike.</p>
            </div>
        </div>
    </section>
  )
}

function Games() {
  return (
    <>
      <section className = 'card_games'>
        <div className = 'main_container'>
            <br/>
            <h1 style={{color: "antiquewhite"}} className="MainHeading">Лучшие игры:</h1>
            <div id ='Games' className="slider">

              <input type="radio" name="slider" id="slide1" checked /> 
              <input type="radio" name="slider" id="slide2"/>
              <input type="radio" name="slider" id="slide3"/>
          
              
              <div className="slides">
                  <div className="slide"><img src="static/burgplace.png" width ='300'/><h1>Devastablance. Mountain Brotherhood</h1></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
                  <div className="slide"><img src="static/burgplace.png" width="300"/></div>
              </div>
              
              <div className="controls">
                  <label for="slide1"></label>
                  <label for="slide2"></label>
                  <label for="slide3"></label>
              </div>
            </div>
        </div>
      </section>
    </>
  )
}

function Authors() {
  return (
    <section className = 'card_devs'>
      <div className = 'main_container'>
          <br />
          <h1 style={{color: "antiquewhite"}} className="MainHeading">Лучшие разработчики:</h1>
      </div>
    </section>
  )
}

function Footer() {
  return (
    <footer>
    <div className= 'footer'>
        <div>
            <p>Связаться с нами:</p>
            <p>Email: shvarev.egor.a@yandex.ru</p>
            <p>Tg: @ShvarevEgor</p>
            <p>Discord: @hfghfh</p>
            <p>VK: Шварёв Егор</p>
        </div>
        <div>
            <p>Связанное с проектом:</p>
            <p>Код на GitHub</p>
            <p>Сообщество Discord</p>
            <p>Сообщество Shvap Games</p>
            <p>Официальный сайт Shvap</p>
        </div>
        <div>
            <p>Правила:</p>
            <p>Правила использования</p>
            <p>Политика конфиденциальности</p>
        </div>
    </div>
    <div className="under_footer">
        <h1>Все права защищены, Shvap Studio ©, 2025 год</h1>
    </div>

  </footer>
  )
}

({/*function Btn() {
  return (
      <button onClick={sendRequest}>Кнопка</button>
  )
}*/})

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
