import { mount } from '@vue/test-utils';
import MockAdapter from 'axios-mock-adapter';
import LoginForm from '../components/LoginForm.vue';
import axios from 'axios';

test('test login form can register', async () => {
    const loginFormWrapper = mount(LoginForm);
    const axiosMock = new MockAdapter(axios);

    const expectedData = {
        username: 'testuser',
        password: 'testpassword1',
    };

    axiosMock.onPost('/api/v1/auth/login').reply(200, 'Success');

    await loginFormWrapper.setData({ formData: expectedData });
    await loginFormWrapper.find('form').trigger('submit.prevent');

    // Подождать, пока Vue обновит DOM
    await loginFormWrapper.vm.$nextTick();


    expect(loginFormWrapper.text()).toContain('Login successful');

    axiosMock.restore();
});

test('test login form error message', async () => {
    const loginFormWrapper = mount(LoginForm);
    const axiosMock = new MockAdapter(axios);

    // Подготовка данных
    const expectedData = {
        username: 'testuser',
        password: 'testpassword1',
    };

    // Эмуляция ошибки во время запроса
    axiosMock.onPost('/api/v1/auth/login').reply(404, 'Failed');

    // Заполнение данных формы и отправка формы
    await loginFormWrapper.setData({ formData: expectedData });
    await loginFormWrapper.find('form').trigger('submit.prevent');

    // Подождать, пока Vue обновит DOM
    await loginFormWrapper.vm.$nextTick();
    await new Promise((resolve) => setTimeout(resolve, 0));

    // Проверить, что элемент с классом .error-message видим и содержит текст
    const errorMessageElement = loginFormWrapper.find('.error-message');
    expect(errorMessageElement.exists()).toBe(true);
    expect(errorMessageElement.text()).toContain('Login failed. Please check your credentials.');

    axiosMock.restore();
});
