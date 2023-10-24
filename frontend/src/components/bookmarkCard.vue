<template>
    <div class="bookmark-card">
        <div class="bookmark-content">
            <!-- Примените стили к тексту внутри закладки -->
            <p class="bookmark-name">{{ bookmark.name.toUpperCase() }}</p>
            <a :href="bookmark.link" target="_blank">{{ bookmark.name }}</a>

            <button @click="removeBookmark">🗑️</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BookmarkCard',
    props: {
        bookmark: Object // Свойство, которое ожидает объект bookmark
    },

    methods: {
    removeBookmark() {
      // Вызывайте событие для удаления закладки, передавая `bookmark` в родительский компонент
      this.$emit('remove', this.bookmark);
    }
  }
}
</script>

<style scoped>
.bookmark-card {
    /* border: 1px solid #3696b9; */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 10px;
    background-color: #8ca0ff;
    border-radius: 5px;
    text-align: center;
}

a {
    color: #1100ff;
    /* Цвет ссылки */
}

.bookmark-content {
    text-align: center;
    /* Выравнивает текст по центру */
}

.bookmark-name {
    font-size: 18px;
    /* Размер шрифта для имени */
    font-weight: bold;
    /* Жирный шрифт */
    /* Дополнительные стили для имени */
}

.bookmark-link {
    font-size: 14px;
    /* Размер шрифта для ссылки */
    /* Дополнительные стили для ссылки */
}</style>