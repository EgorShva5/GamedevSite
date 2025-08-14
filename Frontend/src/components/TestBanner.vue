<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  const fieldBanner = ref('');
  const response = ref();

  async function getBanners() {
    try {
      const res = await axios.get('http://localhost:8000/', { params: { banner: fieldBanner.value || '1' }});
      response.value = res.data;
    } catch (error) {
      response.value = '';
    }
  }

  onMounted(
    () => {
      getBanners();
    }
  );
</script>

<template>
  <input class='field' v-model="fieldBanner" placeholder="номер"></input>
  <button class='btn' @click="getBanners">Get</button>
  <input class='field' :value="response" readonly></input>
  <div v-if="response" class='slider_container'>
          <div id ='Games' class="slider">           
              <div id ='game_box' class="slides">
                <template v-for='msg in response'>
                  <div class='slide'>
                    <a :href='msg.linkpath' target='_blank'>
                      <img :src="msg.imgpath" alt="Картинка">
                    </a>
                    <h1>{{ msg.title }}</h1>
                  </div>
                </template>
              </div>
          </div>
      </div>
</template>

<style lang="css" scoped>
  .slider {
    color: aliceblue;
  }
 img {
  max-width: 300px;
 }
</style>