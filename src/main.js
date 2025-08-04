import './assets/main.css'
import './assets/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import fadeIn from './directives/fadeIn'

const app = createApp(App)

app.use(router)

app.directive('fade-in', fadeIn)

app.mount('#app')
