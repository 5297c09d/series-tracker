<template>
  <section id="page">
    <header class="header">
      <h1>Series Tracker</h1>
    </header>
    <main>
      <!-- <RegistrationForm /> -->
      <LoginForm />
    </main>
    <footer></footer>
  </section>
</template>

<script>
//Login Form 💛

import LoginForm from './components/LoginForm.vue'

export default {
  components: {
    LoginForm
  },
}


//Registration Form 💜

// import RegistrationForm from './components/RegistrationForm.vue'

// export default {
//   components: {
//     RegistrationForm
//   },
// }

</script>

<style>
/* TODO: Скачать и вставить */
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

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
    "main"
    "foot";
  grid-template-rows: 50px 1fr 30px;
}

#page>header {
  grid-area: head;
  background-color: #8ca0ff;
}

#page>main {
  grid-area: main;
  background-color: #ffff64;
  display: flex;
  justify-content: center;
  align-items: center;
}

#page>footer {
  grid-area: foot;
  background-color: #8cffa0;
}

.header {
  font-family: 'Comic Neue', cursive;
  display: flex;
  justify-content: center;
  align-items: center;
  color: black
    /* Размер высоты, чтобы заголовок был посередине вертикально */
}

.header h1 {
  font-size: 40px;
  /* Размер шрифта заголовка */
  text-align: center;
  /* Выравнивание текста по центру горизонтально */
}
</style>
