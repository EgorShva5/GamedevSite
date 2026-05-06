<script setup>
    import icon from '/icon.png'
    import greenScreen from '../assets/green_sc.jpg'

    let username = ''
    let password = ''

    const props = defineProps({
        game_info: {
            type: Object,
            required: true,
            default: () => {}
        }
    })

    async function EnterReq() {
        console.log(game_info)
    }

</script>

<template>
    <section class = 'FirstPar'>
        <div class="content">
            <div class = 'MainPart'>  
                <div class="centerText">
                    <h1>
                        <span style="color: #259073;">Мы думаем, вам подойдёт:</span>
                    </h1>
                    
                    <h2><span style="color: #259073;">{{game_info.title}}</span></h2>
                    <p>{{game_info.description}}</p>
                    <a @click = 'EnterReq()'>Продолжить посиск</a> <br>
                    <router-link :to="`/game/`+game_info.id" class = 'SimpleBtn'>Перейти к игре</router-link> 
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
        background-color: rgba(0, 0, 0, 0.88);
        position: fixed;
        min-width: 100vw;
        min-height: 100vh;
        display: flex;
        flex-direction:center;
        align-items:center;
    }

    .MainPart {
        color: white;
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