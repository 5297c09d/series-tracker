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
      <div v-if="passwordsMissmatch" class="error-message">Пароли введены неверно</div>
    </form>
    <div class="success-message" v-if="showSuccessMessage">
      Registration successful
    </div>
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
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

.registration-card {
  background-color: #8ca0ff;
  border-radius: 100px;
  /* Rounded corners for the card */
  box-shadow: 0 5px 13px rgb(63, 63, 63);
  /* Shadow effect */
  padding: 50px;
  max-width: 300px;
  width: 100%;
  text-align: center;
}

.registration-form {
  font-family: 'Comic Neue', cursive;
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 20px;
  max-width: 400px;
  margin: 0 auto;
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
  border: 1px solid #000000ef;
  border-radius: 20px;
  outline: none;
}

button.rounded-button {
  font-family: 'Comic Neue', cursive;
  background-color: #3f6c9b;
  color: #000000;
  border: 1px solid #000000ef;
  border-radius: 30px;
  padding: 15px 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
  box-shadow: 0 5px 13px rgb(63, 63, 63);
  margin: auto;
  width: 50%;
}

button.rounded-button:hover {
  font-family: 'Comic Neue', cursive;
  background-color: #225184;
  transform: scale(1.05);
  color: #ffffff;
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
</style>
  