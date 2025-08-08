import { useState, useEffect } from 'react'
import placeholderBurger from './assets/placeholder-burger.jpg'
import neckhurts from './assets/neckhurts.png'
import icon from '/icon.png'
import './App.css'

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
              <img className="header_img" src={icon} alt='Лего' />
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
                <p style={{color: "antiquewhite"}}>Мы - независимые разработчики из России, Беларуси, Казахстана, Украины и других стран бывшего Советского Союза. Среди нас уже больше 5 различных студий, создающих игры для вас! В творениях участников сообщества представлены игры различных жанров - от приключений до vampirelike.</p>
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
              <div id ='game_box' className="slides">
                  <div className="slide"><img src={placeholderBurger}/><h1>Devastablance. Mountain Brotherhood</h1></div>
                  <div className="slide"><a href='https://www.youtube.com/watch?v=Hr5xdIWHljA' target='_blank'><img src={neckhurts}/></a><h1>NECKHURTS</h1></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
                  <div className="slide"><img src={placeholderBurger}/></div>
              </div>
              
            <Controls />
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

function Controls() {
  const [currentNum, setCurrentNum] = useState(1);
  const perMove = 3;
  const maxPages = 3

  let btns = []
  
  for (let i=1; i <= 3; i++) {
    btns.push(<button id = {`slider${i}`} type='button' onClick={() => setCurrentNum(i)}>{i}</button>)
  }

  function hideAllGames(blocks) {
    blocks.forEach(element => { 
      element.style.display = 'none';
    });
  }
  function showCurrentGames(blocks) {
    hideAllGames(blocks);
    
    Array.from(blocks).slice((currentNum - 1) * perMove, (currentNum - 1) * perMove + perMove ).forEach(element => {
      element.style.display = 'block';
    });
  }

  function BtnsDisable() {
    btns.forEach((btn) => btn.props['disabled'] = true)
  }

  function FadeOut(box_opacity, game_box) {
    box_opacity = 1.0

    let timer = setInterval(function() {
      if (!game_box) console.error('Не существует')
      if (box_opacity <= 0) {
        clearInterval(timer);
        BtnsDisable()
      } 
      else {
        box_opacity -= 0.02
        game_box.style.opacity = box_opacity
      }
    }, 20);
  }

  function FadeIn(box_opacity, game_box) {
    box_opacity = 0.0

    let timer = setInterval(function() {
      if (!game_box) console.error('Не существует')
      if (box_opacity >= 1) {
        clearInterval(timer);
      } 
      else {
        box_opacity += 0.02
        game_box.style.opacity = box_opacity
      }
    }, 20);
  }

  useEffect(() => {
    const game_box = document.getElementById('game_box')
    let box_opacity = game_box.style.opacity 

    FadeOut(box_opacity, game_box)

    const blocks = document.querySelectorAll('.slide');
    showCurrentGames(blocks);
    
    FadeIn(box_opacity, game_box)
    
  }, [currentNum]);

  return (
    <div className="controls">
      {btns}
    </div>
  );
}

export default App
