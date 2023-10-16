
import { defineConfig } from 'vite'
import vue from "@vitejs/plugin-vue";

export default defineConfig({
    plugins: [
        vue()
    ],
    test: {
        // включить jest-подобные глобальные тестовые API
        globals: true,
        // Моделирование DOM с помощью happy-dom
        // (требует установки happy-dom в качестве одноранговой зависимости)
        environment: 'happy-dom'
    }
})