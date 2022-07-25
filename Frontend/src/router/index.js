import { createRouter, createWebHistory } from "vue-router";
import MainView from "../views/MainView.vue";
import StatsView from "../views/StatsView.vue";
import SettingsView from "../views/SettingsView.vue";
import LoginView from "../views/LoginView.vue";
import SettingsBuilding from "../components/settings/SettingsBuilding.vue";
import SettingsManager from "../components/settings/SettingsManager.vue";
import SettingsUser from "../components/settings/SettingsUser.vue";
import store from "../store";

const requireAuth = () => (to, from, next) => {
  if (store.getters.isAuthed) {
    return next();
  }
  next("/login");
};

const logout = () => async (to, from, next) => {
  if (store.getters.isAuthed) {
    try {
      await store.dispatch("logout");
    } catch {
      // do nothing
    }
  }

  next("/login");
};

const routes = [
  {
    path: "/",
    name: "main",
    component: MainView,
  },
  {
    path: "/stats",
    name: "stats",
    component: StatsView,
    beforeEnter: requireAuth(),
  },
  {
    path: "/settings",
    name: "settings",
    component: SettingsView,
    children: [
      {
        path: "building",
        component: SettingsBuilding,
      },
      {
        path: "user",
        component: SettingsUser,
      },
      {
        path: "manager",
        component: SettingsManager,
      },
    ],
    beforeEnter: requireAuth(),
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/logout",
    name: "logout",
    beforeEnter: logout(),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
