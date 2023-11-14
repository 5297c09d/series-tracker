<template>
  <div class="registration-card">
    <form class="registration-form" @submit.prevent="submitForm">
      <div class="input-container" :class="{ 'has-error': passwordsMissmatch }">
        <label for="username">User Name:</label>
        <input type="text" id="username" v-model="formData.username" required>
      </div>

      <div class="input-container" :class="{ 'has-error': passwordsMissmatch }">
        <label for="password1">Password:</label>
        <input type="password" id="password1" v-model="formData.password1" required>
      </div>

      <div class="input-container" :class="{ 'has-error': passwordsMissmatch }">
        <label for="password2">Repeat the password:</label>
        <input type="password" id="password2" v-model="formData.password2" required>
      </div>
      <button type="submit" class="rounded-button">Sign up</button>
      <div v-if="passwordsMissmatch" class="error-message">Passwords entered incorrectly, try again</div>
    </form>
    <div class="success-message" v-if="showSuccessMessage">
      Registration successful
    </div>
    <button class="button-spacing"> <router-link to="/">Do you have an account already?</router-link> </button>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {

  data() {
    return {
      formData: {
        username: '',
        password1: '',
        password2: '',
      },
      showSuccessMessage: false,
      passwordsMissmatch: false, // Добавляем состояние для проверки совпадения паролей
    };
  },

  methods: {
    async submitForm() {
      if (this.formData.password1 !== this.formData.password2) {
        this.passwordsMissmatch = true
        return;

      } else {
        this.passwordsMissmatch = false
      }

      try {
        // Определите данные, которые вы хотите отправить в формате JSON
        const jsonData = {
          username: this.formData.username,
          password1: this.formData.password1,
          password2: this.formData.password2,
        };

        // Отправить POST-запрос с данными в формате JSON на указанную конечную точку
        await axios.post('/api/v1/auth/register', jsonData, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        // Здесь обрабатывается ответ, например, выводится сообщение об успехе
        this.showSuccessMessage = true;
      } catch (error) {
        // Обработка ошибок, например, вывод сообщения об ошибке
        console.error('Registration error:', error);
      }
    },
  },
};
</script>
  
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Abel&display=swap');

.registration-card {
  background-color: #1C1A1C;
  border-radius: 40px;
  box-shadow: 0 5px 13px rgb(0, 0, 0);
  padding: 50px;
  max-width: 300px;
  width: 100%;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  }

.registration-form {
  font-family: 'Abel', sans-serif;
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 20px;
  max-width: 300px;
  color:wheat
}

.input-container {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
}

input {
  padding: 10px;
  border-radius: 13px;
  outline: none;
  color:#FF2C78
}

button.rounded-button {
  font-family: 'Abel', sans-serif;
  padding: 10px 20px;
  border: none;
  font-size: 17px;
  color: #fff;
  border-radius: 7px;
  letter-spacing: 2px;
  font-weight: 700;
  text-transform: uppercase;
  transition: 0.5s;
  transition-property: box-shadow;
}

button.rounded-button {
  background: #FF2C78;
  box-shadow: 0 0 25px #fa82ae
}
button.rounded-button:hover {
  box-shadow: 0 0 5px #FF2C78,
    0 0 25px #FF2C78,
    0 0 50px #fa82ae,
    0 0 100px #fa82ae;
}

.has-error {
  border: 1px solid red;
  /* Устанавливаем красную рамку для полей */
}

.error-message {
  color: red;
  /* Устанавливаем красный цвет для текстового сообщения */
  font-size: 14px;
  /* Устанавливаем размер шрифта */
}

.button-spacing {
    margin-top: 30px;
    background-color: transparent;
    border: none;
    cursor: pointer;
    font-family: 'Abel', sans-serif;
    color: #000000; 
    font-size: 18px
  }

</style>
  