import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'  
import Home from './components/MainPage.vue'
import AboutUs from './components/AboutUs.vue'
import HowToGet from './components/HowToGetInto.vue'
import GamePage from './components/SimpleGamePage.vue'
import Catalog from './components/Catalog.vue'
import Enter from './components/Enter.vue'
import Register from './components/Registration.vue'
import Opros from './components/Opros.vue'
import Community from './components/Community.vue'


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
        name: 'Game',
        params: true
    },
    {
        path: '/catalog',
        component: Catalog,
        name: 'Catalog'
    },
    {
        path: '/enter',
        component: Enter,
        name: 'Enter'
    },
    {
        path: '/registration',
        component: Register,
        name: 'Registration'
    },
    {
        path: '/opros',
        component: Opros,
        name: 'Opros'
    },
    {
        path: '/community',
        component: Community,
        name: 'Community'
    }
]})

createApp(App)
  .use(router)
  .mount('#app')