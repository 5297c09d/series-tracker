<template>
  <div>
    <div class="container">

      <div class="input-group">
        <label for="myInputForTheName">Enter the name of the show:</label>
        <input v-model="newBookmark.name" type="text" id="myInputForTheName" placeholder="Enter a name" size="70">
      </div>

      <div class="input-group">
        <label for="myInputForLink">Link to player with series:</label>
        <input v-model="newBookmark.link" type="url" id="myInputForLink" placeholder="Enter the link" size="70">
      </div>

      <button class="btn" @click="createBookmark">
        <span class="text">Create a bookmark</span>
      </button>

      <!--<button class="create-button" @click="createBookmark">Create a bookmark</button>>-->
    </div>
    <div class="grid-section">
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
@import url('https://fonts.googleapis.com/css2?family=Abel&display=swap');


.input-group {
  font-family: 'Abel', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  color: wheat
}

/* .create-button {
  color: rgb(165, 42, 75)
} */


.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 30vh;
  margin-bottom: 20px;
  /* Добавьте отступ вниз */
}

.btn {
  border: none;
  width: 15em;
  height: 5em;
  border-radius: 19px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  background: #1C1A1C;
  cursor: pointer;
  transition: all 450ms ease-in-out;
  margin-top: 10px;
}

.sparkle {
  fill: #AAAAAA;
  transition: all 800ms ease;
}

.text {
  font-family: 'Abel', sans-serif;
  font-weight: 600;
  color: #AAAAAA;
  font-size: medium;
}

.btn:hover {
  background: linear-gradient(0deg, #fa82ae, #FF2C78);
  box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.4),
    inset 0px -4px 0px 0px rgba(0, 0, 0, 0.2),
    0px 0px 0px 4px rgba(255, 255, 255, 0.2),
    0px 0px 180px 0px #FF2C78;
  transform: translateY(-2px);
}

.btn:hover .text {
  color: wheat;
}

.btn:hover .sparkle {
  fill: wheat;
  transform: scale(1.2);
}

.grid-section {
  display: grid;
  grid-template-columns: repeat(4, 1fr); 
  grid-template-rows: auto;
  gap: 20px; 
  background-color:#0d1117; 
  padding:10px; 
  border-radius:10px; 
}
</style>
