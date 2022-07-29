<template>
  <NavBar></NavBar>
  <RouterView />
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  created() {
    this.$axios.interceptors.response.use(
      (res) => {
        return res;
      },
      (err) => {
        if (err.response.status === 401) {
          this.$store.dispatch("unauthorized");
          this.$router.push("/login");
        }
        return Promise.reject(err);
      }
    );
    this.$store.state.axios = this.$axios;
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
