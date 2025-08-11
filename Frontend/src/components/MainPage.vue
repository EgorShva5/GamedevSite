<script setup>
  import { ref, Transition } from 'vue'

  import CardController from '../components/CardController.vue'

  import axios from "axios"

  import placeholderBurger from '../assets/placeholder-burger.jpg'
  import neckhurts from '../assets/neckhurts.png'
  import icon from '/icon.png'
  import shvIco from '../assets/GoogPlayIco.jpg'
  import rietlyIcn from '../assets/rietly.png'
  import goldhide from '../assets/GH.jpg'
  import badFantasy from '../assets/nems82.png'
  import brightMystery from '../assets/DpvPIO.png'

  const show = ref(true)
  const show_two = ref(true)

  const message = ref('')

  const slidesGlobal = ref([
  { img: placeholderBurger, title: "Devastablance. Mountain Brotherhood", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: brightMystery, title: "Bright Mystery", link: "https://www.youtube.com/watch?v=Hr5xdIWHljA", isHidden: true},
  { img: badFantasy, title: "BAD Fantasy", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "Поплава", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: icon, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
  { img: placeholderBurger, title: "", link: "https://vuejs.org/guide/introduction.html", isHidden: true},
]) // 11 for now

  const authorGlobal = ref([
    { img: shvIco, title: "Shvap", link: "https://google.com", isHidden: true},
    { img: rietlyIcn, title: "Rietly", link: "https://google.com", isHidden: true},
    { img: goldhide, title: "GoldHide games", link: "https://google.com", isHidden: true},
    { img: neckhurts, title: "NECKHURTS", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true},
    { img: placeholderBurger, title: "Mr. burger", link: "https://google.com", isHidden: true}
  ])

  async function getResponse() {
    try {
      const res = await axios.post('http://localhost:8000/Custom', {name: 'Egr'}, {timeout: 5000})
    } catch {
      message.value='failed to get response'
    }
    
    /*try {
        const resp = await axios.get('http://localhost:8000/Custom', {timeout: 3000})
        message.value=resp.data.message
      } catch {
        message.value='failed to get response'
      }*/
    }

</script>

<template>
    <section class="welcome">
        <div  class="main_container">
            <div id ='header_text'>
                <input :value="message" readonly>{{ message }}</input>
                <button @click="getResponse">Button</button>
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
          <h1 style='color: antiquewhite; text-align: center;' class="MainHeading">Лучшие разработчики:</h1>
          <Transition name = 'fade_a'>
          <div v-if="show_two" class="dev_group">
            <div class="devs">
                <template v-for="author in authorGlobal">
                  <div class='dev' v-if='!author.isHidden'>
                    <a :href='author.link' target='_blank'>
                      <img :src="author.img" alt="Картинка">
                    </a>
                    <h1>{{ author.title }}</h1>
                  </div>
                </template>
              <!---placeholderBurger-->
            </div>
          </div>
          </Transition>
      </div>
      <CardController :show_two= 'show' :all-slides='authorGlobal' @update-slides="updatedSlides => authorGlobal = updatedSlides" @update-show="updatedShow => show_two = updatedShow"/>
    </section>

    <section class = 'FinalMessage'>
      <div class = 'final_container'>
        <h1 class="MainHeading">На этом пока всё. Что же дальше?</h1>
        <p>В <a style="font-size: 25px;" class="SimpleBtn" href="https://google.com">этой статье</a> мы рассказали, что можно делать на сайте различным группам пользователей. Мы уверенны, она поможет вам освоиться здесь! <br>--- --- ---</p>
        <h3>Вступайте в наше дружное Discord-сообщество!</h3>
        <p>Здесь вы можете найти множество интересных проектов, посмотреть на блоги участников инициативы и завести множество друзей! <a style="font-size: 25px;" class="SimpleBtn" href="https://google.com" target="_blank"> Тебе стоит лишь нажать на эту ссылку.</a> Ждём тебя!</p>
      </div>
    </section>

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
    text-decoration: none;
    color: antiquewhite;
    transition: all .2s;
    cursor: pointer;
  }

  .SimpleBtn:hover {
    color: #259073;
    text-shadow: 0px 0px 10px #259073;
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
      min-height: 47vh;
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
    flex-wrap: wrap;
    align-items: center;
    margin-left: auto;
    justify-content: space-around;
    margin-right: auto;
    color: antiquewhite;
  }

  .footer p {
    margin: 10px;
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
      text-align: center;
      display: flex; /* Располагаем слайды в ряд */
      flex-wrap: wrap;
      justify-content: space-around;
  }

  /* Каждый отдельный слайд */
  .slide {
      transition: all .2s;
  
      max-width: 300px;
      color: antiquewhite;
      margin: 10px 10px;
      flex-shrink: 0; /* Запрещаем уменьшение элементов внутри flex-контейнера */
      img { 
        transition: all .2s;
        
          border-radius: 0%;
          width: 300px;
          height: 300px;
          object-fit: cover;
      } /* Квадратные картинки в слайдах */
  }

.slide:hover {
    color: #259073;

    img {
      box-shadow: 0px 0px 20px black;
      border-radius: 20%;
    }
}

  .dev_group {
    min-height: 47vh;
    height: auto;
    padding: 0 10px;
    display: flex;
    flex-direction: row;
    max-width: 80%;
    align-items: center;
    margin-left: auto;
    margin-right: auto;  
  }

  .devs {
    text-align: center;
    display: flex; /* Располагаем слайды в ряд */
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .dev {
    transition: all .2s;
    max-width: 300px;
    color: antiquewhite;
    margin: 10px 10px;
    flex-shrink: 0; /* Запрещаем уменьшение элементов внутри flex-контейнера */
    img { 
      transition: all .2s;
      border-radius: 100%;
      width: 250px;
      height: 250px;
      object-fit: cover;
    } 
  }
  
  .dev:hover {
    color: #259073;
     
    img {
      border-radius: 20%;
    }
  }

  .final_container {
    min-height: 400px;
    height: auto;
    text-align: center;
    color: aliceblue;
    background-color: rgb(20,20,20);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .final_container h3, p{
    margin: 0;
  }

  .final_container * {
    max-width: 30vw;
  }

  .fade-enter-active,
  .fade-leave-active,
  .fade_a-leave-active,
  .fade_a-enter-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to,
  .fade_a-enter-from,
  .fade_a-leave-to {
    opacity: 0.0;
  }
</style>