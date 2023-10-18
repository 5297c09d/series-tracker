<template>
  <div class="login-card">
    <form class="login-form" @submit.prevent="submitForm">
      <div class="input-container">
        <label for="username">User Name:</label>
        <input type="text" id="username" v-model="formData.username" required>
      </div>

      <div class="input-container">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="formData.password" required>
      </div>

      <button type="submit" class="rounded-button">Log in</button>

    </form>
    <div v-if="showSuccessMessage">
      Login successful
    </div>
    <div class="error-message" v-if="showErrorMessage">
      Login failed. Please check your credentials.
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
        password: '',
      },
      showSuccessMessage: false,
      showErrorMessage: false,
    };
  },
  methods: {
    async submitForm() {
      // Определите данные, которые вы хотите отправить в формате JSON
      const jsonData = {
        username: this.formData.username,
        password: this.formData.password,
      };

      try {
        const response = await axios.post('/api/v1/auth/login', jsonData, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (response.status === 200) {
          this.showSuccessMessage = true;
        } else {
          this.showErrorMessage = true;
        }

      } catch (error) {
        this.showErrorMessage = true;
      }
    },
  },
};
</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

.login-card {
  background-color: #8ca0ff;
  border-radius: 100px;
  box-shadow: 0 5px 13px rgb(63, 63, 63);
  padding: 50px;
  max-width: 300px;
  width: 100%;
  text-align: center;
}

.login-form {
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

.error-message {
  color: red;
  font-weight: bold;
  margin-top: 10px;
}
</style>
  