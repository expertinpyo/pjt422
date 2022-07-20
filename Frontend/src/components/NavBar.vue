<template>
  <nav class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/" exact>
        <img src="@/assets/logo.png" width="39" height="39" />
        422
      </RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse flex-grow-0"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex">
          <li class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/" exact>
              메인
            </RouterLink>
          </li>
          <li v-if="is_authed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/stats">
              통계
            </RouterLink>
          </li>
          <li v-if="is_authed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/settings">
              설정
            </RouterLink>
          </li>
          <li v-if="is_authed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/logout">
              로그아웃
            </RouterLink>
          </li>
          <li v-if="!is_authed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/login">
              로그인
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  computed: {
    is_authed() {
      return this.$store.getters.is_authed;
    },
  },
};
</script>

<style>
.nav-link {
  max-width: 120px;
  margin-left: auto;
  margin-right: auto;
  font-weight: bold;
}
.nav-link.active {
  border-bottom: 1px solid black;
}
</style>
