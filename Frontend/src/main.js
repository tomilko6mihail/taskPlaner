import './assets/css/main.css'
import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import { definePreset } from '@primeuix/themes';
import Aura from '@primeuix/themes/aura';
import App from './App.vue'
import store from './store'
import components from '@/components/UI'
import ProgressBar from 'primevue/progressbar';

const MyPreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '{violet.50}',
            100: '{violet.100}',
            200: '{violet.200}',
            300: '{violet.300}',
            400: '{violet.400}',
            500: '{violet.500}',
            600: '{violet.600}',
            700: '{violet.700}',
            800: '{violet.800}',
            900: '{violet.900}',
            950: '{violet.950}'
        }
    },
    components: {
        progressbar: {
            value:{
               background: "{violet.800}"
            },
        }
    }
});

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app
.use(store)
.use(PrimeVue, {
    theme: {
        preset: MyPreset,
        options: {
            darkModeSelector: false || 'none',
        }
    }
})
///.component('Button', Button)
.component('ProgressBar', ProgressBar)
.mount('#app')
