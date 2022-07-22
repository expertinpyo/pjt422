import { createStore } from "vuex";

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
      // TODO: localStorage 확인하는 코드 필요
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
          reject();
          return;
        }

        // TODO: login process
        const accessToken = userid + passwd;
        if (accessToken !== null) {
          commit("SET_ACCESS_TOKEN", accessToken);
          resolve();
          return;
        }

        reject();
      });
    },
    async logout({ commit, state }) {
      return new Promise((resolve, reject) => {
        if (state.accessToken === null) {
          reject();
          return;
        }

        // TODO: logout process
        const logoutSuccess = true;
        if (logoutSuccess) {
          commit("SET_ACCESS_TOKEN", null);
          resolve();
          return;
        }

        reject();
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
