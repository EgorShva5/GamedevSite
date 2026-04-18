<script setup>
    import background from '../assets/bckgweb.png'

    import { ref, onMounted } from 'vue'
    import axios from "axios"
    import {useRoute} from "vue-router"
    

    const route = useRoute();
    
    const message = ref();

    async function get_game() {
        try {
            message.value = await axios.get('http://localhost:8000/GamePage', {params: {id: route.params.id}});
            message.value = message.value.data
        } catch {
            message.value='failed to get response';
        };
    }

    function getImageUrl(name) {
        return new URL(`../assets/${name}`, import.meta.url).href
    }

    onMounted(
    () => {
      get_game();
    }
    );
    
</script>

<template v-if="message.value">
    <section class = 'MainContent'>
        <div class = 'MainContainer'>
            <div style="color:black" v-for="msg in message">
                <h1 id = 'title'>{{ msg.title }}</h1>
                
                <div class = 'ImageContainer'>
                    <img id ='banner' :src="getImageUrl(msg.imgpath)" alt="Картинка">
                    <img class = 'screenshots' src="../assets/2026-04-08_21-31-49.png" alt="Картинка">
                </div>
                <div class = 'Description'>
                    <h1 class = 'unique_color'>Описание игры:</h1>
                    <h2>{{ msg.description }}</h2>
                </div>
                <div class="LastContainer">
                    <div>
                        <h1 class = 'unique_color'>Где скачать?</h1>
                        <a :href='msg.linkpath' target='_blank'>Ссылка на игру!</a>
                    </div>
                    
                </div>
                
            </div>
        </div>
    </section>
</template>

<style lang="css" scoped>
    .MainContent {
        background-image: url('../assets/bckgweb.png');
    }

    .MainContainer {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-width: 70vw;
        max-width: 70vw;
        margin: auto;
        background-color: rgba(0, 0, 0, 0.699);
        
    }

    .ImageContainer {
        margin: 20px;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;

        #banner {
            width: 35vh;
        }
    }

    .LastContainer {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }

    .screenshots {
        width: 640px;   
    }

    .unique_color {
       color: #259073;
       text-shadow: 0px 0px 10px black;
    }

    .Description {
        margin: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: antiquewhite;
    }

    #title {
        min-width: 40vw;
        text-align: center;
        margin: 20px;
        background-color: rgb(69, 153, 0);
        box-shadow: 0px 0px 20px rgb(0, 122, 31);
        color: white;
        text-shadow: 0px 0px 10px black;
    }

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