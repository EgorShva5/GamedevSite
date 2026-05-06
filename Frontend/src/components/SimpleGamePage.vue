<script setup>
    import background from '../assets/bckgweb.png'

    import { ref, onMounted } from 'vue'
    import axios from "axios"
    import {useRoute} from "vue-router"
    

    const route = useRoute();
    
    const message = ref();
    const deep_info = ref({});

    const screen_catalog = ref();
    const screens = ref([]);

    async function get_game() {
        try {
            message.value = await axios.get('http://localhost:8000/GamePage', {params: {id: route.params.id}});
            message.value = message.value.data
        } catch {
            message.value='failed to get response';
        };
    }

    async function get_game_deep_info() {
        try {
            let data = await axios.get('http://localhost:8000/GameDeepInfo', {params: {id: route.params.id}});
            deep_info.value = data.data.message;
            screen_catalog.value = data.data.message.screens.split(',')[0];
            screens.value = data.data.message.screens.split(',')/*.slice(1,-1)*/
        } catch {
            message.value='failed to get response';
        };
    }

    function getImageUrl(name) {
        console.log(`../assets/DevMB/scr1.jpg`, `../assets/${name}`)
        name = name.toString()
        name = name.trim()
        console.log(new URL(`../assets/DevMB/scr1.jpg`, import.meta.url).href)
        return new URL(`../assets/${name}`, import.meta.url).href
    }

    let currentSlide = 0;
 
    function showSlide(index) {
        const slides = document.querySelectorAll('.slide');

 
        if (index >= slides.length) {
            currentSlide = 0;
        } else if (index < 0) {
            currentSlide = slides.length - 1;
        } else {
            currentSlide = index;
        }
        const offset = -currentSlide * 100;

        document.querySelector('.slides').style.transform = `translateX(${offset}%)`;   
    }
 
    function nextSlide() {
        showSlide(currentSlide + 1);
    }

 
    function prevSlide() { 
        showSlide(currentSlide - 1);
    }

    onMounted(
    () => {
        get_game();
        get_game_deep_info();
    }
    );
    
    document.addEventListener('DOMContentLoaded', () => {
        showSlide(currentSlide);
    });

</script>

<template v-if="message.value">
    <section class = 'MainContent'>
        <div class = 'MainContainer'>
            <div style="color:black" v-for="msg in message">
                <h1 id = 'title'>{{ msg.title }}</h1>
                
                <div class = 'ImageContainer'>
                    <img id ='banner' :src="getImageUrl(msg.imgpath)" alt="Картинка">
                     
                    <div class="slider">  
                        <div class="slides">
                            <template v-for='screen in screens'>
                                <div class="slide">
                                    <a :href = 'getImageUrl(screen)'> 
                                        <img :src="getImageUrl(screen)" :alt="'Image' +screen">
                                    </a>
                                </div>
                            </template>
                        </div>
                        <button class="prev" @click="prevSlide()">❮</button>
                        <button class="next" @click="nextSlide()">❯</button>
                    </div>
                </div>
                <div class = 'Description'>
                    <h1 class = 'unique_color'>Описание игры:</h1>
                    <h2>{{ msg.description }}</h2>
                </div>
                <div class="LastContainer">
                    <div class = 'OtherContent'>
                        <h1 class = 'unique_color'>Где скачать?</h1>
                        <a :href='msg.linkpath' target='_blank'>Ссылка на игру!</a>
                        <div class = 'DevBanner'>
                            <img id = 'DevImage' alt = 'Разраб' src = '../assets/GoogPlayIco.jpg'/>
                            <div class = 'DevBanner_h'>
                                <h1>Разработчик:</h1>
                                <h2>Shvap Games</h2>
                            </div>
                        </div>

                        <div> 
                            <h1 class='unique_color'>Обзоры:</h1> <br>
                            <textarea name = 'MainText' id = 'MainText' style='width: 90%; height: 50px' placeholder = 'Напишите основной текст вопроса' required></textarea><br>
                            <a class = 'SimpleBtn'>Отправить</a>
                            <br>
                            <h2>Пока обзоров нет :(</h2>
                        </div>
                    </div>

                    <div class = 'RatingContainer'>
                        <h2>Надо играть (Нет/да)? <span style="color: coral;">{{deep_info.r_bad}}</span>/<span style="color: #51ec9cff;">{{deep_info.r_good}}</span> </h2>
                        <h1 class="unique_color">Рейтинг:</h1>
                        <h3>Визуал: 5/10</h3>
                        <h3>Саунд: 6/10</h3>
                        <h3>Геймплей: 7/10</h3>
                        <h3>Время в игре: 21 ч.</h3>
                        <h3>Общее впечатление: 9/10</h3>
                        <h3>Отсутствие багов: 5/10</h3> 
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

    #DevImage {
        height: 100px;
        border-radius: 100%;
        margin: 10px;
    }

    .DevBanner {
        display: flex;
        color: white;
        flex-direction: row;
        margin-top: 20px;
    }

    .DevBanner_h {
        * {
            margin: 0px;
        }
    }

    .OtherContent {
        min-width: 40vw;
        max-width: 40vw;
    }

    .LastContainer {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding-left: 5vw;
        padding-right: 5vw;

        h2 {
            color: white;
        }
    }

    .RatingContainer {
        color: white;

        * {
            margin: 6px;
            padding: 0px;
        }
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

    .slider {
        position: relative;
        width: 80%;
        max-width: 600px;
        overflow: hidden;
        border: 2px solid #ddd;
        border-radius: 10px;
        background-color: #fff;
    }

 
    .slides {
        display: flex;
        transition: transform 0.5s ease-in-out;
    }

    .slide {
        min-width: 100%;
        box-sizing: border-box;
    }

 
    .slide img {
        width: 100%;
        display: block;
    }

 
    button {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: rgba(0, 0, 0, 0.5);
        color: #fff;

        border: none;
        padding: 10px;
        cursor: pointer;
        border-radius: 50%;
    }

 
    button.prev {
        left: 10px;
    }

    button.next {
        right: 10px;
    }
</style>