<script setup>
  import { compile, ref, Transition, computed, onMounted } from 'vue'

  import CardController from '../components/CardController.vue'
  import TestBanner from './TestBanner.vue'

  import axios from "axios"

  import placeholderBurger from '../assets/template_vopros.png'
  import neckhurts from '../assets/neckhurts.png'
  import icon from '/icon.png'
  import shvIco from '../assets/GoogPlayIco.jpg'
  import rietlyIcn from '../assets/rietly.png'
  import goldhide from '../assets/GH.jpg'
  import badFantasy from '../assets/nems821.png' 
  import brightMystery from '../assets/DpvPIO2.png'
  import dev_icon from '../assets/saund2fin.png'
  import underbox from '../assets/underbox.png'
  import svo from '../assets/SVOItch.png'
  import catronns from '../assets/FNWC.png'
  import ch_pack from '../assets/CharactersPack.png'
  import racing_game from '../assets/RacingGameRe-make.png'

  const show = ref(true)
  const show_two = ref(true)

  const message = ref('')

  const per_page = 20

  let slidesGlobal = ref([
   /* { img: 'template_vopros.png', title: "Тестовое название", link: "https://store.steampowered.com/app/2894900/Devastablance_Gornoe_Bratstvo/", isHidden: false}*/
  ])

  function getImageUrl(name) {
    return new URL(`../assets/${name}`, import.meta.url).href
  }

  async function getGame(game_id) {
    try {
      const res = await axios.get('http://localhost:8000/Catalog', {params: {banner: game_id}}, {timeout: 5000}) /*('http://localhost:8000/Custom', {timeout: 5000})*/

      let data = res.data.message
      console.log(slidesGlobal.value.push({img: data.imgpath, title: data.title, link: data.linkpath, id: data.id, isHidden: true}))

    } catch {
      message.value='failed to get response'
    }
  }

  async function getGameList(start, end) {
    for (let i = start; i <= end; i++) {
      getGame(i); 
      console.log(i)
    }
  }

  onMounted(
    () => {
      getGameList(1,20);
    }
  );
</script>

<template>
    <section class="welcome">
        <div  class="main_container">
            <div id ='header_text'>
                <!--<input :value="message" readonly></input>-->
                <!--<button @click="getResponse">Button</button>-->
                <h1 class="MainHeading" style='color: antiquewhite'>Умный помощник</h1>
                <h1 style='color: antiquewhite'>Поможет подобрать интересные именно вам игры!</h1>
                <p style='color: antiquewhite'>Умный алгоритм рекомендаций определит ваши увлечения, а также подберёт игры в соответствии с выбранными тегами.</p>
                <br>
                <a href = 'https://www.google.com' id = 'create_recomendation_btn'> Найти игры!</a>
              </div>
            <!--<TestBanner/>-->
        </div>
    </section>

    <section class='card_games'>
        <br/>
        <br><br></br>
      <h1 style='color: antiquewhite; text-align: center;' class="MainHeading">Каталог игр:</h1>
        <br><br></br>
      <div class="devs">
        <template v-for='slide in slidesGlobal'>
            <div v-if="slide.isHidden===false" class='slide'>
              <router-link :to="`/game/`+slide.id"> 
                <img :src="getImageUrl(slide.img)" alt="Картинка">
              </router-link>
              <h1>{{ slide.title }}</h1>
            </div>
        </template>
      </div>
      
      <CardController :show = 'show' :all-slides='slidesGlobal' :perpage="per_page" @update-slides="updatedSlides => slidesGlobal = updatedSlides" @update-show="updatedShow => show = updatedShow"/>
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
    flex-direction: column;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0px 0px 60px rgb(10,10,10);
      background-color: rgb(20,20,20);
  }

  .card_devs {
      align-items: center;
      background-color: rgb(20,20,20);
      background-image: url(https://i.postimg.cc/RVQqW9Nj/image.png);
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
  }

  .welcome {
      align-items: center;
      background-color: rgb(20,20,20);
      background-image: url(https://i.postimg.cc/mgSGhYCb/abstract-green-light-black-shadow-line-geometric-on-dark-grey-metallic-design-modern-luxury-futurist.jpg);
      background-repeat: repeat;
      background-position: right;
  }

  .main_container {
      margin-right: auto;  
      margin-left: auto;
      min-height: 320px;
      max-width: 60%;
      height: auto;
      padding: 0 10px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

  }

  #create_recomendation_btn {
    min-width: 30vh;
    min-height: 40px;
    background-color: bisque;
    color: black;
    font-size: 20px;
    padding: 5px;
    border-radius: 10px;
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
      margin: 15px 10px;
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
    max-width: 70%;
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