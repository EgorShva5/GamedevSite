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
            <br></br>
            <div class="center text_w">
                <h1 class = 'MainHeading'>О проекте</h1>
                <p>Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап</p>
            </div>
            <br></br><br></br>
            <div class="center text_w">
                <h1 class = 'MainHeading'>Что мы использовали:</h1>
                <p>Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап. Ехал грека через реку видит грека в реке рак сунул грека руку в реку рак за руку греку цап</p>
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