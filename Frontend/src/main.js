import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'  
import Home from './components/MainPage.vue'
import AboutUs from './components/AboutUs.vue'

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
    }]
})

createApp(App)
  .use(router)
  .mount('#app')