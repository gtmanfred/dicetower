import Vue from 'vue'
import App from './App.vue'
import {
  BootstrapVue,
  ButtonPlugin
} from 'bootstrap-vue'

Vue.config.productionTip = process.env.NODE_ENV === 'production'
Vue.use(BootstrapVue)
Vue.use(ButtonPlugin)

new Vue({
  render: h => h(App),
}).$mount('#app')
