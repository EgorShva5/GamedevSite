<template>
    <div class="blog-card">
      <!-- Блок изображения -->
      <div class="card-image">
        <img 
          :src="postImage" 
          :alt="title"
          @error="handleImageError"
        />
        <!-- Плашка пользователя поверх изображения (альтернативный вариант) -->
        <!-- По заданию плашка – отдельный блок, поэтому она вынесена в тело карточки -->
      </div>
  
      <!-- Тело карточки -->
      <div class="card-body">
        <!-- Плашка пользователя -->
        <div class="user-plate">
          <img 
            class="user-avatar" 
            :src="user.avatar" 
            :alt="user.name"
          />
          <div class="user-info">
            <div class="user-name">{{ user.name }}</div>
            <div class="user-handle">{{ user.handle }}</div>
            <div class="post-date">{{ formattedDate }}</div>
          </div>
        </div>
  
        <!-- Название поста -->
        <h3 class="card-title">{{ title }}</h3>
  
        <!-- Основной текст (обрезается, если слишком длинный) -->
        <p class="card-text">{{ truncatedContent }}</p>
  
        <!-- Поле для тегов (список тегов) -->
        <div class="tags-field">
          <span 
            v-for="tag in tags" 
            :key="tag" 
            class="tag"
          >
            #{{ tag }}
          </span>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    // URL изображения поста
    postImage: {
      type: String,
      default: 'https://picsum.photos/id/1/400/250'
    },
    // Заголовок поста
    title: {
      type: String,
      required: true
    },
    // Основной текст (может быть длинным)
    content: {
      type: String,
      required: true
    },
    // Массив тегов (строки)
    tags: {
      type: Array,
      default: () => []
    },
    // Объект пользователя: аватар, имя, ник, дата публикации
    user: {
      type: Object,
      required: true,
      validator: (value) => value.name && value.avatar && value.handle
    },
    // Максимальная длина основного текста
    maxContentLength: {
      type: Number,
      default: 120
    }
  })
  
  // Обрезка длинного текста
  const truncatedContent = computed(() => {
    if (props.content.length > props.maxContentLength) {
      return props.content.slice(0, props.maxContentLength) + '...'
    }
    return props.content
  })
  
  // Форматирование даты (если передана строка или timestamp)
  const formattedDate = computed(() => {
    if (!props.user.date) return ''
    const date = new Date(props.user.date)
    return date.toLocaleDateString('ru-RU', {
      day: 'numeric',
      month: 'short',
      year: 'numeric'
    })
  })
  
  // Запасное изображение при ошибке загрузки
  const handleImageError = (e) => {
    e.target.src = 'https://picsum.photos/id/20/400/250'
  }
  </script>
  
  <style scoped>
  /* Стили карточки */

  .blog-card {
    min-width: 40vw;
    background: #2b2b2b;
    border-radius: 20px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.02);
    overflow: hidden;
    margin: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
  }
  
  .blog-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 30px -12px rgba(0, 0, 0, 0.15);
  }
  
  .card-image {
    width: 100%;
    height: 200px;
    overflow: hidden;
    background-color: #3c7556;
  }
  
  .card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }
  
  .blog-card:hover .card-image img {
    transform: scale(1.03);
  }
  
  /* Тело карточки */
  .card-body {
    padding: 1.25rem;
  }
  
  /* Плашка пользователя */
  .user-plate {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
  }
  
  .user-avatar {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #e5e7eb;
  }
  
  .user-info {
    flex: 1;
    line-height: 1.3;
  }
  
  .user-name {
    font-weight: 600;
    font-size: 0.9rem;
    color: #259073;
  }
  
  .user-handle {
    font-size: 0.75rem;
    color: #6b7280;
  }
  
  .post-date {
    font-size: 0.7rem;
    color: #9ca3af;
    margin-top: 2px;
  }
  
  /* Название поста */
  .card-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin: 0 0 10px 0;
    color: #259073;
    line-height: 1.4;
  }
  
  /* Основной текст */
  .card-text {
    font-size: 0.9rem;
    line-height: 1.5;
    color: #9ca3af;
    margin-bottom: 16px;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  
  /* Поле для тегов */
  .tags-field {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
  }
  
  .tag {
    background: #f0fdf4;
    color: #15803d;
    font-size: 0.7rem;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 30px;
    letter-spacing: 0.3px;
    transition: background 0.2s;
  }
  
  .tag:hover {
    background: #dcfce7;
  }
  
  /* Адаптивность */
  @media (max-width: 480px) {
    .blog-card {
      max-width: 100%;
    }
    .card-body {
      padding: 1rem;
    }
  }
  </style>