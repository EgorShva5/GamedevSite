import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'  
import Home from './components/MainPage.vue'
import AboutUs from './components/AboutUs.vue'
import HowToGet from './components/HowToGetInto.vue'
import GamePage from './components/SimpleGamePage.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [{
        path: '/',
        component: Home,
        name: 'Home'
    },
    {
        path: '/about',
        component: AboutUs,
        name: 'About US'
    },
    {
        path: '/how_to_get',
        component: HowToGet,
        name: 'How to get into'
    },
    {
        path: '/game/:id',
        component: GamePage,
        name: 'Game'
    }
]})

createApp(App)
  .use(router)
  .mount('#app')