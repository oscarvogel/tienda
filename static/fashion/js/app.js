$(() => {
    new Vue({
      el: '#app',

      data () {
        return {
          info: null
        }
      },
      mounted () {
        let externalScript = document.createElement('script')
        externalScript.setAttribute('src', '/fashion/js/jquery-3.3.1.min.js')
        document.head.appendChild(externalScript)
        axios
          .get('/productos/api/v1.0/favoritos/')
          .then(response => (this.info = response))
      }
    })
});