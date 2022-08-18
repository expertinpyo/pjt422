<template>
  <div class="settings-container">
    <div class="page-selector">
      <RouterLink to="/settings/building" active-class="active">
        <button class="btn btn-outline-primary">건물 관리</button>
      </RouterLink>
      <RouterLink to="/settings/user" active-class="active">
        <button class="btn btn-outline-primary">사용자 목록</button>
      </RouterLink>
      <RouterLink to="/settings/manager" active-class="active">
        <button class="btn btn-outline-primary">관리자 목록</button>
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
  border-right: 1px solid black;
  padding: 10px;
  margin-right: 0;
}
.page-selector > a {
  margin: 20px 0;
}
.page-selector button {
  width: 120px;
}
.settings-page {
  width: 100%;
}
</style>
