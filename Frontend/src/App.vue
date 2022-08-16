<template>
  <NavBar></NavBar>
  <RouterView />
</template>

<script>
import NavBar from "@/components/navbar/NavBar.vue";

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
@font-face {
  font-family: "NanumBarunGothic";
  font-style: normal;
  font-weight: 400;
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot");
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot?#iefix")
      format("embedded-opentype"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.woff")
      format("woff"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.ttf")
      format("truetype");
}
@font-face {
  font-family: "Pretendard-Regular";
  src: url("https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff")
    format("woff");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "GowunBatang-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/GowunBatang-Regular.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: Pretendard-Regular;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
