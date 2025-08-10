<script setup>
  import { ref, Transition } from 'vue'

  import CardController from './components/CardController.vue'

  import placeholderBurger from './assets/placeholder-burger.jpg'
  import neckhurts from './assets/neckhurts.png'
  import icon from '/icon.png'

  const show = ref(true)

  const slidesGlobal = ref([
  { img: placeholderBurger, title: "Devastablance. Mountain Brotherhood", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: neckhurts, title: "NECKHURTS", link: "https://www.youtube.com/watch?v=Hr5xdIWHljA", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "Поплава", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: icon, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
]) // 11 for now
</script>

<template>

  <header>
    <div class = 'head_container'>
        <div class="h_cotainer">
            <img class="header_img" :src="icon" alt='Лого' />
            <h1 class="title_text">| Подземная сеть геймдева</h1>
        </div>
        <div>
        <ul class = 'header_btns'>
            <li><a class = 'SimpleBtn'>Каталог</a></li>
            <li><a class = 'SimpleBtn'>О нас</a></li>
            <li><a class = 'SimpleBtn'>Как попасть?</a></li>
            <li><a class = 'SimpleBtn'>Войти</a></li>
        </ul>
        </div>
    </div>
  </header>

  <main>
    <section class="welcome">
        <div class="main_container">
            <div id ='header_text'>
                <h1 class="MainHeading" style='color: antiquewhite'>Подземная сеть геймдева</h1>
                <h1 style='color: antiquewhite'>Сообщество независимых разработчиков игр из СНГ.</h1>
                <p style='color: antiquewhite'>Мы - независимые разработчики из России, Беларуси, Казахстана, Украины и других стран бывшего Советского Союза. Среди нас уже больше 5 различных студий, создающих игры для вас! В творениях участников сообщества представлены игры различных жанров - от приключений до vampirelike.</p>
            </div>
        </div>
    </section>

    <section class='card_games'>
      <br/>
      <h1 style='color: antiquewhite; text-align: center;' class="MainHeading">Лучшие игры:</h1>

      <Transition  name = 'fade'>
      <div v-if="show" class='slider_container'>
          <div id ='Games' class="slider">           
              <div id ='game_box' class="slides">
                <template v-for='slide in slidesGlobal'>
                  <div class='slide' v-if='!slide.isHidden'>
                    <a :href='slide.link' target='_blank'>
                      <img :src="slide.img" alt="Картинка">
                    </a>
                    <h1>{{ slide.title }}</h1>
                  </div>
                </template>
              </div>
          </div>
      </div>
    </Transition>

    <CardController :show = 'show' :all-slides='slidesGlobal' @update-slides="updatedSlides => slidesGlobal = updatedSlides" @update-show="updatedShow => show = updatedShow"/>

    </section>

    <section class = 'card_devs'>
      <div class = 'slider_container'>
          <br />
          <h1 style='color: antiquewhite' class="MainHeading">Лучшие разработчики:</h1>
      </div>
    </section>


    <footer>
      <div class= 'footer'>
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
    <div class="under_footer">
        <h1>Все права защищены, Shvap Studio ©, 2025 год</h1>
    </div>
  </footer>

  </main>
</template>

<style lang="css" scoped>
  .head_container {
      background-color: rgb(20,20,20);
      padding: 0 10px;
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: center;
      margin-left: auto;
      margin-right: auto;
  }

  .SimpleBtn {
      color: antiquewhite;
      transition: all .2s;
  }

  .SimpleBtn:hover {
      color: #259073;
      text-shadow: 0px 0px 20px #259073;
  }

  .MainHeading {
      font-size: 30px;
  }

  .card_games {
      box-shadow: 0px 0px 60px rgb(10,10,10);
      background-color: rgb(20,20,20);
  }

  .card_devs {
      align-items: center;
      background-image: url(https://i.postimg.cc/RVQqW9Nj/image.png);
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
  }

  .welcome {
      margin-top: -100px;
      padding-top: 100px;
      align-items: center;
      background-image: url(https://i.postimg.cc/tCPfQ12z/image.png);
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
  }

  .main_container {
      min-height: 500px;
      height: auto;
      padding: 0 10px;
      display: flex;
      flex-direction: column;
      max-width: 80%;
      justify-content: center;
      margin-right: auto;  
      margin-left: auto;
  }

  #header_text {
    width: 80%;
    margin-right: auto;
  }

  .slider_container {
      min-height: 33vh;
      height: auto;
      padding: 0 10px;
      display: flex;
      flex-direction: column;
      max-width: 80%;
      align-items: center;
      margin-left: auto;
      margin-right: auto;  
  }

  .header_img {
      transition: all .2s;
      margin-right: 0;
      margin-left: 0;
      width: 50px;
      height: 50px;
  }

  .header_img:hover{
      cursor: pointer;
      scale: 1.2;
      margin-right: 10px;
      margin-left: 10px;
  }

  .header_btns {
      font-size: 16px;
      cursor: pointer;
      gap: 20px;
      display: flex;
      list-style: none;
  }

  #header_text {
      cursor: default;
      transition: all .1s;
      border-left: 0px solid #259073;
      padding-left: 0px;
  }

  #header_text:hover {
      border-left: 5px solid #259073;
      padding-left: 10px;
  }

  .h_cotainer {
      display: flex;
      align-items: center;
  }

  .title_text {
      margin-left: 10px;
      color: #259073;
  }

  .footer {
    min-height: 250px;
    height: auto;
    background-color: rgb(20,20,20);
    padding: 0 10px;
    display: flex;
    flex-direction: row;
    text-align: center;
    align-items: center;
    margin-left: auto;
    justify-content: space-around;
    margin-right: auto;
    color: antiquewhite;
  }

  .footer div{
    border-top: 0px solid #259073;
    transition: all .1s;
    width: 300px;
  }

  .footer div:hover{
      border-top: 5px solid #259073;
  }

  .under_footer {
      height: 100px;
      background-color: rgb(20,20,20);
      display: flex;
      justify-content: center;
      align-items: center;
      color: antiquewhite;
  }

  /* Контейнер слайдера */
  .slider {
      position: relative;
  }

  /* Контейнер, в котором будут находиться все слайды */
  .slides {
      opacity: 1.0;
      text-align: center;
      display: flex; /* Располагаем слайды в ряд */
      flex-wrap: wrap;
      justify-content: space-around;
  }

  /* Каждый отдельный слайд */
  .slide {
      max-width: 300px;
      color: antiquewhite;
      margin: 10px 10px;
      flex-shrink: 0; /* Запрещаем уменьшение элементов внутри flex-контейнера */
      img { 
          width: 300px;
          height: 300px;
          object-fit: cover;
      } /* Квадратные картинки в слайдах */
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0.0;
  }
</style>