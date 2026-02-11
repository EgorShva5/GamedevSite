<script setup>
    import Sanya from '../assets/201072348.png'
    import Goga from '../assets/GoogPlayIco.jpg'

</script>

<template>
    <section class = 'raz_rabs'>
        <div class="content">
            <div class = 'center'>
                <br/>
                <h1 class="MainHeading">Разработчики проекта:</h1>
                <br/>
            </div>
            <div class = 'dev_div'>
                <div class="dev_card">
                    <img :src = 'Sanya' alt="Саня"></img>
                    <h1>rabiNyoom</h1>
                    <p>Пишет фронт и бек, вообще крутой чел, гений просто</p>
                    <p><a href="https://github.com/rabiNyoom" class="Btn">GitHub</a></p>
                </div>
                <div class="dev_card">
                    <img :src = 'Goga' alt="Гога"></img>
                    <h1>EgorShva5</h1>
                    <p>Пишет фронт и бек, пытается доганть Саню</p>
                    <p><a href="https://github.com/rabiNyoom" class="Btn">GitHub</a></p>
                </div>
            </div>
        </div>
    </section>

    <section class = 'shvap'>
        <div class="content">
            <div class="center">
                <div class="row_align">
                <img src="https://i.postimg.cc/cHDMsBC0/shv.png" width="250px" height="250px" class="corner_img"></img>
                <div>
                    <div class="center text_w">
                        <h1 class = 'MainHeading'>Команда разработки</h1>
                        <p>
                            В разработке проекта принимали участие члены команды разработчиков "Shvap Games".
                        </p>
                    </div>
                
                </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="css" scoped>
    p {
        margin: 4px;
    }

    .MainHeading {
        color: antiquewhite;
        font-size: 30px;
    }
    .center {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .center.text_w *{
        color: antiquewhite;
        max-width: 50vw;
    }

    .row_align {
        display: flex;
        flex-direction: row;
    }

    .corner_img {
        transition: all .2s;
        border-radius: 100%;
    }

    .corner_img:hover {
        transform: rotate(-15deg)
    }

    .content {
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    .shvap {
        background-color: rgb(20,20,20);
        min-height: 400px;
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