import { createStore } from "vuex";

export default createStore({
  state: {
    access_token: null,
  },
  getters: {
    is_authed(state) {
      if (state.access_token !== null) {
        return true;
      }
      // TODO: localStorage 확인하는 코드 필요
      return false;
    },
  },
  mutations: {
    SET_ACCESS_TOKEN(state, access_token) {
      state.access_token = access_token;
    },
  },
  actions: {
    async login({ commit, state }, { userid, passwd }) {
      return new Promise((resolve, reject) => {
        if (state.access_token !== null) {
          reject();
          return;
        }

        // TODO: login process
        const access_token = userid + passwd;
        if (access_token !== null) {
          commit("SET_ACCESS_TOKEN", access_token);
          resolve();
          return;
        }

        reject();
      });
    },
    async logout({ commit, state }) {
      return new Promise((resolve, reject) => {
        if (state.access_token === null) {
          reject();
          return;
        }

        // TODO: logout process
        const logout_success = true;
        if (logout_success) {
          commit("SET_ACCESS_TOKEN", null);
          resolve();
          return;
        }

        reject();
      });
    },
  },
  modules: {},
});
