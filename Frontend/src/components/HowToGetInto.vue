<script setup>
    import icon from '/icon.png'
    import greenScreen from '../assets/green_sc.jpg'
</script>

<template>
    
    <section class = 'zachem'>
        <div class = 'content'> 
            <div class="centerText">
                <br></br><br></br>
                <h1 class="MainHeading">
                    Как попасть в инициативу "Сеть геймдева"?
                </h1>
                <br></br>
                <h2>
                    Чем полезен проект разработчикам?
                </h2>
            </div>

            <div class = 'Introduction'>  
                <img :src = 'icon' width="300px" height="300px" alt = 'Лого'></img>
                <div class="centerText">
                    <p>
                        «Сеть геймдева» — шанс для инди‑разработчиков заявить о проекте и привлечь активную аудиторию.
                        Российские команды сталкиваются со сложностями в платежах, ограничениями площадок и высокой конкуренцией, что ведёт к низким продажам и слабой вовлечённости.
                        <br></br> <br></br>
                        Наша инициатива бесплатно поддерживает независимые студии и помогает им выйти на новую аудиторию.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <section class = 'FirstPar'>
        <div class="content">
            <div class="centerText">
                <br></br>
                <h2>
                    Сообщество Discord - основа проекта.
                </h2>
            </div>
            <div class = 'MainPart'>  
                <div class="centerText">
                    <p>
                        "Сеть геймдева" имеет сообщество в мессенджере "Discord". На данный момент именно оно является основой нашего проекта.
                    </p>
                </div>
            </div>
        </div>
    </section>
    
 
</template>

<style lang="css" scoped>
    p {
        margin: 4px;
        font-size: 20px;
    }

    .centerText {
        text-align: center;
    }
    
    .FirstPar {
        color: antiquewhite;
        align-items: center;
        background-image: url(https://i.postimg.cc/wjspGNgv/image.png);
        background-repeat: repeat;
        background-size: cover;
        background-position: center;
        background-position-x: -150px;
    }

    .corner_img {
        border-radius: 90%;
    }

    .zachem {
        background-color: rgb(20,20,20);
        color: antiquewhite;
    }

    .Introduction {
        margin: auto;
        max-width: 70%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        min-height: 350px;
        height: auto;
    }

    .MainPart {
        margin: auto;
        max-width: 70%;
        min-height: 400px;
        height: auto;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .MainHeading {
        color: antiquewhite;
        font-size: 30px;
    }
    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .center.text_w *{
        color: antiquewhite;
        max-width: 50vw;
    }

    .content {
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    .Btn {
        border-radius: 30%;
        padding: 3px;
        background-color: #259073;
        text-decoration: none;
        color: rgb(0, 0, 0);
        transition: all .2s;
        cursor: pointer;
    }

    .Btn:hover {
        border-radius: 45%;
        text-shadow: 0px 0px 20px #259073;
    }

    .raz_rabs {
        background-color: rgb(20,20,20);
    }

    .dev_div {
        display: flex;
        flex-direction: row;

        align-items: center;
        justify-content: center;
    }

    .dev_card {
        margin: 30px;
        color: antiquewhite;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;

        max-width: 220px;

        img {
            width: 200px;
            height: 200px;
            border-radius: 100%;
        }
    }
</style>