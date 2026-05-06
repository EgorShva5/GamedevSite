<script setup>
    import icon from '/icon.png'
    import greenScreen from '../assets/green_sc.jpg'

    let username = ''
    let password = ''

    async function EnterReq() {
        console.log(username, password)
    }

</script>

<template>
    <section class = 'FirstPar'>
        <div class="content">
            <div class = 'MainPart'>  
                <div class="centerText">
                    <h1>
                        <span style="color: #259073;">Вход</span>
                    </h1>
                    <input v-model="username" class="textbox" type="text" name="username" placeholder="Enter Username" required><br>
                    <input v-model="password" class="textbox" type="password" name="password" placeholder="Enter Password" required>
                    <p class = 'SimpleText'><i><SUP>Нет аккаунта? <router-link to="/registration">Регистрация</router-link></SUP></i></p>
                    <a @click = 'EnterReq()'>Отправить данные</a> 
                </div>
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
        max-width: 70%;
        height: 70vh;
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