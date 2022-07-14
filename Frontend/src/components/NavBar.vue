<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/" exact>프로젝트명</RouterLink>
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
          <li class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/stats">
              통계
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" active-class="active" to="/settings">
              설정
            </RouterLink>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <RouterLink class="nav-link" to="/logout">로그아웃</RouterLink>
          </li>
          <li v-else class="nav-item">
            <RouterLink class="nav-link" to="/login">로그인</RouterLink>
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
    isLoggedIn() {
      // TODO: 로그인 방법과 저장공간 정의
      return false;
    },
  },
};
</script>
