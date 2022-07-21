<template>
  <div class="login-container">
    <h1>관리자 로그인</h1>
    <div class="form-floating form-id">
      <input
        type="text"
        class="form-control"
        id="floatingInput"
        placeholder="ID"
        v-model="userid"
      />
      <label for="floatingInput">ID</label>
    </div>
    <div class="form-floating form-pw">
      <input
        type="password"
        class="form-control"
        id="floatingPassword"
        placeholder="Password"
        v-model="passwd"
      />
      <label for="floatingPassword">Password</label>
    </div>
    <div class="login-fail-text" v-if="login_fail">
      ID 혹은 패스워드가 잘못 입력되었습니다.
    </div>
    <button
      class="btn btn-lg btn-primary button-login"
      type="button"
      @click="login()"
      :disabled="userid === '' || passwd === ''"
    >
      LOGIN
    </button>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      userid: "",
      passwd: "",
      login_fail: false,
    };
  },
  methods: {
    async login() {
      try {
        await this.$store.dispatch("login", {
          userid: this.userid,
          passwd: this.passwd,
        });
        this.$router.push("/");
      } catch {
        this.userid = "";
        this.passwd = "";
        this.login_fail = true;
      }
    },
  },
  mounted() {
    if (this.$store.getters.is_authed) {
      this.$router.push("/");
      return;
    }
  },
};
</script>

<style>
.login-container {
  width: 500px;
  margin-left: auto;
  margin-right: auto;
}
.form-id {
  margin-top: 40px;
  margin-bottom: 10px;
}
.form-pw {
  margin-bottom: 10px;
}
.login-fail-text {
  text-align: right;
  color: red;
}
.button-login {
  margin-top: 20px;
  width: 100%;
}
</style>
