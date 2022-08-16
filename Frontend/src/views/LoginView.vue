<template>
  <div class="login-container">
    <div class="login-label">관리자 로그인</div>
    <div class="form-floating form-id">
      <input
        type="text"
        class="form-control"
        id="floatingInput"
        placeholder="ID"
        v-model="userid"
        @keypress="keypress"
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
        @keypress="keypress"
      />
      <label for="floatingPassword">Password</label>
    </div>
    <div class="login-fail-text" v-if="loginFail">
      ID 혹은 패스워드가 잘못 입력되었습니다.
    </div>
    <button
      class="btn btn-lg button-login"
      type="button"
      @click="click"
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
      loginFail: false,
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
        this.loginFail = true;
      }
    },
    click(ev) {
      if (ev.button === 0) {
        this.login();
      }
    },
    keypress(ev) {
      if (ev.keyCode === 0x0d) {
        this.login();
      }
    },
  },
  created() {
    if (this.$store.getters.isAuthed) {
      this.$router.push("/");
      return;
    }
  },
};
</script>

<style>
.login-container {
  width: 500px;
  margin: 150px auto;
  color: #354f52;
  font-weight: lighter;
}
.form-control {
  border-radius: 20px;
  background-color: #e8e8e8;
}
.form-id {
  margin-top: 80px;
  margin-bottom: 20px;
}
.form-pw {
  margin-bottom: 20px;
}
.login-fail-text {
  text-align: right;
  color: red;
}
.login-container button {
  margin-top: 20px;
  width: 100%;
  background-color: #84a98c;
  color: white;
  font-weight: regular;
}
.login-label {
  font-family: NanumBarunGothic;
  font-weight: 700;
  font-size: 30px;
}
</style>
