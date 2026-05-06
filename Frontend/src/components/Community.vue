<script setup>
    import { compile, ref, Transition, computed, onMounted } from 'vue'
    import axios from "axios"
    import Home from '../App.vue'
    import BlogCard from '../components/CommunityCardComponent.vue'

    let password = ''

    async function getPassword() {
        try {
            const res = await axios.get('http://localhost:8000/GenPassword', {timeout: 5000})
            console.log(res)
            let data = res.data.message
            password = data

            console.log(password)
        } catch {
            message.value='failed to get response'
        }
    }
    const posts = [
        {
            id: 1,
            image: 'https://picsum.photos/id/46/400/250',
            title: 'Искусство минимализма в веб-дизайне',
            content: 'Минимализм – это не просто отсутствие элементов, это продуманная эстетика, которая улучшает UX и фокусирует внимание на контенте. В этой статье мы разбираем ключевые принципы минималистичного дизайна и показываем примеры успешных реализаций.',
            tags: ['дизайн', 'ux', 'минимализм'],
            user: {
            name: 'Анна Крылова',
            handle: '@anna_design',
            avatar: 'https://randomuser.me/api/portraits/women/68.jpg',
            date: '2025-03-10T10:00:00Z'
            }
        },
        {
            id: 2,
            image: 'https://picsum.photos/id/0/400/250',
            title: 'Vue 3: новые возможности композиции',
            content: 'Composition API открывает гибкие способы организации логики. Рассмотрим практические примеры с `script setup`, реактивность и переиспользуемые композабулы.',
            tags: ['vue', 'javascript', 'frontend'],
            user: {
            name: 'Максим Иванов',
            handle: '@max_dev',
            avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
            date: '2025-03-05T14:30:00Z'
            }
        },
        {
            id: 3,
            image: 'https://picsum.photos/id/243/400/252',
            title: 'Возможности выпуска игры в стим в реалиях России',
            content: 'В современных условиях обычному работяге из России довольно сложно опубликовать свою игру на крупнейшую ПК-площадку Steam. В этой статье мы рассмотрим различные варианты публикации',
            tags: ['steam', 'публикация', 'санкции'],
            user: {
            name: 'Иван Годунов',
            handle: '@go_dun_132',
            avatar: 'https://randomuser.me/api/portraits/men/34.jpg',
            date: '2025-03-05T14:30:00Z'
            }
        },
        {
            id: 4,
            image: 'https://picsum.photos/id/23/400/251',
            title: 'Vue 3: новые возможности композиции',
            content: 'Composition API открывает гибкие способы организации логики. Рассмотрим практические примеры с `script setup`, реактивность и переиспользуемые композабулы.',
            tags: ['vue', 'javascript', 'frontend'],
            user: {
            name: 'Максим Иванов',
            handle: '@max_dev',
            avatar: 'https://randomuser.me/api/portraits/men/22.jpg',
            date: '2025-03-05T14:30:00Z'
            }
        }
        ]

    console.log(Home, 'current_user')
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
                <h1>Сообщество</h1>
                <ul class = 'header_btns'>
                    <li>Популярное</li>
                    <li>Последние</li>
                    <li>С лучшим рейтингом</li>
                    <li>Рекомендуемое</li>
                </ul>
            </div>

            <BlogCard
                v-for="post in posts"
                :key="post.id"
                :postImage="post.image"
                :title="post.title"
                :content="post.content"
                :tags="post.tags"
                :user="post.user"
            />
        </div>
    </section>
</template>

<style lang="css" scoped>
  .header_btns {
      font-size: 16px;
      cursor: pointer;
      gap: 20px;
      display: flex;
      list-style: none;
  }

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
        height: 15vh;
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