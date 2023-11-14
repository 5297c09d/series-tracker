<template>
  <section id="page">
    <header class="header">
      <div class="div">TV Show Tracker</div>
    </header>
    <main>
        <div id="app">
          <loginPage></loginPage>
          <!--<bookmarksPage></bookmarksPage>-->
         <!---как то сделать сюда импорт из loginPage и страницы закладок-->
        </div>
    </main>
    <footer></footer>
  </section>
</template>

<script>

// import bookmarksPage from './pages/bookmarksPage.vue';

import loginPage from './pages/loginPage.vue';

export default {
  name: 'App',
  components: {
    loginPage
    // bookmarksPage,
  }
}

</script>

<style>
/* TODO: Скачать и вставить */
@import url('https://fonts.googleapis.com/css2?family=Bitter&display=swap');

:root {
  --color-pink: #bb509a;
}

html,
body,
#app {
  width: 100%;
  height: 100%;
  margin: 0;
}

#page {
  display: grid;
  width: 100%;
  height: 100%;
  grid-template-areas:
    "head"
    "main";
    /* "foot"; */
  grid-template-rows: 100px 1fr;
}

#page>header {
  grid-area: head;
  background-color: #0d1117;
}

#page>main {
  grid-area: main;
  background-color:#21262d;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* #page>footer {
  grid-area: foot;
  background-color: rgba(98, 168, 135, 1);
} */

 
  .header {
    font-family: 'Bitter', serif;
  display: flex;
  justify-content: center;
  align-items: center;
  color: wheat;
  font-size: 60px;
  }
</style>
