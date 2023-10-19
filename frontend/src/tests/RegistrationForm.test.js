import { mount } from '@vue/test-utils'; // Import mount from @vue/test-utils
import MockAdapter from 'axios-mock-adapter'; // Import MockAdapter from axios-mock-adapter
import RegistrationForm from '../components/RegistrationForm.vue';
import axios from 'axios';

test('test registration form can register', async () => {
    const regFormWrapper = mount(RegistrationForm);
    const axiosMock = new MockAdapter(axios);

    const expectedData = {
        username: 'testuser',
        password1: 'testpassword1',
        password2: 'testpassword1',
    };

    axiosMock.onPost('/api/v1/auth/register').reply(200, 'Success');

    await regFormWrapper.setData({ formData: expectedData });
    await regFormWrapper.find('form').trigger('submit.prevent');

    await regFormWrapper.vm.$nextTick(); // Wait for Vue to update the DOM

    expect(regFormWrapper.text()).toContain('Registration successful');

    axiosMock.restore();
});

