import axios from "axios";

const _axios = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_HOST,
});

export default {
  install: (app) => {
    app.config.globalProperties.$axios = _axios;
  },
};
