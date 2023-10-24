<template>
  <div>
    <div class="container">

      <div class="input-group">
        <label for="myInputForTheName">Enter the name of the show:</label>
        <input v-model="newBookmark.name" type="text" id="myInputForTheName" placeholder="Enter a name" size="70">
      </div>

      <div class="input-group">
        <label for="myInputForLink">Link to the pleiard with the series:</label>
        <input v-model="newBookmark.link" type="url" id="myInputForLink" placeholder="Enter the link" size="70">
      </div>

      <button class="create-button" @click="createBookmark">Create a bookmark</button>
    </div>
    <div class="grid">
      <bookmarkCard v-for="(bookmark, index) in bookmarks" :key="index" :bookmark="bookmark" @remove="removeBookmark">
      </bookmarkCard>
    </div>
  </div>
</template>

<script>
import bookmarkCard from '../components/bookmarkCard.vue';

export default {
  data() {
    return {
      bookmarks: [],
      newBookmark: {}
    };
  },
  components: {
    bookmarkCard,
  },
  methods: {
    createBookmark() {
      // Добавляем новую закладку в массив bookmarks
      this.bookmarks.push({ ...this.newBookmark });

      // Очищаем поля ввода
      this.newBookmark.name = '';
      this.newBookmark.link = '';
    },
    removeBookmark(bookmark) {
      // Находите индекс закладки в массиве bookmarks и удаляете ее
      const index = this.bookmarks.indexOf(bookmark);
      if (index !== -1) {
        this.bookmarks.splice(index, 1);
      }
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 30vh;
}

.input-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  /* Опциональный отступ между группами полей */
}

.create-button {
  color: rgb(165, 42, 75)
}

.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  /* 5 столбцов в ширину */
  grid-template-rows: auto;
  /* 3 строки в высоту */
  gap: 60px;
  /* Опциональный отступ между элементами сетки */
}
</style>
