<script setup>
  import { computed, onMounted } from 'vue'

  const props = defineProps({
    allSlides: {
      type: Array,
      required: true,
      default: () => []
    },
    show: {
      type: Boolean,
      required: true,
      default: () => true
    }
  })

  const emit = defineEmits(['update-slides'])

  const PER_PAGE = 3
  const maxPages = computed(() => Math.ceil(props.allSlides.length / PER_PAGE))

  function setCurrentGames(page) {
    const updatedSlides = props.allSlides.map((slide, index) => {
      const first = (page - 1) * PER_PAGE
      const last = first + PER_PAGE
      
      return {
        ...slide,
        isHidden: !(index >= first && index < last)
      }
    })

    let updatedShow = !props.show

    emit('update-slides', updatedSlides)
    emit('update-show', updatedShow)

    setTimeout(()=>{
      updatedShow = !updatedShow

      emit('update-show', updatedShow)
    }, 140)
  }

  onMounted(() => {
    setCurrentGames(1)
  })
</script>

<template>
  <div class="controls">
    <button v-for="n in maxPages" class="btns_slider" type="button" @click="() => setCurrentGames(n)">{{ n }}</button>
  </div>
</template>

<style lang="css" scoped>
  /* Контейнер для точек управления (индикаторов) */
  .controls {
      text-align: center; /* Размещаем точки по центру */
      margin-top: 10px; /* Добавляем отступ сверху */
  }

  /* Стиль для точек переключения */
  .controls label {
      display: inline-block; /* Размещаем точки в строку */
      width: 15px; /* Размер точки */
      height: 15px;
      border-radius: 50%; /* Делаем точки круглыми */
      margin: 5px; /* Добавляем небольшой отступ между ними */
      cursor: pointer; /* Делаем курсор в виде руки при наведении */
  }

  .btns_slider {
      color: aliceblue;
      font-size: 20px;
      transition: all .2s;
      margin: 10px;
      margin-bottom: 20px;
      height: 30px;
      width: 30px;
      cursor: pointer;
      border-radius: 20px;
      border: 1px solid #259073;
      background-color: #259073;
  }

  .btns_slider:hover {
      scale: 1.2;
  }
</style>

<!---
  function FadeOut(box_opacity, game_box) {
    box_opacity = 1.0

    let timer = setInterval(function() {
      if (!game_box) console.error('Не существует')
      if (box_opacity <= 0) {
        clearInterval(timer);
    //    BtnsDisable()
      } 
      else {
        box_opacity -= 0.02
        game_box.style.opacity = box_opacity
      }
    }, 20);
  }

  function FadeIn(box_opacity, game_box) {
    box_opacity = 0.0

    let timer = setInterval(function() {
      if (!game_box) console.error('Не существует')
      if (box_opacity >= 1) {
        clearInterval(timer);
      } 
      else {
        box_opacity += 0.02
        game_box.style.opacity = box_opacity
      }
    }, 20);
  }
-->