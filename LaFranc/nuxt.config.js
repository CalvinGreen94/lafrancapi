export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "LaFranc",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "Nuxt.js project" }
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900"
      },
      {
        rel: "stylesheet",
        href:
          "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
      },
      {
        rel: "stylesheet",
        href:
          "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
      }
    ],
    script: [
      {
        src: "https://code.jquery.com/jquery-3.3.1.slim.min.js",
        type: "text/javascript"
      },
      {
        src:
          "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
        type: "text/javascript"
      },

      {
        src:
          "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js",
        type: "text/javascript"
      }
    ]
  },
  env: {
    HOST_URL: process.env.HOST_URL || "http://127.0.0.1:8686/"
  },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: ["@nuxtjs/axios", "@nuxtjs/python"],
  python: {
    compiler: "pj" // default
  }

  // axios: { baseURL: "http://127.0.0.1:5055/" },
  // auth: {
  //   strategies: {
  //     local: {
  //       endpoints: {
  //         home: {
  //           url: "home",
  //           method: "post",
  //           // propertyName: "meta.token"
  //         },
  //         // user: {
  //         //   url: "user",
  //         //   method: "get",
  //         //   propertyName: "data"
  //         // },
  //         // logout: {
  //         //   url: "logout",
  //         //   method: "post"
  //         // }
  // }
};
