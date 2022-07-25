<template>
  <div class="settings-container">
    <div class="page-selector">
      <RouterLink to="/settings/building" active-class="active">
        건물 관리
      </RouterLink>
      <RouterLink to="/settings/user" active-class="active">
        사용자 목록
      </RouterLink>
      <RouterLink to="/settings/manager" active-class="active">
        관리자 목록
      </RouterLink>
    </div>
    <div class="settings-page">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsView",
};
</script>

<style scoped>
.settings-container {
  display: flex;
  flex-direction: row;
}
.page-selector {
  display: flex;
  flex-direction: column;
  width: 150px;
  border-right: 1px solid black;
  margin-right: 0;
}
.page-selector > a {
  text-decoration: none;
}
.settings-page {
  width: 100%;
}
div {
  border: 1px solid red;
}
</style>
