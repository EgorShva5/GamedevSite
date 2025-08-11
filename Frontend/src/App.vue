<script setup>
  import icon from '/icon.png'
</script>

<template>
  <header>
    <div class = 'head_container'>
        <div class="h_cotainer">
            <router-link to = '/'><img class="header_img" :src="icon" alt='Лого'></img></router-link>
            <h1 class="title_text">| Подземная сеть геймдева</h1>
        </div>
        <div>
        <ul class = 'header_btns'>
            <li><router-link to="/about" class = 'SimpleBtn'>Каталог</router-link></li>
            <li><router-link to="/about" class = 'SimpleBtn' >О нас</router-link></li>
            <li><a class = 'SimpleBtn'>Как попасть?</a></li>
            <li><a class = 'SimpleBtn'>Войти</a></li>
        </ul>
        </div>
    </div>
  </header>

  <main>
    <router-view> </router-view>
  </main>
 
  <footer>
    <div class= 'footer'>
      <div>
          <p>Связаться с нами:</p>
          <p>Email: shvarev.egor.a@yandex.ru</p>
          <p>Tg: @ShvarevEgor</p>
          <p>Discord: shvap.studio</p>
          <p>VK: Шварёв Егор</p>
      </div>
      <div>
          <p>Связанное с проектом:</p>
          <p><a class = 'SimpleBtn' href="https://github.com/EgorShva5/GamedevSite" target='_blank'>Код на GitHub</a></p>
          <p><a class = 'SimpleBtn' href="https://discord.gg/99bqS3TX4c" target='_blank'>Сообщество Discord</a></p>
          <p><a class = 'SimpleBtn' href="https://discord.gg/EKWBWEa9vA" target='_blank'>Сообщество Shvap Games</a></p>
          <p><a class = 'SimpleBtn' href="https://github.com/EgorShva5/GamedevSite" target='_blank'>Официальный сайт Shvap</a></p>
      </div>
      <div>
          <p>Правила:</p>
          <p><a class = 'SimpleBtn' href="https://github.com/EgorShva5/GamedevSite" target='_blank'>Правила использования</a></p>
          <p><a class = 'SimpleBtn' href="https://github.com/EgorShva5/GamedevSite" target='_blank'>Политика конфиденциальности</a></p>
      </div>
    </div>
    <div class="under_footer">
        <h1>Все права защищены, Shvap Studio ©, 2025 год</h1>
    </div>
  </footer>
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

  #header_text {
    width: 80%;
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
  .h_cotainer *{
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
</style>