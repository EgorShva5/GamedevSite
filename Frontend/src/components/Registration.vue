<script setup>
    import { compile, ref, Transition, computed, onMounted } from 'vue'
    import axios from "axios"
    import Home from '../App.vue'

    let password = ref();
    let c_password = ref();
    let username = ref();
    let email = ref();
    let type_of_acc = ref();

    let resp = ref();

    async function registration() {
        try {
            let res = await axios.post('http://localhost:8000/Registration', {params: {username: username.value, password: c_password.value, email: email.value, type: type_of_acc.value}}, {timeout: 5000})

            console.log(res)
        } catch {
            alert('Чё-то не так');
        }
    }

    async function getPassword() {
        try {
            const res = await axios.get('http://localhost:8000/GenPassword', {timeout: 5000})
            console.log(res)
            let data = res.data.message
            password.value = data

            console.log(password)
        } catch {
            message.value='failed to get response'
        }
    }

    onMounted(
        () => {
        getPassword();
        }
    );
</script>

<template>
    <section class = 'FirstPar'>
        <div class="content">
            <div class = 'MainPart'>  
                <div class="centerText">
                    <h1>
                        <span style="color: #259073;">Регистрация</span>
                    </h1>
                    <input v-model="username" class="textbox" type="text" name="username" placeholder="Enter Username" required><br>
                    <input v-model="c_password" class="textbox" type="password" name="password" placeholder="Enter Password" required>
                    <p v-if = "password != ''" style='margin: 0' class = 'SimpleText'><i><SUP>Предлагаем:  {{password}}</SUP></i></p>
                    <input v-model="email" class="textbox" type="email" name="email" placeholder="Enter Email" required><br>
                    <select v-model="type_of_acc" name = 'type' class = 'select-css'>
                        <option>Разработчик</option>
                        <option>Игрок</option>
                        <option>Блогер/стример</option>
                    </select>
                    /*<p>{{resp}}</p>*/
                    <button @click = 'registration()' type='submit'>Отправить данные</button>
                    <p class = 'SimpleText'><i><SUP>Уже есть аккаунт? <router-link to="/enter">Вход</router-link></SUP></i></p>
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

    .select-css { 
        display: block; 
        font-size: 16px; 
        font-family: sans-serif; 
        font-weight: 700; 
        color: #444; 
        line-height: 1.3; 
        width: 90%;
        padding: 10px;
        /*padding: .6em 1.4em .5em .8em; width: 100%; */
        max-width: 100%;
        box-sizing: border-box; 
        margin: 5px; 
        border: 1px solid #aaa;
        box-shadow: 0 1px 0 1px rgba(0,0,0,.04); 
        border-radius: .5em;
        -moz-appearance: none;
        -webkit-appearance: none;
        appearance: none;
        background-color: #fff; 
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007CB2%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'), linear-gradient(to bottom, #ffffff 0%,#e5e5e5 100%); 
        background-repeat: no-repeat, repeat;
        background-position: right .7em top 50%, 0 0;
        background-size: .65em auto, 100%; 
        } 
        .select-css::-ms-expand { display: none; } 
        .select-css:hover { border-color: #888; } 
        .select-css:focus { border-color: #aaa; 
        box-shadow: 0 0 1px 3px rgba(59, 153, 252, .7);
        box-shadow: 0 0 0 3px -moz-mac-focusring; 
        color: #222;
        outline: none; 
        } 
        .select-css option { font-weight:normal; } 
        *[dir="rtl"] .select-css, :root:lang(ar) .select-css, :root:lang(iw) .select-css { 
        background-position: left .7em top 50%, 0 0; 
        padding: .6em .8em .5em 1.4em; 
    }

</style>