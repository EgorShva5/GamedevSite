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
                    Как попасть в инициативу <span style="color: #259073;">"Сеть геймдева"</span>?
                </h1>
            </div>

            <div class = 'Introduction'>  
                <img src = 'https://i.postimg.cc/MZVSMgF4/image.png' width="270px" height="270px" class="corner_img" alt = 'Лого'></img>
                <div class="centerText">
                    <div class="textUp">
                        <h2>
                            <span style="color: #259073;">Чем полезен проект разработчикам?</span>
                        </h2>
                        <p>
                            <span style="color: #259073;">«Сеть геймдева»</span> — шанс для инди‑разработчиков заявить о проекте и привлечь активную аудиторию.
                            Российские команды сталкиваются со сложностями в платежах, ограничениями площадок и высокой конкуренцией, что ведёт к низким продажам и слабой вовлечённости.
                            <br></br> <br></br>
                            Наша инициатива <b>бесплатно</b> поддерживает независимые студии и помогает им выйти на новую аудиторию.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class = 'FirstPar'>
        <div class="content">
            <div class="centerText">
                <h2>
                    <span style="color: #259073;"> <i>Сообщество Discord</i> - основа проекта.</span>
                </h2>
            </div>
            <div class = 'MainPart'>  
                <div class="centerText">
                    <p>
                        <span style="color: #259073;">«Сеть геймдева»</span> имеет сообщество в мессенджере «Discord». На данный момент именно оно является основой нашего проекта. <br></br><br></br>
                        Для того чтобы попасть в инициативу вы должны следовать следующим инструкциям:
                        
                    </p>
                </div>
                <ol style="color: white">
                    <li>Зайти на сервер «Подземная сеть геймдева».</li>
                    <li>Найти канал «Регистрация» и заполнить закреплённую там форму.</li>
                </ol>
            </div>
        </div>
    </section>
    
    <section class="FinalPart">
        <div class="content">
            
            <div class="FinalPartDiv">
                <div class="textUp">
                    <h2>
                        <span style="color: #259073;">Сообщество Discord - основа проекта.</span>
                    </h2>
                    <p>
                        После одобрения заявки вам присвоят статус «Участник общего соглащения» и создадут блог разработчика на данном сервере. <br></br><br></br>
                        При наличии у вас собственного сервера/сообщества в «Discord», ссылку на него опуюликует в канале «Наши сервера»<br></br><br></br>
                        По желанию участника мы можем так же создать отдельные странички игр и разработчика на официальном сайте инициативы(Т.е здесь).<br></br><br></br>
                    </p>
                </div>
                <img id="rot_img" src="https://i.postimg.cc/GhKxXhfy/image.png" width="300xp" height="300px" alt="Дискорд"></img>
            </div>
        </div>
    </section>

</template>

<style lang="css" scoped>
    p {
        text-shadow: 0 0 0.2em black;
        margin: 4px;
        font-size: 20px;
    }

    .centerText {
        text-align: center;
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

    .corner_img {
        transition: all .2s;
        border-radius: 90%;
    }

    .corner_img:hover {
        transform: rotate(-15deg)
    }

    .textUp {
        margin-left: 20px;
        margin-right: 20px;
        display: flex;
        flex-direction: column;
    }

    .zachem {
        background-color: rgb(20,20,20);
        color: antiquewhite;
    }

    #rot_img {
        transition: all .2s;
    }

    #rot_img:hover{
        transform: rotate(15deg)
    }

    .FinalPart {
        background-color: rgb(20,20,20);
        color: antiquewhite;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .FinalPart h2 {
        margin-top: auto;
    }

    .FinalPartDiv {
        max-width: 1000px;
        min-height: 400px;
        height: auto;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        text-align: center;
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
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .MainHeading {
        color: antiquewhite;
        font-size: 30px;
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
</style>