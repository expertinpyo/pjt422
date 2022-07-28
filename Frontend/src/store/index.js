import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    accessToken: null,
    selectedTrashbin: null,
    hoveredTrashbin: null,
  },
  getters: {
    isAuthed(state) {
      if (state.accessToken !== null) {
        return true;
      }
      const accessToken = window.localStorage.getItem("access-token");
      if (accessToken) {
        state.accessToken = accessToken;
        axios.defaults.headers.common["Authorization"] =
          "token " + state.accessToken;
        return true;
      }
      return false;
    },
  },
  mutations: {
    SET_ACCESS_TOKEN(state, accessToken) {
      state.accessToken = accessToken;
    },
    SET_SELECTED_TRASHBIN(state, trashbin) {
      state.selectedTrashbin = trashbin;
    },
    SET_HOVERED_TRASHBIN(state, trashbin) {
      state.hoveredTrashbin = trashbin;
    },
  },
  actions: {
    async login({ commit, state }, { userid, passwd }) {
      return new Promise((resolve, reject) => {
        if (state.accessToken !== null) {
          // TODO: expired check
          reject();
          return;
        }

        const login_url =
          process.env.VUE_APP_BACKEND_HOST + "/api/v1/accounts/login/";
        const login_payload = {
          username: userid,
          password: passwd,
        };

        axios
          .post(login_url, login_payload)
          .then((res) => {
            const accessToken = res?.data?.key;
            if (accessToken !== null) {
              commit("SET_ACCESS_TOKEN", accessToken);
              window.localStorage.setItem("access-token", accessToken);
              axios.defaults.headers.common["Authorization"] =
                "token " + state.accessToken;
              resolve();
              return;
            }
            reject();
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
    async logout({ commit, state }) {
      return new Promise((resolve, reject) => {
        if (state.accessToken === null) {
          reject();
          return;
        }

        const logout_url =
          process.env.VUE_APP_BACKEND_HOST + "/api/v1/accounts/logout/";
        const logout_payload = {
          key: state.accessToken,
        };

        axios
          .post(logout_url, logout_payload)
          .then(() => {
            commit("SET_ACCESS_TOKEN", null);
            window.localStorage.removeItem("access-token");
            delete axios.defaults.headers.common["Authorization"];
            resolve();
          })
          .catch((err) => {
            commit("SET_ACCESS_TOKEN", null);
            window.localStorage.removeItem("access-token");
            delete axios.defaults.headers.common["Authorization"];
            reject(err);
          });
      });
    },
    setHoveredTrashbin({ commit }, trashbin) {
      commit("SET_HOVERED_TRASHBIN", trashbin);
    },
    setSelectedTrashbin({ commit }, trashbin) {
      commit("SET_SELECTED_TRASHBIN", trashbin);
    },
  },
  modules: {},
});
