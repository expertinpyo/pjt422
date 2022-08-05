import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: null,
    selectedTrashbin: null,
    hoveredTrashbin: null,
    axios: null,
    notifications: [],
  },
  getters: {
    isAuthed(state) {
      if (state.accessToken !== null) {
        return true;
      }
      const accessToken = window.localStorage.getItem("access-token");
      if (accessToken) {
        state.accessToken = accessToken;
        state.axios.defaults.headers.common["Authorization"] =
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
    SET_NOTIFICATIONS(state, notifications) {
      state.notifications = notifications;
    },
  },
  actions: {
    async login({ commit, state }, { userid, passwd }) {
      return new Promise((resolve, reject) => {
        if (state.accessToken !== null) {
          reject();
          return;
        }

        const loginUrl = "/api/v1/accounts/login/";
        const loginPayload = {
          username: userid,
          password: passwd,
        };

        state.axios
          .post(loginUrl, loginPayload)
          .then((res) => {
            const accessToken = res?.data?.key;
            if (accessToken !== null) {
              commit("SET_ACCESS_TOKEN", accessToken);
              window.localStorage.setItem("access-token", accessToken);
              state.axios.defaults.headers.common["Authorization"] =
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

        const logoutUrl = "/api/v1/accounts/logout/";
        const logoutPayload = {
          key: state.accessToken,
        };

        const afterPost = () => {
          commit("SET_ACCESS_TOKEN", null);
          window.localStorage.removeItem("access-token");
          delete state.axios.defaults.headers.common["Authorization"];
          resolve();
        };

        state.axios
          .post(logoutUrl, logoutPayload)
          .then(afterPost)
          .catch(afterPost);
      });
    },
    unauthorized({ commit, state }) {
      commit("SET_ACCESS_TOKEN", null);
      window.localStorage.removeItem("access-token");
      delete state.axios.defaults.headers.common["Authorization"];
    },
    setHoveredTrashbin({ commit }, trashbin) {
      commit("SET_HOVERED_TRASHBIN", trashbin);
    },
    setSelectedTrashbin({ commit }, trashbin) {
      commit("SET_SELECTED_TRASHBIN", trashbin);
    },
    async getNotifications({ commit, state, getters }) {
      return new Promise((resolve, reject) => {
        if (!getters.isAuthed) {
          commit("SET_NOTIFICATIONS", []);
          resolve();
          return;
        }

        const notiUrl = "/api/v1/campus/trashbin/check/";
        state.axios
          .get(notiUrl)
          .then((res) => {
            commit("SET_NOTIFICATIONS", res.data);
            resolve();
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
  },
  modules: {},
});
