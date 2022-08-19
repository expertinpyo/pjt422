<template>
  <nav class="navbar navbar-expand-sm navbar-light">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/" exact>
        <img src="@/assets/logo.png" width="50" height="50" />
        <span class="navbar-brandname">싸피대학교 쓰레기통 관리 시스템</span>
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
          <li v-if="isAuthed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/noti">
              알림
            </RouterLink>
          </li>
          <li v-if="isAuthed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/stats">
              통계
            </RouterLink>
          </li>
          <!-- <li v-if="isAuthed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/settings">
              설정
            </RouterLink>
          </li> -->
          <li v-if="isAuthed" class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/logout">
              <span class="nav-item-logout">로그아웃</span>
            </RouterLink>
          </li>
          <li v-if="!isAuthed" class="nav-item">
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
    isAuthed() {
      return this.$store.getters.isAuthed;
    },
  },
};
</script>

<style>
.container-fluid {
  font-family: GowunBatang-Regular;
  font-weight: 700;
  border-bottom: 1.5px solid #828282;
}
.nav-link {
  max-width: 120px;
  margin: 5px 10px;
}
.nav-link.active {
  /* border-bottom: 1px solid black; */
}
.navbar-brandname {
  font-size: 18px;
  font-weight: bolder;
  padding: 0 10px;
}
.nav-item-logout {
  padding: 5px;
  border-radius: 10px;
  /* background-color: #a5b8a5; */
}
</style>
