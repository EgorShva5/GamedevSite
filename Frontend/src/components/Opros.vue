<script setup>
    import { compile, ref, Transition, computed, onMounted } from 'vue'
    import icon from '/icon.png'
    import greenScreen from '../assets/green_sc.jpg'

    let username = ''
    let password = ''

    let opr = ref();

    async function opr_pr() {
        opr.value = 'Опрос пройден!'
    }

</script>

<template>
    <section class = 'FirstPar'>
        <div class="content">
            <div class = 'MainPart'>  
                <div class="centerText">
                    <h1>
                        <span style="color: #31b74aff;">{{opr}}</span>
                    </h1>

                    <h1>
                        <span style="color: #259073;">Опрос</span>
                    </h1>
                    <br>
                    
                    <p class = 'SimpleText'>Какой жанр игр вам нравится больше всего?</p>
                    <input type='radio'>Экшен</input><input type='radio'>РПГ</input><input type='radio'>Стратегия</input><input type='radio'>Шутер</input>
                    <br><br>
                    <p class = 'SimpleText'>Какой жанр вы предпочитаете для игры в одиночку?</p>
                    <input type='radio'>Приключения</input><input type='radio'>Симулятор</input><input type='radio'>Головоломка</input><input type='radio'>Хоррор</input>
                    <br><br>
                    <p class = 'SimpleText'>Какой жанр вам совсем не интересен?</p>
                    <input type='radio'>Спорт</input><input type='radio'>Гонки</input><input type='radio'>Файтинг</input><input type='radio'>Платформер</input>
                    <br><br>
                    <p class = 'SimpleText'>В какой жанр вы хотели бы поиграть в ближайшее время?</p>
                    <input type='radio'>Королевская битва</input><input type='radio'>Песочница</input><input type='radio'>Выживание</input><input type='radio'>MMO RPG</input>
                    <br><br>
                    <p class = 'SimpleText'>Какой жанр вы считаете самым увлекательным?</p>
                    <input type='radio'>Стелс</input><input type='radio'>Открытый мир</input><input type='radio'>Рогалик</input><input type='radio'>Строительство</input>
                    <br><br>
                    <a class = 'SimpleBtn' @click = 'opr_pr()'>Отправить</a>

                </div>
            </div>
        </div>
    </section>
</template>

<style lang="css" scoped>

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
    p {
        text-shadow: 0 0 0.2em black;
        margin: 4px;
        font-size: 20px;
    }

    .centerText {
        text-align: center;
    }

    input[type="text"], input[type="password"], input[type="email"] {
        width: 90%;
        padding: 12px;
        margin: 5px 0;
        border: none;
        border-radius: 5px;
        text-align: center;
        font-family: 'Jost';
        font-weight: bold;
        font-style: oblique;
        font-size: 25px;
    }

    .FirstPar {
        color: antiquewhite;
        align-items: center;
        background-color: rgb(20,20,20);
        background-image: url(https://i.postimg.cc/tTBJwTKs/2025-08-15-17-14-45.png);
        background-repeat: repeat;
        background-size: cover;
        background-position: center;
        min-height: 400px;
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .MainPart {
        margin: auto;
        height: 90vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .content {
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
</style>