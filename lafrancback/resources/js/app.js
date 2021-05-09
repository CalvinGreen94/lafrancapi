require('./bootstrap');
window.Vue = require('vue');
  
Vue.component('multiple-image-component', require('./components/MultipleImageUploadComponent.vue'));
  
const app = new Vue({
    el: '#app'
});
