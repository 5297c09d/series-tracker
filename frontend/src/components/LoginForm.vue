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
    <button class="button-spacing"> <router-link to="/registration">Register a new account</router-link> </button>
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

    goToDashboard(isAuthenticated) {
      if (isAuthenticated) {
        this.$router.push('/dashboard');
      } else {
        this.$router.push('/login');
      }
    },
  },
};

</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Abel&display=swap');

.login-card {
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

.login-form {
  font-family: 'Abel', sans-serif;
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 25px;
  max-width: 400px;
  color: wheat
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
  color: #FF2C78
}

button.rounded-button {
  /* font-family: 'Abel', sans-serif;
  background-color: #FF2C78;
  color: wheat;
  border: 1px solid #000000ef;
  border-radius: 19px;
  padding: 15px 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
  box-shadow: 0 5px 13px rgb(63, 63, 63);
  margin: auto;
  width: 50%; */
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
  /* font-family: 'Abel', sans-serif;
  background-color: #FF2C78;
  transform: scale(1.05);
  color: #000000; */
  box-shadow: 0 0 5px #FF2C78,
    0 0 25px #FF2C78,
    0 0 50px #fa82ae,
    0 0 100px #fa82ae;
}

.error-message {
  color: red;
  font-weight: bold;
  margin-top: 10px;
}

.button-spacing {
  margin-top: 30px;
  background-color: transparent;
  border: none;
  font-family: 'Abel', sans-serif;
  color: #000000;
  font-size: 18px
}
</style>
  