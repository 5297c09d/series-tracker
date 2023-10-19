import { createApp } from 'vue';
import App from './App.vue';
import LoginForm from './components/LoginForm.vue';
import RegistrationForm from './components/RegistrationForm.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: LoginForm },
  { path: '/about', component: RegistrationForm },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.use(router); // Добавляем роутер в приложение

app.mount('#app'); // Запускаем приложение

