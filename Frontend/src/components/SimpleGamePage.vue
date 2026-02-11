<script setup>
    import Sanya from '../assets/201072348.png'
    import Goga from '../assets/GoogPlayIco.jpg'
    import { ref, onMounted } from 'vue'
    import axios from "axios"
    import {useRoute} from "vue-router"
    
    const route = useRoute();
    
    const message = ref();

    async function get_game() {
        try {
            message.value = await axios.get('http://localhost:8000/GamePage', {id: route.params.id}) ;
            message.value = message.value.data
        } catch {
            message.value='failed to get response';
        };
    }
    
    onMounted(
    () => {
      get_game();
    }
    );
    
</script>

<template v-if="message.value">
    <div style="color:black" v-for="msg in message">
        <h1>{{ msg.title }}</h1>
        <h2>{{ msg.description }}</h2>
        <img :src="msg.imgpath" alt="Картинка">
        <a :href='msg.linkpath' target='_blank'>Ссылка на игру!</a>
    </div>
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